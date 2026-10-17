# Lab 1 Study Notes: M0 to M2

### Cloud basics, Google's infrastructure, and resources and access, condensed for Lab 1 and the ACE exam

> **As of:** 2026-10-17 · **Sources:** the M0, M1 and M2 `_v2.md` study guides in [modules/](../modules/) · **Synced with:** the Claude Doc of the same name, https://claude.ai/code/artifact/97e12c9e-19a1-46c4-aebb-2633255c7281

---

## Table of Contents

- [PART 0 — Course introduction (M0)](#part-0)
- [Google Cloud ↔ AWS cheat sheet](#part-aws)
- [PART 1 — Introducing Google Cloud (M1)](#part-1)
  - [1.1 Cloud computing: the 5 traits](#part-1-1)
  - [1.2 Service models](#part-1-2)
  - [1.3 Global infrastructure](#part-1-3)
  - [1.4 Security: defense in depth](#part-1-4)
  - [1.5 Open APIs and open source](#part-1-5)
  - [1.6 Pricing and billing](#part-1-6)
  - [1.7 M1 self-check quiz](#part-1-7)
- [PART 2 — Resources and Access (M2)](#part-2)
  - [2.1 Resource hierarchy](#part-2-1)
  - [2.2 Projects](#part-2-2)
  - [2.3 Identity and Access Management (IAM)](#part-2-3)
  - [2.4 The three kinds of IAM roles](#part-2-4)
  - [2.5 Service accounts](#part-2-5)
  - [2.6 Cloud Identity](#part-2-6)
  - [2.7 Four ways to work with Google Cloud](#part-2-7)
  - [2.8 M2 self-check quiz](#part-2-8)
- [PART 3 — Bridge to Lab 1: Cloud Marketplace LAMP](#part-3)
- [PART 4 — Grill log: questions, slips and fixes](#part-4)
  - [4.1 Deep dives on the slips](#part-4-1)
  - [4.2 The questions, round by round](#part-4-2)

---

<a id="part-0"></a>
## PART 0 — Course introduction (M0)

> [!IMPORTANT]
> A lab gives you a temporary project and student account for a fixed time, and **it cannot be paused**. Start a lab only when you have a continuous block of time.

Everything below keeps what Lab 1 or the Associate Cloud Engineer (ACE) exam needs. Cut: etiquette and agenda slides, repeated section dividers, product history detail, sustainability marketing, TensorFlow, and the mobile app's feature list.

---

<a id="part-aws"></a>
## Google Cloud ↔ AWS cheat sheet

If you know AWS, map each Google Cloud name to the service you already know.

| Google Cloud | AWS equivalent | Note |
| :--- | :--- | :--- |
| **Organization node** | AWS Organizations (root) | Top of the hierarchy |
| **Folder** | Organizational Unit (OU) | Groups projects / accounts |
| **Project** | AWS account | Closest match; in GCP each service's API must be enabled per project |
| **IAM** | IAM | GCP grants roles on a resource-hierarchy level; AWS attaches policies to identities |
| **Service account** | IAM role for EC2 (instance profile) | Identity for software, not people |
| **Cloud Identity** | IAM Identity Center | Central users and groups |
| **Compute Engine** | EC2 | IaaS VMs, per-second billing |
| **App Engine** | Elastic Beanstalk | PaaS: deploy code, platform runs it |
| **Cloud Run** | App Runner / ECS on Fargate | Serverless containers (Lab 4) |
| **Cloud Run functions** | Lambda | Event-driven functions |
| **GKE** | EKS | Managed Kubernetes |
| **Cloud Storage** | S3 | Object storage (Lab 3) |
| **Cloud SQL** | RDS | Managed MySQL / PostgreSQL / SQL Server (Lab 3) |
| **BigQuery** | Redshift / Athena | Analytics warehouse |
| **Dataproc** | EMR | Managed Spark / Hadoop |
| **VPC network** | VPC | GCP VPC is **global** with regional subnets; AWS VPC is regional (Lab 2) |
| **Firewall rules** | Security groups / NACLs | Lab 1 and 2 |
| **Cloud Marketplace** | AWS Marketplace | Lab 1 |
| **Artifact Registry** | ECR | Lab 4 |
| **Cloud Build** | CodeBuild | Lab 4 |
| **Cloud Shell / gcloud** | CloudShell / AWS CLI | |
| **Budgets, quotas** | AWS Budgets, Service Quotas | |
| **Cloud Monitoring / Logging** | CloudWatch | |

> **Key Idea:** The biggest mindset change from AWS: in Google Cloud the **project** is the unit for billing, API enablement and IAM, and a **VPC is global**.

---

<a id="part-1"></a>
## PART 1 — Introducing Google Cloud (M1)

<a id="part-1-1"></a>
### 1.1 Cloud computing: the 5 traits
#### "The NIST definition: what makes something cloud"

NIST is the US National Institute of Standards and Technology; its definition is the standard one, and nothing in it is US-specific.

| # | Trait | What it means |
| :---: | :--- | :--- |
| 1 | **On-demand self-service** | Compute, storage and network through a web interface, with no human in the loop |
| 2 | **Broad network access** | Over the internet, from anywhere |
| 3 | **Resource pooling** | Provider allocates from a big shared pool, buys in bulk, passes savings on; you don't care where the hardware is |
| 4 | **Rapid elasticity** | Scale up or down quickly |
| 5 | **Measured service** | Pay only for what you use, or reserve; stop using and you stop paying |

How we got here:

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    A["1st wave: Colocation<br/>rent rack space"] --> B["2nd wave: Virtualized data centers<br/>virtual servers, you still maintain them"]
    B --> C["3rd wave: Google<br/>container-based, automated, elastic"]
    style A fill:#2d3436,stroke:#6c5ce7,color:#ffffff
    style B fill:#16213e,stroke:#0f3460,color:#ffffff
    style C fill:#2d3436,stroke:#00b894,color:#ffffff
```

<a id="part-1-2"></a>
### 1.2 Service models

| Model | You manage | Provider manages | Google example | You pay for |
| :--- | :--- | :--- | :--- | :--- |
| **IaaS** | OS, runtime, app | Hardware, network, virtualization | Compute Engine | Resources you allocate |
| **PaaS** | App code (bound to provided libraries) | OS, runtime, infrastructure | App Engine | Resources you use |
| **Serverless** | Code or container only | Everything else, including scaling | Cloud Run, Cloud Run functions | Per request or event |
| **SaaS** | Nothing, you just use it | Everything | Gmail, Docs, Drive (Google Workspace) | Subscription |

> **Key Idea:** The trend is toward managed services: less time on infrastructure, more on the product.

<a id="part-1-3"></a>
### 1.3 Global infrastructure

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TD
    L["Location<br/>e.g. North America"] --> R1["Region<br/>e.g. us-central1"]
    L --> R2["Region<br/>e.g. us-east1"]
    R1 --> Z1["Zone us-central1-a<br/>VMs are deployed here"]
    R1 --> Z2["Zone us-central1-b"]
    R1 --> Z3["Zone us-central1-c"]
    style L fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style R1 fill:#16213e,stroke:#0f3460,color:#ffffff
    style R2 fill:#16213e,stroke:#0f3460,color:#ffffff
    style Z1 fill:#2d3436,stroke:#00b894,color:#ffffff
    style Z2 fill:#2d3436,stroke:#00b894,color:#ffffff
    style Z3 fill:#2d3436,stroke:#00b894,color:#ffffff
```

- **Location → Region → Zone.** A zone is where resources such as a VM are actually deployed. A region holds several zones.
- Some services run **multi-region** (for example Cloud Storage `US`, `EU`, `ASIA`, used in Lab 3).
- 100+ edge caching nodes serve popular content from the nearest location to cut latency (the time a packet takes from source to destination).
- Live counts of regions and zones: cloud.google.com/about/locations.

| Spread across | What you gain |
| :--- | :--- |
| **Several zones in one region** | Fault tolerance |
| **Several regions** | Closer to users worldwide, and you survive a whole-region outage |

<a id="part-1-4"></a>
### 1.4 Security: defense in depth, layer by layer

| Layer | What Google does |
| :--- | :--- |
| **Hardware infrastructure** | Custom-designed server boards, network gear and a hardware security chip; secure boot stack (signed BIOS, bootloader, kernel, OS image); layered physical premises security |
| **Service deployment** | RPC traffic between data centers is encrypted |
| **User identity** | Login page challenges on risk signals (new device or location); second factor with U2F security keys |
| **Storage services** | **Encryption at rest by default**, with centrally managed keys; hardware encryption on drives and SSDs |
| **Internet communication** | Google Front End (GFE) terminates TLS with proper certificates and perfect forward secrecy; multi-layer DoS protection |
| **Operational security** | Intrusion detection and Red Team exercises; limited and monitored admin access; U2F keys for all employees; central source control with two-party code review; bug bounty |

**Analogy:** a bank doesn't rely on one wall. It has guards at the door, ID checks, a vault and cameras, so getting past one layer still leaves the others.

**Worked example:** you open your Lab 3 blog, which shows an image stored in Cloud Storage. The request meets every layer:

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    U["You<br/>browser"] --> G["1. Internet communication<br/>GFE: TLS + DoS absorbed"]
    G --> I["2. User identity<br/>risk checks, security key"]
    I --> S["3. Service deployment<br/>encrypted RPC between services"]
    S --> D["4. Storage services<br/>image encrypted at rest"]
    D --> H["5. Hardware<br/>secure boot, guarded building"]
    H -.-> O["6. Operational security<br/>monitored staff, two-person code review"]
    style U fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style G fill:#16213e,stroke:#0f3460,color:#ffffff
    style I fill:#16213e,stroke:#0f3460,color:#ffffff
    style S fill:#16213e,stroke:#0f3460,color:#ffffff
    style D fill:#0f3460,stroke:#533483,color:#ffffff
    style H fill:#2d3436,stroke:#6c5ce7,color:#ffffff
    style O fill:#2d3436,stroke:#6c5ce7,color:#ffffff
```

1. **Internet communication:** your browser reaches the Google Front End first; it handles HTTPS and soaks up DoS floods before anything reaches the app.
2. **User identity:** signing in to the console, Google checks risk signals (new device or country) and can ask for a second factor such as a security key.
3. **Service deployment:** as Google's services pass your request between data centers, that internal RPC traffic is encrypted.
4. **Storage services:** the image sits on disk encrypted at rest by default, with nothing for you to turn on.
5. **Hardware:** the server runs Google-designed chips and a secure boot stack, so tampered software won't boot; the building has layered physical security.
6. **Operational security:** staff who could touch that server have limited, monitored access and use security keys; changes to its code need two-person review.

> [!IMPORTANT]
> **What the ACE exam tests here:**
> - Encryption at rest and in transit is **on by default**. An answer like "enable encryption on the bucket" as an extra step is usually a trap.
> - **Shared responsibility:** Google secures these six layers; you secure yours: IAM roles, firewall rules, patching your VM's OS, and keys if you choose to manage them.
> - You won't be asked to recite the six layers in order; know that each exists.

<a id="part-1-5"></a>
### 1.5 Open APIs and open source

Google publishes key technology as open source so you are not locked in. Kubernetes and GKE let you mix microservices across clouds, and Google Cloud Observability monitors workloads across multiple providers.

<a id="part-1-6"></a>
### 1.6 Pricing and billing

| Feature | What it does |
| :--- | :--- |
| **Per-second billing** | Compute Engine, GKE, Managed Service for Apache Spark (Dataproc), App Engine flexible environment |
| **Sustained use discounts** | Applied automatically when a VM runs more than 25% of the month, for every extra minute |
| **Custom machine types** | Choose the exact vCPU and memory, so you pay only for what the workload needs |
| **Pricing calculator** | Estimate costs: cloud.google.com/products/calculator |

Tools to avoid surprise bills:

1. **Budgets** at billing-account or project level, fixed or tied to a metric such as a % of last month's spend.
2. **Alerts** when spend nears the budget, typically at 50%, 90% and 100%.
3. **Reports** in the console, by project or service.
4. **Quotas**, which cap consumption to stop errors or attacks from running away.

> [!IMPORTANT]
> A budget alerts you; it does not stop spending.

Quotas apply **per project** and come in two types:

| Quota type | Behaviour | Example |
| :--- | :--- | :--- |
| **Rate quota** | Resets after a time window | GKE API, 3,000 calls per project every 100 seconds |
| **Allocation quota** | Caps how many resources you can have | 15 VPC networks per project |

Some quotas can be raised by requesting an increase from Google Cloud.

<a id="part-1-7"></a>
### 1.7 M1 self-check quiz

<details>
<summary><strong>Q1.</strong> Why use resources in several zones within one region?</summary>

Fault tolerance.

</details>

<details>
<summary><strong>Q2.</strong> Which service model binds your code to libraries that give access to the infrastructure it needs?</summary>

PaaS.

</details>

<details>
<summary><strong>Q3.</strong> Why use resources in several regions?</summary>

Closer to users around the world, and protection against a whole-region failure.

</details>

<details>
<summary><strong>Q4.</strong> Name the 5 traits of cloud computing.</summary>

On-demand self-service, broad network access, resource pooling, rapid elasticity, measured service.

</details>

<details>
<summary><strong>Q5.</strong> In IaaS do you pay for resources allocated or resources used? And in PaaS?</summary>

IaaS: allocated. PaaS: used.

</details>

<details>
<summary><strong>Q6.</strong> A VM runs all month. What discount do you get without doing anything?</summary>

A sustained use discount (it applies past 25% of the month).

</details>

<details>
<summary><strong>Q7.</strong> What is the difference between a rate quota and an allocation quota? At what level do both apply?</summary>

A rate quota resets after a time window; an allocation quota caps a count of resources. Both are per project.

</details>

<details>
<summary><strong>Q8.</strong> Your budget is &#36;1,000 with an alert at 90%. What happens when spend reaches &#36;900, and what happens at &#36;1,100?</summary>

At \$900 you get an alert. At \$1,100 you get another alert if one is set at 100%, but nothing stops: budgets don't cap spend.

</details>

<details>
<summary><strong>Q9.</strong> Which layer of Google's security model covers encryption at rest?</summary>

Storage services.

</details>

---

<a id="part-2"></a>
## PART 2 — Resources and Access (M2)

<a id="part-2-1"></a>
### 2.1 Resource hierarchy
#### "Four levels, and policies flow downward"

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TD
    O["Organization node<br/>via Workspace or Cloud Identity"] --> F1["Folder: Engineering"]
    O --> F2["Folder: Sales"]
    F1 --> P1["Project: dev"]
    F1 --> P2["Project: prod"]
    P1 --> R1["Resource: VM"]
    P2 --> R2["Resource: bucket"]
    P2 --> R3["Resource: Cloud SQL"]
    style O fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style F1 fill:#16213e,stroke:#0f3460,color:#ffffff
    style F2 fill:#16213e,stroke:#0f3460,color:#ffffff
    style P1 fill:#2d3436,stroke:#6c5ce7,color:#ffffff
    style P2 fill:#2d3436,stroke:#6c5ce7,color:#ffffff
    style R1 fill:#0f3460,stroke:#533483,color:#ffffff
    style R2 fill:#0f3460,stroke:#533483,color:#ffffff
    style R3 fill:#0f3460,stroke:#533483,color:#ffffff
```

| Level | What it is |
| :--- | :--- |
| **Resources** | VMs, buckets, VPC networks, BigQuery tables, anything you create |
| **Projects** | Every resource belongs to exactly one project |
| **Folders** | Group projects (for example per department) and can nest; they let teams delegate admin rights. Folders need an organization node |
| **Organization node** | The top. You get one through Google Workspace or Cloud Identity. A new org node still lets everyone in the domain create projects and billing accounts, to avoid disruption. Special roles live here, such as **Organization Policy Administrator** and **Project Creator** (controls who can create projects and so spend money) |

> **Key Idea:** Policies can be set at the organization, folder and project levels (and on some individual resources) and are **inherited downward**. Effective access on a resource is the **union** of everything granted at and above it. Example: Viewer at org + Editor at folder + Storage Admin at project = all three on a bucket in that project.

<a id="part-2-2"></a>
### 2.2 Projects

The project is where you **enable APIs and services**, link billing, and add or remove collaborators. Projects are billed and managed separately.

| Attribute | Globally unique? | Set by | Changeable? |
| :--- | :--- | :--- | :--- |
| **Project ID** | Yes | You at creation (Google suggests one) | **No, immutable after creation** |
| **Project name** | No | You | Yes, any time |
| **Project number** | Yes | Google | No |

- The project ID is what you pass to tools to say which project to work on (Cloud Shell's `$DEVSHELL_PROJECT_ID`, `gcloud config set project`).
- **Resource Manager** is the API to list, create, update, delete and recover projects (RPC and REST).

<a id="part-2-3"></a>
### 2.3 Identity and Access Management (IAM)
#### "Who can do what on which resource"

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    W["Who: principal<br/>Google account, group,<br/>service account, Cloud Identity domain"] -->|granted| R["What: role<br/>a bundle of permissions"]
    R -->|on| X["Which resource<br/>org, folder, project or resource,<br/>and everything below it"]
    style W fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style R fill:#16213e,stroke:#0f3460,color:#ffffff
    style X fill:#0f3460,stroke:#533483,color:#ffffff
```

- **Who (principal):** a Google account, a Google group, a service account, or a Cloud Identity domain, each identified by an email address.
- **What (role):** a collection of permissions. Granting a role grants all its permissions.
- **Which resource:** the level of the hierarchy where you grant it; it applies there and to everything below.

> [!IMPORTANT]
> **Deny policies** block specific permissions whatever roles say. IAM checks deny before allow, and deny policies are inherited too.

<a id="part-2-4"></a>
### 2.4 The three kinds of IAM roles (broadest to finest)

| Kind | What it is | Example | Notes |
| :--- | :--- | :--- | :--- |
| **Basic** | Owner, Editor, Viewer; apply to every resource in the project | Viewer: look. Editor: look and change. Owner: also manage roles and set up billing | Too broad when several people share a project with sensitive data |
| **Predefined** | Curated per service | `roles/compute.instanceAdmin` on a project, folder or organization | Matches typical job needs |
| **Custom** | Your own permission set, for least privilege | "instanceOperator": start and stop VMs, not reconfigure them | Project or organization level only, **never folder** |

A project-level custom role can't include org- or folder-only permissions such as `resourcemanager.organizations.get`.

> [!NOTE]
> Billing without resource access is a separate role, Billing Account Administrator. The slides list a "billing administrator" next to the basic roles; on the exam the basic roles are Owner, Editor and Viewer.

<a id="part-2-5"></a>
### 2.5 Service accounts
#### "An identity for software, not a person"

**The problem it solves:** an app on a VM needs to call other services regularly, and nobody should have to grant access by hand each time.

**What a service account does:**
- Acts as an identity for an application or VM, so it can call other services without a human.
- Is named with an email address, and authenticates with **cryptographic keys instead of a password**.
- Gets roles like any principal. Example: a VM whose service account has Instance Admin can create, modify and delete other VMs.

**Analogy:** a staff badge issued to a machine instead of a person.

> **Key Idea:** A service account is also a **resource**, so people get roles on it: Alice can be Editor of the service account, Bob only Viewer.

<a id="part-2-6"></a>
### 2.6 Cloud Identity

- Manages users and groups centrally in the Google Admin console instead of loose Gmail accounts and groups.
- Lets admins use existing Active Directory or LDAP usernames and passwords.
- When someone leaves, disable the account and remove them from groups in one place.
- Free edition, and a premium edition that adds mobile device management. Google Workspace customers already have it.

<a id="part-2-7"></a>
### 2.7 Four ways to work with Google Cloud

| Way | What it gives you |
| :--- | :--- |
| **Google Cloud console** | Web GUI to deploy, scale and diagnose; search resources; SSH to VMs in the browser; set budgets |
| **Google Cloud SDK and Cloud Shell** | SDK includes the `gcloud` CLI and tools like `bq` for BigQuery. **Cloud Shell** is a browser terminal: Debian-based, **5 GB persistent home directory**, pre-authenticated, SDK preinstalled. This is where you run lab commands |
| **APIs** | Every service has one; the APIs Explorer lets you try them; client libraries for Java, Python, PHP, C#, Go, Node.js, Ruby and C++ |
| **Google Cloud app (mobile)** | Start, stop and SSH to VMs, start and stop Cloud SQL, see billing alerts and key metrics |

<a id="part-2-8"></a>
### 2.8 M2 self-check quiz

<details>
<summary><strong>Q1.</strong> Services and APIs are enabled on a per-what basis?</summary>

Per project.

</details>

<details>
<summary><strong>Q2.</strong> Order the IAM role types from broadest to finest-grained.</summary>

Basic, predefined, custom.

</details>

<details>
<summary><strong>Q3.</strong> Which value is globally unique and unchangeable after creation, but chosen by you during creation?</summary>

The project ID.

</details>

<details>
<summary><strong>Q4.</strong> Name the four levels of the resource hierarchy from the top.</summary>

Organization node, folders, projects, resources.

</details>

<details>
<summary><strong>Q5.</strong> Bob has Viewer on the organization and Editor on a folder. What can he do on a project inside that folder?</summary>

Edit: he gets the union of Viewer and Editor, inherited down to the project.

</details>

<details>
<summary><strong>Q6.</strong> Bob has an allow policy granting Editor, and a deny policy denying <code>compute.instances.delete</code>. Can he delete a VM?</summary>

No. Deny policies are checked first and win.

</details>

<details>
<summary><strong>Q7.</strong> At which levels can you create a custom role, and where can't you?</summary>

Project or organization level. Never at folder level.

</details>

<details>
<summary><strong>Q8.</strong> How does a service account authenticate, and why can it also have IAM policies attached to it?</summary>

With cryptographic keys, not a password. It is also a resource, so people can be granted roles to use or manage it.

</details>

<details>
<summary><strong>Q9.</strong> An employee leaves. Which tool lets an admin remove their access in one place?</summary>

Cloud Identity, through the Google Admin console.

</details>

<details>
<summary><strong>Q10.</strong> Name Cloud Shell's two key properties for running lab commands.</summary>

Pre-authenticated with the SDK preinstalled, and a persistent 5 GB home directory.

</details>

---

<a id="part-3"></a>
## PART 3 — Bridge to Lab 1: Cloud Marketplace LAMP

| In the lab you... | The theory behind it |
| :--- | :--- |
| Deploy from **Marketplace** with Click to Deploy | Pre-packaged solution that builds a **Compute Engine VM** (IaaS) running Linux, Apache, MySQL and PHP |
| Pick a **zone** and machine type (`e2-medium`) | The zone decides where the VM lives |
| **Enable the Compute Engine API** when asked | APIs are enabled **per project** |
| See `qwiklabs-gcp-...` in the console | That is the globally unique project ID |
| Sign in as a student account | That account holds an IAM role on the project |
| Open the Site URL | A **firewall rule allows HTTP (tcp:80)** to the VM's external IP |

> **Key Idea:** Patching the VM's OS and software is your job, not Google's: that is the IaaS side of shared responsibility.

---

<a id="part-4"></a>
## PART 4 — Grill log: questions, slips and fixes

Four grill rounds on 2026-10-17. Part 4.1 expands the concepts behind the slips; 4.2 lists every question with its answer, so you can re-quiz yourself one dropdown at a time.

<a id="part-4-1"></a>
### 4.1 Deep dives on the slips

#### Bob is Owner, but an org-level deny exists. How does he delete a VM?

**He can't.** Console, `gcloud` and the API all check the same permission, `compute.instances.delete`, so every route is blocked.

```mermaid
%%{init: {'theme':'base'}}%%
flowchart TD
    R["Request: Bob deletes a VM"] --> D{"Does any deny policy from the org,<br/>folder, project or resource match<br/>Bob and this permission?"}
    D -->|"yes"| X["DENIED<br/>allow policies are never checked"]
    D -->|"no"| A{"Does the union of Bob's allow grants<br/>include the permission?"}
    A -->|"yes"| OK["ALLOWED"]
    A -->|"no"| N["DENIED<br/>nothing grants it"]
    style R fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style D fill:#16213e,stroke:#0f3460,color:#ffffff
    style A fill:#16213e,stroke:#0f3460,color:#ffffff
    style X fill:#2d3436,stroke:#e94560,color:#ffffff
    style N fill:#2d3436,stroke:#e94560,color:#ffffff
    style OK fill:#2d3436,stroke:#00b894,color:#ffffff
```

- **Why Owner doesn't help:** Owner is an *allow* grant on the project. IAM evaluates deny policies first, and a deny set on the org is inherited by everything below it. A project Owner has no power over the org's deny policy.
- **What would make the delete possible** (all done by someone with the right at the org level, not by Bob):
    1. A person with the **Deny Admin** role on the org removes the deny policy.
    2. The deny policy is edited to list Bob, or a break-glass group, as an **exception principal**: the deny then applies to everyone except them.
    3. The deny is narrowed with a condition so it only covers some resources.
- **AWS version:** an Organizations SCP deny beats any Allow, even for an account admin. Only someone in the management account can change the SCP.

> **Key Idea:** Owner plus a deny equals denied. Deny policies win over allow and are inherited down the hierarchy.

#### Why does the Lab 1 site open? Firewall rules in detail

A VM can have an external IP and still be unreachable, because a VPC firewall sits in front of it.

- Every VPC has two **implied rules**: *deny all ingress* and *allow all egress*. They have the lowest priority and can't be deleted.
- Anything else you must allow with a rule. A rule has a **direction** (ingress or egress), a **priority** (a lower number wins), an **action** (allow or deny), a **target** (all instances, a network tag, or a service account), a **source** (IP ranges) and a **protocol and port**.
- Rules are **stateful**: if a request is allowed in, the reply is allowed out automatically.
- **AWS version:** closest to security groups plus NACLs in one: a rule can allow or deny, is set at VPC level, and picks its VMs with tags. Lab 2 builds these by hand.

```mermaid
%%{init: {'theme':'base'}}%%
flowchart LR
    B["Your browser"] -->|"http to the VM's external IP, port 80"| F{"VPC firewall:<br/>does an ingress rule allow tcp:80?"}
    F -->|"no rule"| T["Dropped silently<br/>browser times out"]
    F -->|"allowed"| V["VM"]
    V --> P{"Is Apache listening<br/>on port 80?"}
    P -->|"no"| RF["Connection refused"]
    P -->|"yes"| S["Page served"]
    style B fill:#1a1a2e,stroke:#e94560,color:#ffffff
    style F fill:#16213e,stroke:#0f3460,color:#ffffff
    style V fill:#0f3460,stroke:#533483,color:#ffffff
    style P fill:#16213e,stroke:#0f3460,color:#ffffff
    style T fill:#2d3436,stroke:#e94560,color:#ffffff
    style RF fill:#2d3436,stroke:#e94560,color:#ffffff
    style S fill:#2d3436,stroke:#00b894,color:#ffffff
```

- **Both must be true** for the page to load: the firewall allows port 80, and something is listening on port 80.
- **Debugging rule:** a **timeout** points to the firewall; **connection refused** means the traffic got through but nothing is listening.
- **In Lab 1:** the Marketplace deploy form has a firewall section, and its defaults should leave HTTP traffic allowed (check it on the deploy page; the exact rule name may differ). The lab's exam anchor is to *verify the allow-http rule on port 80*. If the page won't open from a corporate laptop, try off the VPN or another device, as the lab says.
- **Check it yourself** in Cloud Shell: `gcloud compute firewall-rules list`

#### App Engine, Compute Engine and Cloud Run functions side by side

| | Compute Engine (≈ EC2) | App Engine (≈ Elastic Beanstalk) | Cloud Run functions (≈ Lambda) |
| :--- | :--- | :--- | :--- |
| **Model** | IaaS | PaaS | Serverless functions |
| **You deploy** | A VM you configure | Your app code plus an `app.yaml` | One function |
| **You manage** | OS, runtime, scaling, patches | Only the app | Only the function |
| **Scaling** | You set it up | Automatic; the standard environment can scale to zero | Automatic, per event |
| **You pay for** | Resources allocated, per second | Resources used | Per invocation |

Example, a small Python Flask blog: on Compute Engine you build the VM, install Python and a web server, deploy and patch it; on App Engine you run `gcloud app deploy` and Google provisions, scales and patches the servers; with Cloud Run functions you deploy single handlers that run only when a request or event arrives.

#### Why enabling an API happens per project

Every service's API starts **off in each new project**. Lab 1's prompt to enable the Compute Engine API turns it on for that one project only, not for the folder or org above it, or for other projects. AWS has no real equivalent: think of a project as an AWS account where you tick the services you want before using them.

#### Where custom roles are created and where roles are granted

| | Where |
| :--- | :--- |
| **Create (define) a custom role** | Organization or project only, never a folder |
| **Grant any role** | Organization, folder, project or a single resource |

To give every project under the Engineering folder a "vmOperator" role: create it on the **organization**, then grant it on the **folder**, and it flows down.

<a id="part-4-2"></a>
### 4.2 The questions, round by round

<details>
<summary><strong>R1 Q1.</strong> You deploy one VM in one zone and that zone goes down. What should you have done, and what changes if a whole region goes down?</summary>

Spread VMs across several zones of the region, so one zone failing leaves the others running. For a whole-region failure, also run in several regions. Several VMs in the same zone fail together.

</details>

<details>
<summary><strong>R1 Q2.</strong> Compute Engine and App Engine: which is IaaS and which is PaaS, and how does each bill?</summary>

Compute Engine is IaaS (≈ EC2): you pay for what you allocate, per second. App Engine is PaaS (≈ Elastic Beanstalk): you pay for what you use. The Lambda equivalent is Cloud Run functions.

</details>

<details>
<summary><strong>R1 Q3.</strong> Bob has Viewer on the org, Editor on a folder, and a deny on <code>compute.instances.delete</code>. What can he do to a VM in a project inside that folder?</summary>

Everything Editor allows except delete: his grants are the union of Viewer and Editor, and the deny wins on delete. Outside that folder he only inherits the org grant, so he is just a Viewer there.

</details>

<details>
<summary><strong>R1 Q4.</strong> Lab 1 asks you to enable the Compute Engine API. Why, and at which level does it apply?</summary>

Every service's API starts off in each new project. Enabling it applies to that one project only.

</details>

<details>
<summary><strong>R2 Q1.</strong> The project is named "blog-test" and its ID is <code>blog-test-48213</code>. Which can you rename, and which do gcloud commands use?</summary>

You can rename the name; the ID is fixed forever. gcloud uses the ID: `gcloud config set project blog-test-48213`. The ID is like an S3 bucket name: globally unique and unchangeable.

</details>

<details>
<summary><strong>R2 Q2.</strong> An app on a VM must write files to a bucket with no person logging in. What identity should it use?</summary>

A service account attached to the VM (≈ an IAM role on an EC2 instance profile), authenticating with keys, not a password.

</details>

<details>
<summary><strong>R2 Q3.</strong> You set a &#36;50 budget and spend reaches &#36;80. What did Google do?</summary>

It only sent alerts. Budgets never stop spending (same as AWS Budgets).

</details>

<details>
<summary><strong>R2 Q4.</strong> You get "quota exceeded" after creating your 15th VPC network, and later after a burst of API calls. Which quota types?</summary>

The 15th VPC is an **allocation** quota (a cap on how many). The burst of calls is a **rate** quota (a cap per time window that resets). Both are per project.

</details>

<details>
<summary><strong>R3 Q1.</strong> You need a custom role "vmOperator" in every project under the Engineering folder. Where do you create it?</summary>

On the **organization**. A custom role can't be created on a folder; create it on the org, then grant it on the folder.

</details>

<details>
<summary><strong>R3 Q2.</strong> Which tool gives a browser terminal with gcloud installed and logged in?</summary>

Cloud Shell (≈ AWS CloudShell).

</details>

<details>
<summary><strong>R3 Q3.</strong> A legacy app needs full OS control and per-second billing. Which service?</summary>

Compute Engine (≈ EC2).

</details>

<details>
<summary><strong>R3 Q4.</strong> Your Cloud Storage files are encrypted on disk with no configuration. Which security layer?</summary>

Storage services (encryption at rest by default).

</details>

<details>
<summary><strong>R4 Q1.</strong> Bob is Owner on a project, but a deny policy on the org blocks <code>compute.instances.delete</code>. Can he delete a VM?</summary>

No. Deny is checked before allow, and the org-level deny is inherited down. Bob can't remove it himself; see 4.1.

</details>

<details>
<summary><strong>R4 Q2.</strong> Which org-level role controls who can create projects, and so who can spend money?</summary>

Project Creator.

</details>

<details>
<summary><strong>R4 Q3.</strong> Alice should manage a service account, Bob should only see it. How?</summary>

Give each a role *on the service account itself*, because a service account is also a resource.

</details>

<details>
<summary><strong>R4 Q4.</strong> An employee leaves. Where do you disable their account and remove them from all groups at once?</summary>

Cloud Identity, in the Google Admin console (≈ IAM Identity Center).

</details>

<details>
<summary><strong>R4 Q5.</strong> A VM runs the whole month. What discount applies automatically?</summary>

The sustained use discount.

</details>

<details>
<summary><strong>R4 Q6.</strong> Why does the Lab 1 LAMP site open in your browser?</summary>

A firewall rule allows HTTP (tcp:80) to the VM's external IP, and Apache is listening on port 80. See the firewall deep dive in 4.1.

</details>

### 4.3 Three things to remember

1. Deny beats allow, and it is inherited down the tree.
2. Roles can be granted on anything, including a service account; custom roles are created only on an org or a project.
3. A VM is reachable only if a firewall rule lets the traffic in, and something is listening on that port.

---
*Scope: Google Cloud Fundamentals: Core Infrastructure, modules M0 to M2 · Mirrors the Claude Doc linked at the top; changes go into both.*
