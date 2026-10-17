import os
import re

MODULE_SPECS = [
    {
        "dir": "M0_Course_Introduction",
        "file": "M0_Course_Introduction.md",
        "v2_file": "M0_Course_Introduction_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 11: Today's\s+agenda)",
                "mermaid": """
```mermaid
flowchart TD
    M1["M1: Introducing Google Cloud<br/><i>Cloud models & global infra</i>"] --> M2["M2: Resources & Access<br/><i>Resource hierarchy & IAM</i>"]
    M2 --> M3["M3: VMs & Networks<br/><i>Compute Engine & VPC networking</i>"]
    M3 --> M4["M4: Storage in the Cloud<br/><i>Cloud Storage, SQL & Spanner</i>"]
    M4 --> M5["M5: Containers in the Cloud<br/><i>Docker, GKE & Artifact Registry</i>"]
    M5 --> M6["M6: Applications in the Cloud<br/><i>Cloud Run & serverless architectures</i>"]
    M6 --> M7["M7: Course Summary<br/><i>ACE preparation & next steps</i>"]

    style M1 fill:#e8f4f8,stroke:#007acc,color:#003b66
    style M2 fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style M3 fill:#eafaf1,stroke:#2ecc71,color:#145a32
    style M4 fill:#fef9e7,stroke:#f39c12,color:#7d4e00
    style M5 fill:#ebf5fb,stroke:#2980b9,color:#154360
    style M6 fill:#f5eef8,stroke:#8e44ad,color:#4a235a
    style M7 fill:#f2f3f4,stroke:#7f8c8d,color:#2c3e50
```
"""
            }
        ]
    },
    {
        "dir": "M1_Introducing_Google_Cloud",
        "file": "M1_Introducing_Google_Cloud.md",
        "v2_file": "M1_Introducing_Google_Cloud_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 4: What is Cloud Computing\?)",
                "mermaid": """
```mermaid
flowchart LR
    subgraph Colocation["1. Colocation / On-Prem"]
        C1["Customer owns hardware, OS & data center"]
    end
    subgraph IaaS["2. Infrastructure as a Service"]
        I1["Cloud provider owns physical hardware<br/>Customer configures OS, VM & software"]
    end
    subgraph PaaS["3. Platform as a Service"]
        P1["Provider owns OS, hardware & runtime<br/>Customer deploys application code"]
    end
    subgraph Serverless["4. Serverless & FaaS"]
        S1["Fully automated scaling & event execution<br/>Zero server management, pay-per-use"]
    end

    Colocation --> IaaS --> PaaS --> Serverless

    style Colocation fill:#f2f3f4,stroke:#7f8c8d,color:#2c3e50
    style IaaS fill:#e8f4f8,stroke:#007acc,color:#003b66
    style PaaS fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style Serverless fill:#eafaf1,stroke:#2ecc71,color:#145a32
```
"""
            },
            {
                "slide_pattern": r"(### Slide 27: Geographic locations contain regions and zones)",
                "mermaid": """
```mermaid
flowchart TB
    subgraph MultiRegion["Google Cloud Global Infrastructure"]
        subgraph RegionA["Region: us-central1 (Iowa)"]
            ZoneA1["Zone: us-central1-a<br/><i>Independent power, cooling & network</i>"]
            ZoneA2["Zone: us-central1-b<br/><i>Independent power, cooling & network</i>"]
            ZoneA3["Zone: us-central1-c<br/><i>Independent power, cooling & network</i>"]
        end
        subgraph RegionB["Region: europe-west1 (Belgium)"]
            ZoneB1["Zone: europe-west1-b"]
            ZoneB2["Zone: europe-west1-c"]
            ZoneB3["Zone: europe-west1-d"]
        end
        Edge["Google Edge Network / PoPs<br/><i>100+ Points of Presence worldwide</i>"]
    end

    Edge <--> RegionA
    Edge <--> RegionB

    style MultiRegion fill:#f8f9fa,stroke:#34495e,color:#2c3e50
    style RegionA fill:#e8f4f8,stroke:#007acc,color:#003b66
    style RegionB fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style Edge fill:#eafaf1,stroke:#2ecc71,color:#145a32
```
"""
            },
            {
                "slide_pattern": r"(### Slide 58: Google Compute products are billed per-second)",
                "mermaid": """
```mermaid
flowchart TD
    Start{"What is your compute workload model?"}
    Start -- "Need full OS control, custom kernels, or legacy apps" --> CE["Compute Engine (IaaS)<br/><i>Configurable VMs, disks & networking</i>"]
    Start -- "Containerized apps requiring granular cluster control" --> GKE["Google Kubernetes Engine (Hybrid/PaaS)<br/><i>Managed Kubernetes clusters & Pods</i>"]
    Start -- "Stateless HTTP containers with automatic scaling to 0" --> CR["Cloud Run (Serverless)<br/><i>Container runtime, pay-per-request</i>"]
    Start -- "Event-driven lightweight functions or glue logic" --> CF["Cloud Functions (FaaS)<br/><i>Single-purpose event handlers</i>"]
    Start -- "Web app framework without container management" --> GAE["App Engine (PaaS)<br/><i>Standard or Flexible environments</i>"]

    style Start fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style CE fill:#e8f4f8,stroke:#007acc,color:#003b66
    style GKE fill:#ebf5fb,stroke:#2980b9,color:#154360
    style CR fill:#eafaf1,stroke:#2ecc71,color:#145a32
    style CF fill:#f5eef8,stroke:#8e44ad,color:#4a235a
    style GAE fill:#fbeee6,stroke:#e67e22,color:#78281f
```
"""
            }
        ]
    },
    {
        "dir": "M2_Resources_and_Access",
        "file": "M2_Resources_and_Access.md",
        "v2_file": "M2_Resources_and_Access_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 4: Resources are hierarchical)",
                "mermaid": """
```mermaid
flowchart TD
    Org["Organization Node<br/><i>domain.com (Root of hierarchy)</i>"]
    FolderEng["Folder: Engineering"]
    FolderSales["Folder: Sales & Marketing"]
    ProjDev["Project: Dev-Environment<br/><i>Billing Account A · APIs enabled</i>"]
    ProjProd["Project: Prod-Environment<br/><i>Billing Account B · Quotas set</i>"]
    VM1["Compute Engine VM"]
    Bucket1["Cloud Storage Bucket"]
    DB1["Cloud SQL Database"]

    Org --> FolderEng
    Org --> FolderSales
    FolderEng --> ProjDev
    FolderEng --> ProjProd
    ProjDev --> VM1
    ProjProd --> Bucket1
    ProjProd --> DB1

    style Org fill:#d4efdf,stroke:#27ae60,color:#145a32
    style FolderEng fill:#d6eaf8,stroke:#2980b9,color:#154360
    style FolderSales fill:#d6eaf8,stroke:#2980b9,color:#154360
    style ProjDev fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style ProjProd fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style VM1 fill:#f2f4f4,stroke:#7f8c8d,color:#2c3e50
    style Bucket1 fill:#f2f4f4,stroke:#7f8c8d,color:#2c3e50
    style DB1 fill:#f2f4f4,stroke:#7f8c8d,color:#2c3e50
```
"""
            },
            {
                "slide_pattern": r"(### Slide 11: Folders facilitate policy\s+inheritance)",
                "mermaid": """
```mermaid
flowchart TD
    subgraph Inheritance["IAM Permissive Union Rule"]
        OrgPolicy["Organization Level: Bob has Viewer"]
        FolderPolicy["Folder Level: Bob has Editor"]
        ProjectPolicy["Project Level: Bob has Storage Admin"]
        ResourceEffective["Effective Permissions for Bob on Bucket:<br/><b>Viewer + Editor + Storage Admin (Union of all)</b>"]
    end

    OrgPolicy --> FolderPolicy --> ProjectPolicy --> ResourceEffective

    style OrgPolicy fill:#e8f4f8,stroke:#007acc,color:#003b66
    style FolderPolicy fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style ProjectPolicy fill:#ebf5fb,stroke:#2980b9,color:#154360
    style ResourceEffective fill:#eafaf1,stroke:#2ecc71,color:#145a32
```
"""
            },
            {
                "slide_pattern": r"(### Slide 16: Identity and Access Management applies policies)",
                "mermaid": """
```mermaid
flowchart LR
    subgraph Identity["Who (Identity / Member)"]
        U["Google Account (user@email.com)"]
        G["Google Group (dev-team@group)"]
        SA["Service Account (app-sa@project)"]
    end

    subgraph Role["Can Do What (Role)"]
        R1["Basic / Primitive (Viewer, Editor, Owner)"]
        R2["Predefined (roles/storage.objectViewer)"]
        R3["Custom (curated fine-grained permissions)"]
    end

    subgraph Resource["On Which Resource"]
        Res["Project / Bucket / Instance"]
    end

    Identity -- "bound via Policy to" --> Role
    Role -- "grants permissions on" --> Resource

    style Identity fill:#e8f4f8,stroke:#007acc,color:#003b66
    style Role fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style Resource fill:#eafaf1,stroke:#2ecc71,color:#145a32
```
"""
            }
        ]
    },
    {
        "dir": "M3_Virtual_Machines_and_Networks",
        "file": "M3_Virtual_Machines_and_Networks.md",
        "v2_file": "M3_Virtual_Machines_and_Networks_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 5: VPC subnets connect resources in different zones)",
                "mermaid": """
```mermaid
flowchart TB
    subgraph VPC["Global VPC Network: my-custom-vpc"]
        subgraph SubnetUS["Subnet US (us-central1): 10.128.0.0/20"]
            VM1["VM 1 (us-central1-a)<br/>Internal IP: 10.128.0.2"]
            VM2["VM 2 (us-central1-b)<br/>Internal IP: 10.128.0.3"]
        end
        subgraph SubnetEU["Subnet EU (europe-west1): 10.132.0.0/20"]
            VM3["VM 3 (europe-west1-b)<br/>Internal IP: 10.132.0.2"]
        end
    end

    VM1 <-->|"Internal Global Routing (Zero VPN needed)"| VM3
    VM1 <-->|"Internal Local Routing"| VM2

    style VPC fill:#f8f9fa,stroke:#34495e,color:#2c3e50
    style SubnetUS fill:#e8f4f8,stroke:#007acc,color:#003b66
    style SubnetEU fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style VM1 fill:#ffffff,stroke:#007acc,color:#000
    style VM2 fill:#ffffff,stroke:#007acc,color:#000
    style VM3 fill:#ffffff,stroke:#b58900,color:#000
```
"""
            },
            {
                "slide_pattern": r"(### Slide 17: VPCs also do not require a firewall to be provisioned)",
                "mermaid": """
```mermaid
flowchart LR
    Traffic["Incoming Traffic (Ingress)"] --> Priority{"Rule Priority (0 - 65535)<br/><i>Evaluated lowest number first</i>"}
    Priority -- Match found --> Action{"Action: Allow or Deny?"}
    Action -- Allow --> Target{"Target: All instances or Target Tag?"}
    Action -- Deny --> Drop["Traffic Dropped"]
    Target -- Tag Matches --> PortCheck{"Protocol & Port Match?<br/><i>e.g. tcp:80, tcp:22</i>"}
    Target -- Tag Does Not Match --> NextRule["Evaluate Next Priority Rule"]
    PortCheck -- Match --> AllowIngress["Traffic Allowed to VM"]
    PortCheck -- No Match --> NextRule

    style Traffic fill:#f2f3f4,stroke:#7f8c8d,color:#2c3e50
    style Priority fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style Action fill:#fbeee6,stroke:#e67e22,color:#78281f
    style AllowIngress fill:#eafaf1,stroke:#2ecc71,color:#145a32
    style Drop fill:#fadbd8,stroke:#c0392b,color:#78281f
```
"""
            }
        ]
    },
    {
        "dir": "M4_Storage_in_the_Cloud",
        "file": "M4_Storage_in_the_Cloud.md",
        "v2_file": "M4_Storage_in_the_Cloud_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 3: Google has many options for storing data)",
                "mermaid": """
```mermaid
flowchart TD
    StorageDecision{"What type of data are you storing?"}
    
    StorageDecision -- "Unstructured Objects (Images, videos, backups)" --> GCS["Cloud Storage (GCS)<br/><i>Standard, Nearline, Coldline, Archive</i>"]
    
    StorageDecision -- "Block Storage for VMs" --> PD["Persistent Disk / Hyperdisk<br/><i>Standard, SSD, Balanced, Extreme</i>"]
    
    StorageDecision -- "Relational SQL (ACID, transactions)" --> Relational{"Need global horizontal scale?"}
    Relational -- "No (Regional DB <= 64TB)" --> CloudSQL["Cloud SQL<br/><i>MySQL, PostgreSQL, SQL Server</i>"]
    Relational -- "Yes (Global multi-region, 99.999% SLA)" --> Spanner["Cloud Spanner<br/><i>Relational consistency with NoSQL scale</i>"]
    
    StorageDecision -- "NoSQL (Non-relational)" --> NoSQL{"Workload characteristic?"}
    NoSQL -- "High throughput, IoT, time-series, analytics (>1TB)" --> Bigtable["Cloud Bigtable<br/><i>HBase compatible, sub-10ms latency</i>"]
    NoSQL -- "Document/Hierarchical, mobile/web app state, ACID" --> Firestore["Firestore<br/><i>Real-time updates, offline support</i>"]
    
    StorageDecision -- "Analytical Data Warehouse" --> BQ["BigQuery<br/><i>Serverless petabyte-scale SQL analytics</i>"]

    style StorageDecision fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style GCS fill:#e8f4f8,stroke:#007acc,color:#003b66
    style PD fill:#f2f4f4,stroke:#7f8c8d,color:#2c3e50
    style CloudSQL fill:#ebf5fb,stroke:#2980b9,color:#154360
    style Spanner fill:#d4efdf,stroke:#27ae60,color:#145a32
    style Bigtable fill:#fbeee6,stroke:#e67e22,color:#78281f
    style Firestore fill:#fef9e7,stroke:#f39c12,color:#7d4e00
    style BQ fill:#f5eef8,stroke:#8e44ad,color:#4a235a
```
"""
            },
            {
                "slide_pattern": r"(### Slide 16: There are four basic Cloud Storage classes)",
                "mermaid": """
```mermaid
flowchart LR
    Standard["Standard Storage<br/><i>Frequent access<br/>Web content, streaming</i>"]
    -->|"30+ days without access"| Nearline["Nearline Storage<br/><i>Infrequent access (monthly)<br/>Data backups</i>"]
    -->|"90+ days without access"| Coldline["Coldline Storage<br/><i>Rare access (quarterly)<br/>Disaster recovery</i>"]
    -->|"365+ days without access"| Archive["Archive Storage<br/><i>Long-term archival (yearly)<br/>Regulatory compliance</i>"]

    style Standard fill:#d4efdf,stroke:#27ae60,color:#145a32
    style Nearline fill:#d6eaf8,stroke:#2980b9,color:#154360
    style Coldline fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
    style Archive fill:#f2f3f4,stroke:#7f8c8d,color:#2c3e50
```
"""
            }
        ]
    },
    {
        "dir": "M5_Containers_in_the_Cloud",
        "file": "M5_Containers_in_the_Cloud.md",
        "v2_file": "M5_Containers_in_the_Cloud_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 4: Containers group your code and its dependencies)",
                "mermaid": """
```mermaid
flowchart TD
    subgraph VMArchitecture["Virtual Machine Architecture"]
        AppVM1["App A"] --> BinVM1["Bins / Libs"] --> GuestOS1["Guest OS 1"]
        AppVM2["App B"] --> BinVM2["Bins / Libs"] --> GuestOS2["Guest OS 2"]
        GuestOS1 --> Hypervisor["Hypervisor"]
        GuestOS2 --> Hypervisor
        Hypervisor --> HostOSVM["Host OS / Hardware"]
    end

    subgraph ContainerArchitecture["Container Architecture (Lightweight)"]
        AppC1["App A"] --> BinC1["Bins / Libs"]
        AppC2["App B"] --> BinC2["Bins / Libs"]
        BinC1 --> ContainerEngine["Container Runtime (Docker / Containerd)"]
        BinC2 --> ContainerEngine
        ContainerEngine --> SharedKernel["Shared Host OS Kernel & Hardware"]
    end

    style VMArchitecture fill:#f8f9fa,stroke:#7f8c8d,color:#2c3e50
    style ContainerArchitecture fill:#e8f4f8,stroke:#007acc,color:#003b66
```
"""
            },
            {
                "slide_pattern": r"(### Slide 8: Kubernetes manages containerized workloads)",
                "mermaid": """
```mermaid
flowchart TB
    subgraph GKECluster["GKE Cluster"]
        subgraph ControlPlane["Control Plane (Google Managed)"]
            API["kube-apiserver"]
            ETCD["etcd storage"]
            Sched["kube-scheduler"]
            CM["kube-controller-manager"]
        end
        subgraph WorkerNodes["Worker Nodes (Compute Engine VMs)"]
            subgraph Node1["Node 1"]
                Pod1["Pod A (App Container)"]
                Pod2["Pod B (Helper Container)"]
                Kubelet1["kubelet + kube-proxy"]
            end
            subgraph Node2["Node 2"]
                Pod3["Pod A Replica"]
                Kubelet2["kubelet + kube-proxy"]
            end
        end
    end

    ControlPlane --> WorkerNodes

    style GKECluster fill:#f8f9fa,stroke:#34495e,color:#2c3e50
    style ControlPlane fill:#d4efdf,stroke:#27ae60,color:#145a32
    style WorkerNodes fill:#e8f4f8,stroke:#007acc,color:#003b66
    style Node1 fill:#ffffff,stroke:#2980b9,color:#000
    style Node2 fill:#ffffff,stroke:#2980b9,color:#000
```
"""
            }
        ]
    },
    {
        "dir": "M6_Applications_in_the_Cloud",
        "file": "M6_Applications_in_the_Cloud.md",
        "v2_file": "M6_Applications_in_the_Cloud_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 5: Cloud Run is managed serverless computing)",
                "mermaid": """
```mermaid
flowchart LR
    Dev["Developer"] -->|"git push / gcloud builds"| CloudBuild["Cloud Build"]
    CloudBuild -->|"docker push"| AR["Artifact Registry<br/><i>Container Image</i>"]
    AR -->|"deploy"| CloudRun["Cloud Run Service<br/><i>Fully Managed Knative Runtime</i>"]
    
    Requests["Client HTTPS Traffic"] --> Ingress["Google Cloud HTTPS Load Balancer"]
    Ingress --> CloudRun
    
    subgraph AutoScaling["Auto-Scaling Container Instances"]
        CloudRun --> C1["Instance 1 (active)"]
        CloudRun --> C2["Instance 2 (auto-spawned)"]
        CloudRun -.->|"Idle traffic -> scale to 0"| C0["Zero instances ($0 cost)"]
    end

    style Dev fill:#f2f3f4,stroke:#7f8c8d,color:#2c3e50
    style CloudBuild fill:#e8f4f8,stroke:#007acc,color:#003b66
    style AR fill:#fdf6e2,stroke:#b58900,color:#5b4300
    style CloudRun fill:#eafaf1,stroke:#2ecc71,color:#145a32
    style AutoScaling fill:#fcf3cf,stroke:#f39c12,color:#7d4e00
```
"""
            }
        ]
    },
    {
        "dir": "M7_Course_Summary",
        "file": "M7_Course_Summary.md",
        "v2_file": "M7_Course_Summary_v2.md",
        "diagrams": [
            {
                "slide_pattern": r"(### Slide 9: What's next for Cloud Engineer\?)",
                "mermaid": """
```mermaid
mindmap
  root((Google Cloud Fundamentals))
    Compute & Containers
      Compute Engine IaaS
      Google Kubernetes Engine
      Cloud Run Serverless
      Cloud Functions FaaS
    Networking
      Global VPC Networks
      Regional Subnets
      Firewall Rules & Tags
      Cloud Load Balancing
    Storage & Data
      Cloud Storage Buckets
      Cloud SQL MySQL/Postgres
      Cloud Spanner Global
      BigQuery Analytics
    Security & IAM
      Resource Hierarchy
      IAM Policies & Roles
      Service Accounts
      Least Privilege Principle
```
"""
            }
        ]
    }
]

def process_module(spec):
    in_path = os.path.join("modules", spec["dir"], spec["file"])
    out_path = os.path.join("modules", spec["dir"], spec["v2_file"])
    
    print(f"Processing v2: {in_path} -> {out_path}")
    if not os.path.exists(in_path):
        print(f"ERROR: {in_path} does not exist.")
        return

    with open(in_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update doc banner
    content = content.replace(
        "DTCM-v3 High-Fidelity Architecture (`ptcm-pdf-v1`)",
        "DTCM-v3 Clean Architecture (No-Photo / Mermaid Edition)"
    )

    # 2. Remove "List of Figures" section completely from Table of Contents / Header
    content = re.sub(r"## List of Figures\n+.*?(?=\n---\n|\Z)", "", content, flags=re.DOTALL)

    # 3. Strip all image markdown references: ![caption](media/xxx.png)
    content = re.sub(r"!\[.*?\]\(media/.*?\)\n*", "", content)

    # 4. Strip all Figure captions: **Figure N:** ...
    content = re.sub(r"\*\*Figure \d+:\*\*.*?\n*", "", content)

    # 5. Inject Mermaid diagrams at specified slide positions
    for diag in spec["diagrams"]:
        pattern = diag["slide_pattern"]
        mmd_block = diag["mermaid"]
        if re.search(pattern, content):
            # Inject right after the slide header
            content = re.sub(pattern, r"\1\n" + mmd_block, content, count=1)
            print(f"  [INJECTED] Diagram for pattern: {pattern}")
        else:
            print(f"  [WARNING] Pattern '{pattern}' not matched in {spec['file']}")

    # 6. Clean up excessive consecutive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    with open(out_path, "w", encoding="utf-8") as f_out:
        f_out.write(content)

    print(f"Successfully generated: {out_path}\n")


def main():
    for spec in MODULE_SPECS:
        process_module(spec)
    print("[SUCCESS] Generated all 8 photo-free Mermaid v2 Markdown files.")

if __name__ == "__main__":
    main()
