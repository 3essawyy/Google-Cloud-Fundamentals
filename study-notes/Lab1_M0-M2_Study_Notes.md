# Lab 1 Study Notes: M0 to M2

> As of 2026-10-17. Kept in sync with the Claude Doc of the same name: https://claude.ai/code/artifact/97e12c9e-19a1-46c4-aebb-2633255c7281

## M0: Course introduction

Only one point from M0 matters for the labs: a lab gives you a temporary project and student account for a fixed time, and **it cannot be paused**. Start a lab only when you have a continuous block of time.

Everything below keeps what Lab 1 or the Associate Cloud Engineer (ACE) exam needs. Cut: etiquette and agenda slides, repeated section dividers, product history detail, sustainability marketing, TensorFlow, and the mobile app's feature list. Sources: the M0, M1 and M2 `_v2.md` study guides in [modules/](../modules/).

## M1: Introducing Google Cloud

### Cloud computing: the 5 traits (NIST definition)

1. **On-demand self-service:** you get compute, storage and network through a web interface, with no human in the loop.
2. **Broad network access:** over the internet, from anywhere.
3. **Resource pooling:** the provider allocates from a big shared pool, buys in bulk and passes savings on; you don't care where the hardware is.
4. **Rapid elasticity:** scale up or down quickly.
5. **Measured service:** pay only for what you use, or reserve; stop using and you stop paying.

How we got here: colocation (rent rack space) → virtualized data centers (virtual servers, but you still maintain them) → Google's third wave: container-based, automated, elastic services that provision the infrastructure for you.

### Service models

| Model | You manage | Provider manages | Google example | You pay for |
| --- | --- | --- | --- | --- |
| IaaS | OS, runtime, app | Hardware, network, virtualization | Compute Engine | Resources you allocate |
| PaaS | App code (bound to provided libraries) | OS, runtime, infrastructure | App Engine | Resources you use |
| Serverless | Code or container only | Everything else, including scaling | Cloud Run, Cloud Run functions | Per request or event |
| SaaS | Nothing, you just use it | Everything | Gmail, Docs, Drive (Google Workspace) | Subscription |

The trend is toward managed services: less time on infrastructure, more on the product.

### Global infrastructure

- **Location → Region → Zone.** A zone is where resources such as a VM are actually deployed. A region holds several zones.
- Resources in **several zones of one region** give fault tolerance.
- Resources in **several regions** bring the app closer to users worldwide and survive a whole-region outage.
- Some services run **multi-region** (for example Cloud Storage `US`, `EU`, `ASIA`, used in Lab 3).
- 100+ edge caching nodes serve popular content from the nearest location to cut latency (the time a packet takes from source to destination).
- Live counts of regions and zones: cloud.google.com/about/locations.

### Security: defense in depth, layer by layer

| Layer | What Google does |
| --- | --- |
| Hardware infrastructure | Custom-designed server boards, network gear and a hardware security chip; secure boot stack (signed BIOS, bootloader, kernel, OS image); layered physical premises security |
| Service deployment | RPC traffic between data centers is encrypted |
| User identity | Login page challenges on risk signals (new device or location); second factor with U2F security keys |
| Storage services | **Encryption at rest by default**, with centrally managed keys; hardware encryption on drives and SSDs |
| Internet communication | Google Front End (GFE) terminates TLS with proper certificates and perfect forward secrecy; multi-layer DoS protection |
| Operational security | Intrusion detection and Red Team exercises; limited and monitored admin access; U2F keys for all employees; central source control with two-party code review; bug bounty |

### Open APIs and open source

Google publishes key technology as open source so you are not locked in. Kubernetes and GKE let you mix microservices across clouds, and Google Cloud Observability monitors workloads across multiple providers.

### Pricing and billing

- **Per-second billing:** Compute Engine, GKE, Managed Service for Apache Spark (Dataproc), App Engine flexible environment.
- **Sustained use discounts:** applied automatically when a VM runs more than 25% of the month, for every extra minute.
- **Custom machine types:** choose the exact vCPU and memory, so you pay only for what the workload needs.
- **Pricing calculator** to estimate costs: cloud.google.com/products/calculator.
- Tools to avoid surprise bills:
    1. **Budgets** at billing-account or project level, fixed or tied to a metric such as a % of last month's spend.
    2. **Alerts** when spend nears the budget, typically at 50%, 90% and 100%. A budget alerts you; it does not stop spending.
    3. **Reports** in the console, by project or service.
    4. **Quotas**, which cap consumption to stop errors or attacks from running away.
- Quotas apply **per project** and come in two types:
    - **Rate quota** resets after a time window. Example: GKE API, 3,000 calls per project every 100 seconds.
    - **Allocation quota** caps how many resources you can have. Example: 15 VPC networks per project.
    - Some quotas can be raised by requesting an increase from Google Cloud.

### M1 self-check quiz

1. Why use resources in several zones within one region?
2. Which service model binds your code to libraries that give access to the infrastructure it needs?
3. Why use resources in several regions?
4. Name the 5 traits of cloud computing.
5. In IaaS do you pay for resources allocated or resources used? And in PaaS?
6. A VM runs all month. What discount do you get without doing anything?
7. What is the difference between a rate quota and an allocation quota? At what level do both apply?
8. Your budget is $1,000 with an alert at 90%. What happens when spend reaches $900, and what happens at $1,100?
9. Which layer of Google's security model covers encryption at rest?

Answers

1. Fault tolerance.
2. PaaS.
3. Closer to users around the world, and protection against a whole-region failure.
4. On-demand self-service, broad network access, resource pooling, rapid elasticity, measured service.
5. IaaS: allocated. PaaS: used.
6. A sustained use discount (it applies past 25% of the month).
7. A rate quota resets after a time window; an allocation quota caps a count of resources. Both are per project.
8. At $900 you get an alert. At $1,100 you get another alert if one is set at 100%, but nothing stops: budgets don't cap spend.
9. Storage services.

## M2: Resources and Access

### Resource hierarchy

Four levels, bottom up: **Resources → Projects → Folders → Organization node.**

- **Resources:** VMs, buckets, VPC networks, BigQuery tables, anything you create.
- **Projects:** every resource belongs to exactly one project.
- **Folders:** group projects (for example per department) and can nest; they let teams delegate admin rights. Folders need an organization node.
- **Organization node:** the top. You get one through Google Workspace or Cloud Identity. A new org node still lets everyone in the domain create projects and billing accounts, to avoid disruption. Special roles live here, such as **Organization Policy Administrator** and **Project Creator** (controls who can create projects and so spend money).

Policies can be set at the organization, folder and project levels (and on some individual resources) and are **inherited downward**. Effective access on a resource is the **union** of everything granted at and above it. Example: Viewer at org + Editor at folder + Storage Admin at project = all three on a bucket in that project.

### Projects

- The project is where you **enable APIs and services**, link billing, and add or remove collaborators. Projects are billed and managed separately.

| Attribute | Globally unique? | Set by | Changeable? |
| --- | --- | --- | --- |
| Project ID | Yes | You at creation (Google suggests one) | **No, immutable after creation** |
| Project name | No | You | Yes, any time |
| Project number | Yes | Google | No |

- The project ID is what you pass to tools to say which project to work on (Cloud Shell's `$DEVSHELL_PROJECT_ID`, `gcloud config set project`).
- **Resource Manager** is the API to list, create, update, delete and recover projects (RPC and REST).

### Identity and Access Management (IAM)

An IAM policy says **who** can do **what** on **which resource**.

- **Who (principal):** a Google account, a Google group, a service account, or a Cloud Identity domain, each identified by an email address.
- **What (role):** a collection of permissions. Granting a role grants all its permissions.
- **Which resource:** the level of the hierarchy where you grant it; it applies there and to everything below.
- **Deny policies** block specific permissions whatever roles say. IAM checks deny before allow, and deny policies are inherited too.

### The three kinds of IAM roles (broadest to finest)

1. **Basic:** Owner, Editor, Viewer. They apply to every resource in the project.
    - Viewer: look, no changes.
    - Editor: look and change.
    - Owner: look and change, plus manage roles and permissions and set up billing.
    - Too broad when several people share a project with sensitive data.
2. **Predefined:** curated per service, for example `roles/compute.instanceAdmin` on a project, folder or organization.
3. **Custom:** your own permission set for least privilege, for example an "instanceOperator" that can start and stop VMs but not reconfigure them. Created at **project or organization level, never at folder level**. A project-level custom role can't include org- or folder-only permissions such as `resourcemanager.organizations.get`.

Billing without resource access is a separate role, Billing Account Administrator. The slides list a "billing administrator" next to the basic roles; on the exam the basic roles are Owner, Editor and Viewer.

### Service accounts

- An identity for an application or VM, not a person, so it can call other services without a human.
- Named with an email address, and authenticates with **cryptographic keys instead of a password**.
- Gets roles like any principal. Example: a VM whose service account has Instance Admin can create, modify and delete other VMs.
- It is also a **resource**, so people get roles on it: Alice can be Editor of the service account, Bob only Viewer.

### Cloud Identity

- Manages users and groups centrally in the Google Admin console instead of loose Gmail accounts and groups.
- Lets admins use existing Active Directory or LDAP usernames and passwords.
- When someone leaves, disable the account and remove them from groups in one place.
- Free edition, and a premium edition that adds mobile device management. Google Workspace customers already have it.

### Four ways to work with Google Cloud

1. **Google Cloud console:** web GUI to deploy, scale and diagnose; search resources; SSH to VMs in the browser; set budgets.
2. **Google Cloud SDK and Cloud Shell:** the SDK includes the `gcloud` CLI and tools like `bq` for BigQuery. **Cloud Shell** is a browser terminal: Debian-based, **5 GB persistent home directory**, pre-authenticated, SDK preinstalled. This is where you run lab commands.
3. **APIs:** every service has one; the APIs Explorer lets you try them; client libraries exist for Java, Python, PHP, C#, Go, Node.js, Ruby and C++.
4. **Google Cloud app (mobile):** start, stop and SSH to VMs, start and stop Cloud SQL, see billing alerts and key metrics.

### M2 self-check quiz

1. Services and APIs are enabled on a per-what basis?
2. Order the IAM role types from broadest to finest-grained.
3. Which value is globally unique and unchangeable after creation, but chosen by you during creation?
4. Name the four levels of the resource hierarchy from the top.
5. Bob has Viewer on the organization and Editor on a folder. What can he do on a project inside that folder?
6. Bob has an allow policy granting Editor, and a deny policy denying `compute.instances.delete`. Can he delete a VM?
7. At which levels can you create a custom role, and where can't you?
8. How does a service account authenticate, and why can it also have IAM policies attached to it?
9. An employee leaves. Which tool lets an admin remove their access in one place?
10. Name Cloud Shell's two key properties for running lab commands.

Answers

1. Per project.
2. Basic, predefined, custom.
3. The project ID.
4. Organization node, folders, projects, resources.
5. Edit: he gets the union of Viewer and Editor, inherited down to the project.
6. No. Deny policies are checked first and win.
7. Project or organization level. Never at folder level.
8. With cryptographic keys, not a password. It is also a resource, so people can be granted roles to use or manage it.
9. Cloud Identity, through the Google Admin console.
10. Pre-authenticated with the SDK preinstalled, and a persistent 5 GB home directory.

## Bridge to Lab 1: Cloud Marketplace LAMP

- **Marketplace** offers pre-packaged solutions. Click to Deploy builds a **Compute Engine VM** (IaaS) running Linux, Apache, MySQL and PHP.
- You pick a **zone** and machine type (`e2-medium`): the zone decides where the VM lives.
- The deploy asks you to **enable the Compute Engine API**, because APIs are enabled **per project**.
- The lab project ID is the globally unique `qwiklabs-gcp-...` you see in the console.
- You are signed in as a student account holding a role on that project: IAM in action.
- The Site URL opens because a **firewall rule allows HTTP (tcp:80)** to the VM's external IP.
- Patching the VM's OS and software is your job, not Google's: that is the IaaS side of shared responsibility.

This file mirrors the Claude Doc linked at the top; changes go into both.
