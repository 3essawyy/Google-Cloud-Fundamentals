# Google Cloud Fundamentals — Workspace Instructions & Consultation Protocol

### 1. Workspace Mission & Target
* **Target Objective:** Master the *Google Cloud Fundamentals: Core Infrastructure* curriculum as the launchpad for the **Google Cloud Certified Associate Cloud Engineer (ACE)** exam.
* **Workspace Role:** Technical consultation hub, offline syllabus index, lab script generator, and local execution engine.

### 2. Dual-Agent Collaboration Contract
* **Claude (Web) — Primary Tutor & Interactive Driver:**
  * Leads conceptual lectures, Q&A, syllabus progression, and real-time interactive lab prompts.
* **Gemini (CLI) — Technical Consultant & Execution Engine:**
  * **Code & Script Validation:** Audits `gcloud`, `bash`, and container configs before execution in Cloud Shell.
  * **Offline Knowledge Index:** Maintains indexed Markdown slide notes (`modules/`) and lab manuals (`labs/`).
  * **Local Workhorse:** Handles document processing, local SDK/Python utilities, and Docker artifact builds that cannot run on the web.
  * **Zero Direct Mutation Without Approval:** Adheres strictly to the Global Profile's Plan-First Mandate.

### 3. Lab Sequence & Difficulty Progression
Execute labs progressively from easiest to hardest:
1. **Rank 1 (Starter):** `labs/01_Cloud_Marketplace.md`
   * *Domain:* GCP Console, pre-packaged LAMP stack deployment, basic HTTP firewall rules.
2. **Rank 2 (Easy/Medium):** `labs/02_VPC_and_Compute_Engine.md`
   * *Domain:* Custom VPCs, regional subnets, firewall rules with target tags, multi-zone VMs, internal DNS/ICMP.
3. **Rank 3 (Medium):** `labs/03_Storage_and_Cloud_SQL.md`
   * *Domain:* Cloud Storage (`gcloud storage`), Cloud SQL MySQL instance, web application DB binding.
4. **Rank 4 (Medium/Hard):** `labs/04_Hello_Cloud_Run.md`
   * *Domain:* Docker containerization, Artifact Registry, serverless Cloud Run deployments, revisions, and traffic splitting.
* **Master Tracker:** See `labs/LAB_ROADMAP.md` for full completion status and checklists.

### 4. Sandbox Execution & Security Standards
* **Qwiklabs / Skills Boost Sandboxes:** Labs use temporary disposable student accounts (`student-xx@qwiklabs.net`) and project IDs (`qwiklabs-gcp-xx`).
* **Browser Isolation:** Always open the GCP Console in an Incognito / Private window to eliminate collision with personal Google accounts.
* **Cloud Shell Snippet Protocol:** 
  * Prefer pasting verified command blocks directly into the browser Google Cloud Shell.
  * When scripting for Cloud Shell, enforce `set -euo pipefail` and explicit environment variables (`LOCATION`, `PROJECT_ID`).
* **Shell Command Safety:** Shell execution on Windows must remain strictly flat and literal (no `$()`, backticks, or PowerShell subexpressions).
* **Teardown Rule:** Always click **End Lab** immediately upon scoring 100% to avoid quota exhaustion.

### 5. Associate Cloud Engineer (ACE) Architectural Anchors
* **IAM & Resource Hierarchy:** Organization -> Folders -> Projects -> Resources. Principle of Least Privilege (PoLP).
* **Networking (VPC):** VPCs are global; subnets are regional. Internal IP communication within the same VPC is routable across regions without a VPN/gateway if firewalls permit.
* **Compute Engine:** Preemptible/Spot VMs for fault-tolerant workloads; Custom Machine Types for memory/CPU optimization.
* **Storage Spectrum:** 
  * Structured / Relational -> Cloud SQL (OLTP, max 64TB) or Cloud Spanner (Global/Multi-region, unlimited scale).
  * Unstructured -> Cloud Storage (Standard, Nearline, Coldline, Archive).
  * High-Throughput NoSQL -> Cloud Bigtable (Analytical/IoT) or Firestore (App state/documents).
* **Serverless & Containers:** Cloud Run for stateless HTTP containerized microservices; GKE for complex orchestration.

### 6. Workspace Directory Map
* `raw_materials/`: Archived source materials (8 original ILT PDFs and 4 Skills Boost HTML files).
* `modules/`: Converted lecture decks. Each module contains:
  * `M*_v2.md`: **Recommended photo-free study guide** with synthesized Mermaid architecture diagrams.
  * `M*.md`: Verbose version with extracted `.png` slide images and `media/` folder.
* `labs/`: Standardized Markdown lab manuals (`01` through `04`) and master `LAB_ROADMAP.md`.
* `study-notes/`: High-yield bridge notes (`Lab1_M0-M2_Study_Notes.md`, `Lab2_M3_Study_Notes.md`, `Lab3_M4_Study_Notes.md`) synthesized with Claude Web.
* `scripts/`: Conversion engines, Cloud Shell `.sh` scripts, and Claude Web prompt.
* `sessions/`: Milestone reviews, decision logs, and session activity tracking.
