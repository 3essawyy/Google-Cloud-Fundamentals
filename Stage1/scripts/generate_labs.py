import os
import re
from bs4 import BeautifulSoup, Comment

LAB_CONFIGS = [
    {
        "filename": "Lab1.html",
        "output": r"labs\01_Cloud_Marketplace.md",
        "rank": 1,
        "difficulty": "Starter / Easy",
        "time": "30 Minutes",
        "title": "Google Cloud Fundamentals: Getting Started with Cloud Marketplace",
        "module": "Module 1 & 2: Introduction & Resource Management",
        "ace_anchors": [
            "Compute Engine instance creation via pre-configured Marketplace solutions (LAMP stack)",
            "Default vs custom network interfaces and external IP assignment",
            "Firewall rule verification (allow-http, port 80)",
            "Shared responsibility model: OS/software maintenance on Marketplace VM deployments",
        ]
    },
    {
        "filename": "Lab2.html",
        "output": r"labs\02_VPC_and_Compute_Engine.md",
        "rank": 2,
        "difficulty": "Easy / Medium",
        "time": "40 Minutes",
        "title": "Get Started with Virtual Private Cloud Networking and Compute Engine",
        "module": "Module 3: Virtual Machines and Networks in the Cloud",
        "ace_anchors": [
            "VPC architecture: Global VPCs, regional subnets, and non-overlapping CIDR ranges",
            "Firewall rules: Targets (network tags), source IP ranges, protocols, and ports",
            "Compute Engine VMs across different zones in the same region vs different regions",
            "Internal DNS and private IP reachability vs external IP reachability via SSH and ICMP",
        ]
    },
    {
        "filename": "Lab3.html",
        "output": r"labs\03_Storage_and_Cloud_SQL.md",
        "rank": 3,
        "difficulty": "Medium",
        "time": "45 Minutes",
        "title": "Google Cloud Fundamentals: Getting Started with Cloud Storage and Cloud SQL",
        "module": "Module 4: Storage in the Cloud",
        "ace_anchors": [
            "Cloud Storage: Globally unique bucket names, multi-regional vs regional storage classes",
            "Cloud Storage CLI (`gcloud storage` vs legacy `gsutil`) and ACLs / public access prevention",
            "Cloud SQL: Managed relational DB (MySQL), instance provisioning, public vs private IP",
            "Application integration: Startup scripts, environment variables, and secure DB credentials",
        ]
    },
    {
        "filename": "Lab4.html",
        "output": r"labs\04_Hello_Cloud_Run.md",
        "rank": 4,
        "difficulty": "Medium / Hard",
        "time": "45 Minutes",
        "title": "Hello Cloud Run",
        "module": "Module 5 & 6: Containers & Applications in the Cloud",
        "ace_anchors": [
            "Cloud Run architecture: Fully managed serverless container runtime (Knative-based)",
            "Artifact Registry: Storing and managing Docker container images in GCP",
            "Container contract: Listening on PORT environment variable (default 8080), statelessness",
            "Deployment & Traffic Management: `--allow-unauthenticated`, traffic splitting between revisions",
        ]
    }
]

def clean_html_element(elem):
    """Recursively converts HTML elements into clean Markdown."""
    if not elem:
        return ""

    # Remove all HTML comments
    for c in elem.find_all(text=lambda t: isinstance(t, Comment)):
        c.extract()

    md_lines = []

    for child in elem.children:
        if isinstance(child, str):
            text = child.strip()
            if text:
                md_lines.append(text)
            continue

        name = child.name.lower() if child.name else ""

        if name in ["h1", "h2"]:
            t = child.get_text(strip=True)
            if t:
                md_lines.append(f"\n\n## {t}\n")
        elif name == "h3":
            t = child.get_text(strip=True)
            if t:
                md_lines.append(f"\n\n### {t}\n")
        elif name == "h4":
            t = child.get_text(strip=True)
            if t:
                md_lines.append(f"\n\n#### {t}\n")
        elif name in ["p", "div"]:
            # Check for inner code blocks or callouts first
            t = child.get_text(strip=True)
            if t:
                # If child contains nested elements like ql-code-block, process children
                if child.find(["ql-code-block", "pre", "table", "ul", "ol", "ql-infobox", "ql-warningbox"]):
                    sub = clean_html_element(child)
                    if sub.strip():
                        md_lines.append(sub)
                else:
                    md_lines.append(f"\n{t}\n")
        elif name in ["pre", "ql-code-block"]:
            code_text = child.get_text()
            # Clean up lit-html comments or trailing whitespace
            code_clean = re.sub(r"<!--.*?-->", "", code_text).strip()
            if code_clean:
                md_lines.append(f"\n```bash\n{code_clean}\n```\n")
        elif name == "ql-infobox":
            t = child.get_text(strip=True)
            t = re.sub(r"<!--.*?-->", "", t)
            md_lines.append(f"\n> ℹ️ **Note:**\n> {t}\n")
        elif name == "ql-warningbox":
            t = child.get_text(strip=True)
            t = re.sub(r"<!--.*?-->", "", t)
            md_lines.append(f"\n> ⚠️ **Warning:**\n> {t}\n")
        elif name in ["ql-activity-tracking", "ql-assessment"]:
            btn = child.find(["md-filled-button", "button", "ql-button"])
            step_name = child.get("step") or child.get_text(strip=True) or "Step Verification"
            md_lines.append(f"\n> 🎯 **Checkpoint / Check My Progress:** *Verify Task completion in Qwiklabs*\n")
        elif name == "ul":
            for li in child.find_all("li", recursive=False):
                li_text = li.get_text(strip=True)
                if li_text:
                    md_lines.append(f"* {li_text}")
            md_lines.append("")
        elif name == "ol":
            for idx, li in enumerate(child.find_all("li", recursive=False), 1):
                li_text = li.get_text(strip=True)
                if li_text:
                    md_lines.append(f"{idx}. {li_text}")
            md_lines.append("")
        elif name == "table":
            rows = child.find_all("tr")
            if rows:
                table_md = []
                headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
                if headers:
                    table_md.append("| " + " | ".join(headers) + " |")
                    table_md.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    for row in rows[1:]:
                        cols = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                        table_md.append("| " + " | ".join(cols) + " |")
                    md_lines.append("\n" + "\n".join(table_md) + "\n")
        else:
            # Fallback
            sub = clean_html_element(child)
            if sub.strip():
                md_lines.append(sub)

    return "\n".join(md_lines)


def process_lab(cfg):
    print(f"Parsing: {cfg['filename']} -> {cfg['output']}")
    with open(cfg["filename"], "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    inst_div = soup.select_one("div.markdown-lab-instructions")
    if not inst_div:
        print(f"ERROR: markdown-lab-instructions not found in {cfg['filename']}")
        return

    body_md = clean_html_element(inst_div)

    # Post-process body_md to clean multiple blank lines
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)
    # Remove lit comments remnants
    body_md = re.sub(r"<\!--\?lit\$\d+\$-->", "", body_md)

    # Extract all bash commands for Cloud Shell Quick Script
    code_blocks = re.findall(r"```bash\n(.*?)\n```", body_md, re.DOTALL)
    # Filter out username/password or single word blocks
    clean_commands = []
    for cb in code_blocks:
        cb_str = cb.strip()
        if "user_" not in cb_str and len(cb_str.splitlines()) >= 1 and not cb_str.startswith("{"):
            clean_commands.append(cb_str)

    # Build Header
    doc = []
    doc.append(f"# Lab {cfg['rank']}: {cfg['title']}")
    doc.append("")
    doc.append(f"> **Progression Rank:** {cfg['rank']} of 4 ({cfg['difficulty']})")
    doc.append(f"> **Estimated Time:** {cfg['time']} · **Target Track:** {cfg['module']}")
    doc.append(f"> **Role Trajectory:** Google Cloud Associate Cloud Engineer (ACE)")
    doc.append("")
    doc.append("---")
    doc.append("")

    # Quick Script Block
    if clean_commands:
        doc.append("## ⚡ Cloud Shell Quick-Reference Script")
        doc.append("*Consolidated CLI commands ready for pasting into Google Cloud Shell:*")
        doc.append("")
        doc.append("```bash")
        doc.append("#!/usr/bin/env bash")
        doc.append(f"# Lab {cfg['rank']}: {cfg['title']} - Quick Execution Script")
        doc.append("set -euo pipefail")
        doc.append("")
        for idx, cmd in enumerate(clean_commands, 1):
            doc.append(f"# Step Command block {idx}")
            doc.append(cmd)
            doc.append("")
        doc.append("```")
        doc.append("")
        doc.append("---")
        doc.append("")

    # Full Lab Instructions
    doc.append("## 📖 Lab Instructions & Walkthrough")
    doc.append(body_md)
    doc.append("")
    doc.append("---")
    doc.append("")

    # ACE Exam Anchors
    doc.append("## 🎓 Associate Cloud Engineer (ACE) Exam Anchors")
    doc.append("| Core Exam Domain | Practical Architectural Takeaway |")
    doc.append("| :--- | :--- |")
    for anchor in cfg["ace_anchors"]:
        parts = anchor.split(":", 1)
        if len(parts) == 2:
            doc.append(f"| **{parts[0].strip()}** | {parts[1].strip()} |")
        else:
            doc.append(f"| **Key Takeaway** | {anchor.strip()} |")
    doc.append("")

    # Verification Checklist
    doc.append("## ✅ Objective Verification Checklist")
    doc.append("- [ ] Lab sandbox environment provisioned and active.")
    doc.append("- [ ] Task 1 completed and verified.")
    doc.append("- [ ] Task 2 completed and verified.")
    doc.append("- [ ] Task 3 completed and verified.")
    if cfg["rank"] >= 2:
        doc.append("- [ ] Task 4 completed and verified.")
    if cfg["rank"] >= 3:
        doc.append("- [ ] Task 5 completed and verified.")
        doc.append("- [ ] Task 6 completed and verified.")
    doc.append("- [ ] All Qwiklabs progress checkmarks scored 100%.")
    doc.append("- [ ] Lab ended cleanly to avoid quota leakage.")

    final_content = "\n".join(doc)

    os.makedirs(os.path.dirname(cfg["output"]), exist_ok=True)
    with open(cfg["output"], "w", encoding="utf-8") as f_out:
        f_out.write(final_content)
    print(f"Successfully generated: {cfg['output']}")


def generate_roadmap():
    roadmap_path = r"labs\LAB_ROADMAP.md"
    content = """# Google Cloud Fundamentals — Hands-on Lab Progression Roadmap

> **Target Certification:** Google Cloud Certified Associate Cloud Engineer (ACE)
> **Execution Strategy:** Progressive complexity ramp-up (Rank 1: Starter -> Rank 4: Serverless/Containers)
> **Execution Environment:** Google Cloud Skills Boost / Qwiklabs sandbox + Cloud Shell

---

## 🗺️ Lab Sequence & Difficulty Matrix

| Rank | Lab Title | Module Mapping | Difficulty | Estimated Time | Key Services | Primary Interface |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- |
| **1** | [01_Cloud_Marketplace.md](01_Cloud_Marketplace.md) | M1 & M2: Intro / IAM | **Starter** | 30 min | Compute Engine, Marketplace, Firewall | GCP Console |
| **2** | [02_VPC_and_Compute_Engine.md](02_VPC_and_Compute_Engine.md) | M3: VMs & Networks | **Easy-Med** | 40 min | VPC Networks, Subnets, Compute VMs, ICMP/SSH | Cloud Shell + Console |
| **3** | [03_Storage_and_Cloud_SQL.md](03_Storage_and_Cloud_SQL.md) | M4: Storage | **Medium** | 45 min | Cloud Storage, Cloud SQL (MySQL), App Server | gcloud CLI + Console |
| **4** | [04_Hello_Cloud_Run.md](04_Hello_Cloud_Run.md) | M5 & M6: Containers & Apps | **Med-Hard** | 45 min | Docker, Artifact Registry, Cloud Run | Cloud Shell (gcloud + docker) |

---

## 🎯 Architectural Progression Breakdown

```mermaid
flowchart LR
    L1["Lab 1: Marketplace<br/>• Pre-packaged LAMP<br/>• Basic Firewalls (HTTP)<br/>• Console Familiarity"] 
    --> L2["Lab 2: VPC & Compute<br/>• Custom VPC & Subnets<br/>• Multi-zone VMs<br/>• Private vs Public IP Routing"]
    --> L3["Lab 3: Storage & SQL<br/>• Cloud Storage (GCS)<br/>• Cloud SQL Provisioning<br/>• App DB Binding"]
    --> L4["Lab 4: Cloud Run<br/>• Docker Containerization<br/>• Artifact Registry<br/>• Serverless Microservices"]

    style L1 fill:#e8f4f8,stroke:#007acc,color:#003b66
    style L2 fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style L3 fill:#eafaf1,stroke:#2ecc71,color:#145a32
    style L4 fill:#f5eef8,stroke:#8e44ad,color:#4a235a
```

---

## 📋 Progression Checklist

- [ ] **Rank 1:** `01_Cloud_Marketplace.md`
  - *Focus:* Deploy pre-packaged LAMP stack, verify Apache web server, review Compute Engine VM instance.
- [ ] **Rank 2:** `02_VPC_and_Compute_Engine.md`
  - *Focus:* Build custom VPC network, define firewall rules with target tags, deploy multi-zone VMs, test internal DNS & ICMP reachability.
- [ ] **Rank 3:** `03_Storage_and_Cloud_SQL.md`
  - *Focus:* Provision GCS bucket via `gcloud storage`, deploy Cloud SQL instance, configure Compute Engine web server to connect to SQL database and serve static assets from GCS.
- [ ] **Rank 4:** `04_Hello_Cloud_Run.md`
  - *Focus:* Write Dockerfile & Node.js app, package container image, upload to Artifact Registry, deploy serverless service to Cloud Run with public access.

---

## 💡 Best Practices for Sandbox Execution

1. **Incognito / Private Browsing:** Always open the Qwiklabs console link in an Incognito tab to prevent accidental account switching with your personal Google accounts.
2. **Copy-Paste into Cloud Shell:** Use the pre-built `⚡ Cloud Shell Quick-Reference Script` in each lab guide to save time and prevent manual typing mistakes.
3. **Verify Before Scoring:** Always run the verification commands listed in each lab guide before clicking **Check my progress** in Qwiklabs.
4. **Clean End:** Always click **End Lab** once you achieve 100% to ensure resources are torn down cleanly.
"""
    with open(roadmap_path, "w", encoding="utf-8") as f_out:
        f_out.write(content)
    print(f"Successfully generated: {roadmap_path}")

def main():
    os.makedirs("labs", exist_ok=True)
    for cfg in LAB_CONFIGS:
        process_lab(cfg)
    generate_roadmap()
    print("\n[SUCCESS] All 4 lab guides and master roadmap generated successfully.")

if __name__ == "__main__":
    main()
