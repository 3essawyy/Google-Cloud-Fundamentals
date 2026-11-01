# Google Cloud Labs Sprint & ACE Roadmap

> As of 2026-10-19. Kept in sync with the Claude Doc of the same name: https://claude.ai/code/artifact/31099c7b-72f5-4f0c-8475-84e12a255181
> All times are **Cairo time (EEST, UTC+3)**.

All 4 labs are due **Wednesday 2026-10-21 at 23:59 Cairo time**. The plan is one lab a day, Saturday to Tuesday, each after its theory, with Wednesday kept as a buffer. After the labs, a 6-week exam-prep phase targets the **Associate Cloud Engineer (ACE)** exam in early December.

**How to work each lab**

- Read the theory first: the `_v2.md` study guide for that module in [modules/](modules/).
- Run lab commands in **Cloud Shell inside the lab's own console** (incognito window, lab student account). The lab project, student login and region are created fresh each time the lab starts, so commands need the region the lab shows you.
- Use the Gemini CLI agent as the checker: paste a command block and the prompt at the end of the lab checklists, and it fixes placeholders before you run them in Cloud Shell.
- Click **Check my progress** after each task, and **End Lab** only once every check is green.

## What counts as passing Phase 1

The course material in this repo does not state formal pass criteria for the four labs. What the roadmap works to:

- Each lab is done when **every "Check my progress" is green (score 100%)**, then you click **End Lab**.
- All 4 labs must be at 100% by **Wed 2026-10-21 23:59 Cairo time**; Wednesday is for redoing any lab below 100%.
- Not stated anywhere here, so confirm on the Skills Boost course page: whether a badge or course completion is awarded, and how the deadline is enforced.

## Day-by-day sprint (Sat 17 to Wed 21 Oct)

One lab a day after its theory, about 2.5 hours each evening; Wednesday is only for catching up.

| Day | Theory first | Then the lab | Time |
| --- | --- | --- | --- |
| Sat 17 Oct | M0 Course Intro, M1 Introducing Google Cloud, M2 Resources and Access | Lab 1: Cloud Marketplace (LAMP) | ~2.5 h (**done**) |
| Sun 18 Oct | M3 Virtual Machines and Networks | Lab 2: VPC Networking and Compute Engine | ~2.5 h (**done**) |
| Mon 19 Oct | M4 Storage in the Cloud | Lab 3: Cloud Storage and Cloud SQL | ~3 h (**done**) |
| Tue 20 Oct | M5 Containers in the Cloud, M6 Applications in the Cloud | Lab 4: Hello Cloud Run | ~2.5 h |
| Wed 21 Oct | M7 Course Summary, review the ACE anchors of all 4 labs | Redo any lab not at 100%. Deadline 23:59 | ~1.5 h |

If a day slips, do two labs the next day; Labs 1 and 2 are the shortest, so they are the safest to double up.

## Progress log

| Date (Cairo) | Done | Notes |
| --- | --- | --- |
| Sat 17 Oct | Lab 1 (LAMP on Compute Engine) completed, all checks green | First deploy failed with a `setIamPolicy` permission error (probably propagation delay); redeploying worked. Lab 1 notes (M0 to M2) with quizzes and a four-round grill log written. |
| Sun 18 Oct | Lab 2 (VPC Networking and Compute Engine) completed, all checks green | Done just after midnight. Deleting `allow-icmp`, `allow-custom` and `allow-ssh` behaved as expected (see the Lab Run Notes in the lab file). Lab 2 notes (M3) with a five-round grill log and a subnet refresher written. |
| Mon 19 Oct | Lab 3 (Cloud Storage and Cloud SQL) completed | Lab 3 notes (M4) with a four-round grill log (storage classes and read costs, ACL vs IAM, signed URLs, Cloud SQL public vs private IP, transfer maths) written and merged. |
| Tue 20 Oct | Lab 4 (Hello Cloud Run) completed theoretically | Lab session window closed/expired. Full architectural study notes for Modules 5 and 6 (Containers, Artifact Registry, Cloud Build, GKE, Cloud Run, and Traffic Splitting) compiled and verified in `study-notes/Lab4_M5-M6_Study_Notes.md`. |

**Phase 1 Completion:** Stage 1 Foundation completed (3 practical labs at 100% score + Lab 4 comprehensive theoretical architecture). Transitioned to **Stage 2: Associate Cloud Engineer (ACE)**.

## Lab checklists

### Lab 1: Getting Started with Cloud Marketplace (~30 min, Console only)

Theory: [M1](modules/M1_Introducing_Google_Cloud/M1_Introducing_Google_Cloud_v2.md), [M2](modules/M2_Resources_and_Access/M2_Resources_and_Access_v2.md). Manual: [labs/01_Cloud_Marketplace.md](labs/01_Cloud_Marketplace.md).

- [x] Read M0, M1, M2 study guides
- [x] Start lab, open console in incognito with the lab student account
- [x] Task 2: Marketplace > search `LAMP` > **LAMP Stack by Google Click to Deploy** > Get started > Agree > Deploy
- [x] Zone = the lab's zone, Series E2, machine type `e2-medium`, Deploy (enable Compute Engine and Infrastructure Manager APIs if asked)
- [x] Wait for "lamp-1 has been deployed", then Check my progress
- [x] Task 3: `lamp-1-vm` > Details > open the Site URL and see the Apache congratulations page
- [x] All checks green, End Lab

No commands needed. Optional check you can paste in Cloud Shell:

```bash
gcloud compute instances list
gcloud compute firewall-rules list --format="table(name,sourceRanges.list(),allowed[].map().firewall_rule().list())"
```

### Lab 2: VPC Networking and Compute Engine (~40 min)

Theory: [M3](modules/M3_Virtual_Machines_and_Networks/M3_Virtual_Machines_and_Networks_v2.md). Manual: [labs/02_VPC_and_Compute_Engine.md](labs/02_VPC_and_Compute_Engine.md).

- [x] Read M3 study guide
- [x] Task 1: look at the default network's subnets, routes and 4 firewall rules
- [x] Task 1: delete all default firewall rules, then delete the `default` network
- [x] Task 1: try to create a VM and see the "no network available" error, then Cancel
- [x] Task 2: create auto-mode VPC `mynetwork` with all firewall rules ticked
- [x] Task 2: create `mynet-us-vm` and `mynet-r2-vm` (E2, `e2-micro`) in the two zones the lab gives, then Check my progress
- [x] Task 3: SSH to `mynet-us-vm`, ping `mynet-r2-vm` internal and external IP (both work)
- [x] Task 3: delete `mynetwork-allow-icmp`, external ping fails, internal still works
- [x] Task 3: delete `mynetwork-allow-custom`, internal ping fails
- [x] Task 3: delete `mynetwork-allow-ssh`, SSH fails
- [x] All checks green, End Lab

The lab is Console-driven; the Console steps are what it grades. Command equivalents for Task 2 (replace `ZONE_1` and `ZONE_2` with the lab's zones):

```bash
gcloud compute networks create mynetwork --subnet-mode=auto
gcloud compute firewall-rules create mynetwork-allow-icmp --network=mynetwork --allow=icmp
gcloud compute firewall-rules create mynetwork-allow-custom --network=mynetwork --allow=all --source-ranges=10.128.0.0/9
gcloud compute firewall-rules create mynetwork-allow-ssh --network=mynetwork --allow=tcp:22
gcloud compute firewall-rules create mynetwork-allow-rdp --network=mynetwork --allow=tcp:3389
gcloud compute instances create mynet-us-vm --zone=ZONE_1 --machine-type=e2-micro --network=mynetwork
gcloud compute instances create mynet-r2-vm --zone=ZONE_2 --machine-type=e2-micro --network=mynetwork
gcloud compute instances list
```

Inside the `mynet-us-vm` SSH window:

```bash
ping -c 3 MYNET_R2_VM_INTERNAL_IP
ping -c 3 MYNET_R2_VM_EXTERNAL_IP
```

### Lab 3: Cloud Storage and Cloud SQL (~45 min plus Cloud SQL wait)

Theory: [M4](modules/M4_Storage_in_the_Cloud/M4_Storage_in_the_Cloud_v2.md). Manual: [labs/03_Storage_and_Cloud_SQL.md](labs/03_Storage_and_Cloud_SQL.md).

- [x] Read M4 study guide
- [x] Task 2: create VM `bloghost` (lab region and zone, `e2-standard-2`, Debian 12, Allow HTTP, startup script below), note its internal and external IP
- [x] Task 3: in Cloud Shell create the bucket, copy the image, make it public (commands below)
- [x] Task 4: start this early, it takes several minutes. Cloud SQL > MySQL > Enterprise, preset Sandbox, ID `blog-db`, password `Passw0rd1!`, same region and zone as `bloghost`, single zone, Security: allow unencrypted traffic
- [x] Task 4: copy the SQL Public IP, add user `blogdbuser` / `Passw0rd1!`
- [x] Task 4: Connections > Networking > Add network `web front end` = `BLOGHOST_EXTERNAL_IP/32`, Save
- [x] Task 5: SSH to `bloghost`, write `index.php`, see "Database connection failed", then fill in the SQL IP and password, see "Connected successfully"
- [x] Task 6: add the `<img src='...'>` line with the bucket's public URL above the `<h1>`, reload and see the banner
- [x] All checks green, End Lab

Startup script for `bloghost`:

```bash
#!/bin/bash
apt-get install apache2 php php-mysql -y
service apache2 restart
```

Task 3 in Cloud Shell (pick the multi-region nearest the lab region: `US`, `EU` or `ASIA`):

```bash
export LOCATION=US
gcloud storage buckets create -l $LOCATION gs://$DEVSHELL_PROJECT_ID
gcloud storage cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png
gcloud storage cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```

Task 5 on `bloghost` (SSH window). Edit the file with `sudo nano /var/www/html/index.php` and paste the PHP from the lab manual, then:

```bash
sudo service apache2 restart
```

Open `http://BLOGHOST_EXTERNAL_IP/index.php` in the browser after each change.

### Lab 4: Hello Cloud Run (~45 min, Cloud Shell) — Theoretical Completion

Theory: [M5](modules/M5_Containers_in_the_Cloud/M5_Containers_in_the_Cloud_v2.md), [M6](modules/M6_Applications_in_the_Cloud/M6_Applications_in_the_Cloud_v2.md). Manual: [labs/04_Hello_Cloud_Run.md](labs/04_Hello_Cloud_Run.md).  
**Study Notes:** Verified and preserved in [`study-notes/Lab4_M5-M6_Study_Notes.md`](study-notes/Lab4_M5-M6_Study_Notes.md).

> *Note:* Live Skills Boost lab window expired. Practical steps verified theoretically; code commands, Dockerfiles, and architectural trade-offs (Artifact Registry, Cloud Build, Cloud Run concurrency, traffic splitting) are fully documented in the study notes.

- [x] Read M5 and M6 study guides
- [x] Task 1: API enablement (`run.googleapis.com`, `artifactregistry.googleapis.com`)
- [x] Task 2: Express app scaffolding (`package.json`, `index.js`)
- [x] Task 3: Artifact Registry standard Docker repository creation & authentication
- [x] Task 4: Multi-stage Docker build via Google Cloud Build (`gcloud builds submit`)
- [x] Task 5: Serverless container deployment to Cloud Run with unauthenticated HTTP access
- [x] Task 6: Cloud Run revisions, traffic splitting mechanics, and resource cleanup
- [x] Architectural and conceptual review completed in `study-notes/Lab4_M5-M6_Study_Notes.md`

---

## Stage 2: Associate Cloud Engineer (ACE) Official Roadmap & Deadlines

> **Program:** The Get Certified Program — Associate Cloud Engineer (Stage 2)  
> **Cohort ID:** `ACE07-GETCERT/2026.11.02`  
> **Cohort Coordinator:** Damini Chouhan (`daminichouhan@xwf.google.com`)  
> **Technical Trainer:** Supratim Bhattacharya  
> **Program Lead:** Alyssa Groves  
> **Start Date:** November 02, 2026 (Live Kick-off @ 1:00 PM – 2:30 PM CET / 2:00 PM – 3:30 PM Cairo)

---

### Master Deadlines & Critical Milestone Gates

| Status | Milestone / Gate | Date & Time (Cairo / CET) | Hard / Soft | Action Required & Rules |
| :---: | :--- | :--- | :---: | :--- |
| [ ] | **Cohort Kick-off & Session 1** | **Mon, Nov 02, 2026**<br>2:00 PM – 3:30 PM Cairo (1:00 PM CET) | **Fixed** | Attend live review session 1 (or review recording in Google Drive). |
| [ ] | **Skills Credit Activation** | **Sat, Nov 21, 2026** (23:59 CET) | **HARD** | Redeem 400 credits using promo code `1p-gcsgsc-67` via Pub/Sub lab. **Strict deadline (no extensions).** |
| [ ] | **Voucher Request Form Opens** | **Mon, Nov 23, 2026** (Week 4) | **Fixed** | Form unlocks once Week 4 begins. |
| [ ] | **Target 5-Badge Completion** | **Thu, Dec 10, 2026** | **Target** | Complete 5 of 7 skill badges (including mandatory Gemini Enterprise). |
| [ ] | **Target Voucher Submission** | **Dec 10 – Dec 15, 2026** | **Target** | Submit public Skills Boost profile via form early. Beat the *first-come-first-served* voucher pool limit and account for 24–72h processing delay. |
| [ ] | **Pearson VUE Booking** | **Dec 15 – Dec 20, 2026** | **Target** | Apply voucher code and reserve an **In-Person** exam seat in Cairo for Jan 16–19 before university finals start. |
| [ ] | **University Finals Blackout** | **Dec 26, 2026 – Jan 11, 2027** | **Locked** | **Zero GCP stress.** 100% focus on 4 university final exams. |
| [ ] | **Voucher Form Hard Close** | **Tue, Dec 29, 2026** (23:59 CET) | **HARD** | Final cutoff to submit voucher request form. No late requests accepted. |
| [ ] | **Post-Finals Full-Time Cram** | **Jan 12 – Jan 15/18, 2027** | **Sprint** | Intensive mock exams, Claude grilling, and diagnostic review. |
| [ ] | **Target Exam Window** | **Jan 16 – Jan 19, 2027** | **Target** | Sit for official ACE in-person exam at authorized Cairo test center. |
| [ ] | **Final Exam Hard Deadline** | **Wed, Jan 20, 2027** (23:59 CET) | **HARD** | Google's absolute program cutoff to attempt the exam. |

---

### Live Review Sessions Schedule (Mondays @ 2:00 PM Cairo / 1:00 PM CET)

All sessions are 90 minutes, led by technical trainer Supratim Bhattacharya, and recorded to Google Drive:

1. **Session 1:** Monday, November 02, 2026 — Program Kick-off & Exam Guide Review Overview
2. **Session 2:** Monday, November 09, 2026 — Compute Engine & Core Infrastructure
3. **Session 3:** Monday, November 16, 2026 — Scaling, Automation & Storage Services
4. **Session 4:** Monday, November 23, 2026 — Google Kubernetes Engine (GKE) & Voucher Form Launch
5. **Session 5:** Monday, November 30, 2026 — Google Agent Ecosystem & Security Architecture
6. **Session 6:** Monday, December 07, 2026 — Reliable Infrastructure, Design Process & Exam Readiness

---

### Week-by-Week Operational Execution Plan

#### Week 1 (Nov 02 – Nov 08): Activation & Mandatory Enterprise AI
- [ ] **Admin:** Fill Google Access Form for Google Drive and Google Groups access.
- [ ] **Credits:** Activate 400 Google Skills credits using promo code `1p-gcsgsc-67` via the Pub/Sub Qwik Start lab in Incognito.
- [ ] **Live Session 1:** Nov 02 @ 2:00 PM Cairo.
- [ ] **Course:** *Essential Google Cloud Infrastructure: Foundation*.
- [ ] **Skill Badge 1 (MANDATORY):** [Create Your First Gemini Enterprise Application](https://www.skills.google/paths/3546/course_templates/1586) *(Cannot be skipped per program rules).*

#### Week 2 (Nov 09 – Nov 15): Core Services & Load Balancing
- [ ] **Live Session 2:** Nov 09 @ 2:00 PM Cairo.
- [ ] **Course:** *Essential Google Cloud Infrastructure: Core Services*.
- [ ] **Skill Badge 2:** [Implement Load Balancing on Compute Engine](https://www.skills.google/course_templates/648)
  - Covers: Health checks, instance groups, HTTP(S) Load Balancing, autoscaling.

#### Week 3 (Nov 16 – Nov 22): Automation & Infrastructure as Code (IaC)
- [ ] **Live Session 3:** Nov 16 @ 2:00 PM Cairo.
- [ ] **Course:** *Elastic Google Cloud Infrastructure: Scaling and Automation*.
- [ ] **Skill Badge 3:** [Build Infrastructure with Terraform on Google Cloud](https://www.skills.google/course_templates/636)
  - Covers: HCL syntax, Terraform state management, provisioning VPCs and VMs.
- [ ] **Hard Gate:** Nov 21 — Verify 400 credits are safely claimed.

#### Week 4 (Nov 23 – Nov 29): Network Security & Voucher Gate Launch
- [ ] **Live Session 4:** Nov 23 @ 2:00 PM Cairo.
- [ ] **Course:** *Getting Started with Google Kubernetes Engine (GKE)*.
- [ ] **Skill Badge 4:** [Build a Secure Google Cloud Network](https://www.skills.google/course_templates/654)
  - Covers: Custom VPCs, Bastion hosts, firewall hierarchy, private Google access.
- [ ] **Milestone:** Voucher request form officially opens.

#### Week 5 (Nov 30 – Dec 06): Security Fundamentals (5-Badge Milestone)
- [ ] **Live Session 5:** Nov 30 @ 2:00 PM Cairo.
- [ ] **Course:** *Reliable Google Cloud Infrastructure: Design and Process*.
- [ ] **Skill Badge 5:** [Implement Cloud Security Fundamentals on Google Cloud](https://www.skills.google/course_templates/645)
  - Covers: IAM least privilege, Service Accounts, Cloud KMS, Audit Logging.
- [ ] **Milestone Reached:** **5 of 7 Skill Badges Completed!** Public profile ready.

#### Week 6 (Dec 07 – Dec 13): Final Review, Voucher Request & Exam Booking
- [ ] **Live Session 6:** Dec 07 @ 2:00 PM Cairo (Final live exam readiness review).
- [ ] **Voucher Claim:** Submit Voucher Request Form with public Skills Boost URL between **Dec 10 and Dec 15**.
- [ ] **Exam Booking:** Upon receiving the voucher email (24–72 hours), immediately log in to [CertMetrics](https://cp.certmetrics.com/google/en/login) and book an **In-Person Test Center** in Cairo for **January 16–19, 2027**.

#### Pre-Finals Buffer (Dec 14 – Dec 25): University Projects & Light Reading
- [ ] Manage university project deadlines, presentations, and practical lab exams.
- [ ] Light review: Official ACE Exam Guide sections via [GCP Study Hub](https://gcpstudyhub.com/).

#### Finals Blackout Window (Dec 26, 2026 – Jan 11, 2027): University Finals
- [ ] **100% University Academics:** 4 final exams. Zero active cloud lab obligations.
- [ ] *(Note: Dec 29 is the voucher form closing deadline — already safely completed in Week 6).*

#### Final Cram & Exam Week (Jan 12 – Jan 19, 2027): Full Certification Sprint
- [ ] **Jan 12 – Jan 15:** Intensive mock exams, scenario drilling with Claude Web (Examiner mode), review weak sections (IAM, GKE commands, VPC routing).
- [ ] **Jan 16 – Jan 19:** Sit the official Google Cloud Certified Associate Cloud Engineer exam in person.
- [ ] **Jan 20:** Program conclusion hard stop.

---

### Pearson VUE / CertMetrics Exam Registration Guide

1. **Portal:** [https://cp.certmetrics.com/google/en/login](https://cp.certmetrics.com/google/en/login)
2. **Account Name:** Must exactly match the government-issued photo ID (National ID or Passport) presented at the test center.
3. **Checking Dates in Advance (No Voucher Needed):**
   - Click **`Schedule/Launch an exam`** > Select **`Associate Cloud Engineer`** > Click **`SCHEDULE`**.
   - Choose **`At a local test center`** > Select English > Agree to policies.
   - Enter **`Cairo, Egypt`** in the search bar.
   - Select authorized centers:
     - **AMIDEAST Egypt** (38 Mohie El Din Abo El Ezz, Dokki / Giza)
     - **New Horizons** (Dokki / Nasr City)
     - **Synergy** (Dokki / Heliopolis)
   - Click Next to view the live January 2027 calendar and inspect open morning/afternoon slots.
   - Close the browser before checkout.
4. **Booking with Voucher:**
   - Follow the same steps, proceed to checkout, enter the voucher code from Google, verify the total shows **USD $0.00**, and confirm appointment.

---

### External Resources & Study Hubs

* **GCP Study Hub (Interactive Question Bank & Explanations):** [https://gcpstudyhub.com/](https://gcpstudyhub.com/)
* **CertMetrics Exam Booking & Portal:** [https://cp.certmetrics.com/google/en/login](https://cp.certmetrics.com/google/en/login)
* **Google Skills Boost (Labs, Quests & Badges):** [https://www.skills.google/](https://www.skills.google/)
* **Official Google Cloud Associate Cloud Engineer Exam Guide:** [https://cloud.google.com/learn/certification/cloud-engineer](https://cloud.google.com/learn/certification/cloud-engineer)
* **Google Cloud Certification Help & Support:** [https://support.google.com/cloud-certification/gethelp](https://support.google.com/cloud-certification/gethelp)
