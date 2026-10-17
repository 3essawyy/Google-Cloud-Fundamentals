# Google Cloud Labs Sprint & ACE Roadmap

> As of 2026-10-17. Kept in sync with the Claude Doc of the same name: https://claude.ai/code/artifact/31099c7b-72f5-4f0c-8475-84e12a255181
> All times are **Cairo time (EEST, UTC+3)**.

All 4 labs are due **Wednesday 2026-10-21 at 23:59 Cairo time**. The plan is one lab a day, Saturday to Tuesday, each after its theory, with Wednesday kept as a buffer. After the labs, a 6-week exam-prep phase targets the **Associate Cloud Engineer (ACE)** exam in early December.

**How to work each lab**

- Read the theory first: the `_v2.md` study guide for that module in [modules/](modules/).
- Run lab commands in **Cloud Shell inside the lab's own console** (incognito window, lab student account). The lab project, student login and region are created fresh each time the lab starts, so commands need the region the lab shows you.
- Use the Gemini CLI agent as the checker: paste a command block and the prompt at the end of the lab checklists, and it fixes placeholders before you run them in Cloud Shell.
- Click **Check my progress** after each task, and **End Lab** only once every check is green.

## Day-by-day sprint (Sat 17 to Wed 21 Oct)

One lab a day after its theory, about 2.5 hours each evening; Wednesday is only for catching up.

| Day | Theory first | Then the lab | Time |
| --- | --- | --- | --- |
| Sat 17 Oct | M0 Course Intro, M1 Introducing Google Cloud, M2 Resources and Access | Lab 1: Cloud Marketplace (LAMP) | ~2.5 h (**done**) |
| Sun 18 Oct | M3 Virtual Machines and Networks | Lab 2: VPC Networking and Compute Engine | ~2.5 h |
| Mon 19 Oct | M4 Storage in the Cloud | Lab 3: Cloud Storage and Cloud SQL | ~3 h |
| Tue 20 Oct | M5 Containers in the Cloud, M6 Applications in the Cloud | Lab 4: Hello Cloud Run | ~2.5 h |
| Wed 21 Oct | M7 Course Summary, review the ACE anchors of all 4 labs | Redo any lab not at 100%. Deadline 23:59 | ~1.5 h |

If a day slips, do two labs the next day; Labs 1 and 2 are the shortest, so they are the safest to double up.

## Progress log

| Date (Cairo) | Done | Notes |
| --- | --- | --- |
| Sat 17 Oct | Lab 1 (LAMP on Compute Engine) completed, all checks green | First deploy failed with a `setIamPolicy` permission error (probably propagation delay); redeploying worked. Lab 1 notes (M0 to M2) with quizzes and a four-round grill log written. |

**Next:** Sun 18 Oct, M3 notes and Lab 2 (VPC Networking and Compute Engine).

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

- [ ] Read M3 study guide
- [ ] Task 1: look at the default network's subnets, routes and 4 firewall rules
- [ ] Task 1: delete all default firewall rules, then delete the `default` network
- [ ] Task 1: try to create a VM and see the "no network available" error, then Cancel
- [ ] Task 2: create auto-mode VPC `mynetwork` with all firewall rules ticked
- [ ] Task 2: create `mynet-us-vm` and `mynet-r2-vm` (E2, `e2-micro`) in the two zones the lab gives, then Check my progress
- [ ] Task 3: SSH to `mynet-us-vm`, ping `mynet-r2-vm` internal and external IP (both work)
- [ ] Task 3: delete `mynetwork-allow-icmp`, external ping fails, internal still works
- [ ] Task 3: delete `mynetwork-allow-custom`, internal ping fails
- [ ] Task 3: delete `mynetwork-allow-ssh`, SSH fails
- [ ] All checks green, End Lab

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

- [ ] Read M4 study guide
- [ ] Task 2: create VM `bloghost` (lab region and zone, `e2-standard-2`, Debian 12, Allow HTTP, startup script below), note its internal and external IP
- [ ] Task 3: in Cloud Shell create the bucket, copy the image, make it public (commands below)
- [ ] Task 4: start this early, it takes several minutes. Cloud SQL > MySQL > Enterprise, preset Sandbox, ID `blog-db`, password `Passw0rd1!`, same region and zone as `bloghost`, single zone, Security: allow unencrypted traffic
- [ ] Task 4: copy the SQL Public IP, add user `blogdbuser` / `Passw0rd1!`
- [ ] Task 4: Connections > Networking > Add network `web front end` = `BLOGHOST_EXTERNAL_IP/32`, Save
- [ ] Task 5: SSH to `bloghost`, write `index.php`, see "Database connection failed", then fill in the SQL IP and password, see "Connected successfully"
- [ ] Task 6: add the `<img src='...'>` line with the bucket's public URL above the `<h1>`, reload and see the banner
- [ ] All checks green, End Lab

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

### Lab 4: Hello Cloud Run (~45 min, Cloud Shell)

Theory: [M5](modules/M5_Containers_in_the_Cloud/M5_Containers_in_the_Cloud_v2.md), [M6](modules/M6_Applications_in_the_Cloud/M6_Applications_in_the_Cloud_v2.md). Manual: [labs/04_Hello_Cloud_Run.md](labs/04_Hello_Cloud_Run.md).

- [ ] Read M5 and M6 study guides
- [ ] Task 1: enable APIs, set region and `LOCATION`
- [ ] Task 2: create `helloworld/` with `package.json` and `index.js`
- [ ] Task 3: create Artifact Registry repo `my-repository`, configure Docker auth, Check my progress
- [ ] Task 4: write the `Dockerfile` (use the `FROM` image the lab page shows), build with Cloud Build, run locally, Web preview on 8080 shows "Hello World!", Check my progress
- [ ] Task 5: deploy to Cloud Run, open the Service URL, Check my progress
- [ ] Task 6: delete the image and the service
- [ ] All checks green, End Lab

Cloud Shell commands (replace `REGION` with the lab's region, for example `us-central1`):

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
gcloud config set compute/region REGION
LOCATION="REGION"
mkdir helloworld && cd helloworld
```

Create `package.json`, `index.js` and `Dockerfile` with `nano` using the content in the lab manual, then:

```bash
gcloud artifacts repositories create my-repository --repository-format=docker --location=$LOCATION --description="Docker repository"
gcloud auth configure-docker $LOCATION-docker.pkg.dev
gcloud builds submit --tag $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
docker run -d -p 8080:8080 $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
curl localhost:8080
gcloud run deploy helloworld --image $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld --allow-unauthenticated --region=$LOCATION
```

Clean up (Task 6):

```bash
gcloud artifacts docker images delete $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
gcloud run services delete helloworld --region=$LOCATION
```

### Prompt for the Gemini CLI agent

Paste this before running a lab's commands:

```text
I'm doing Google Cloud Skills Boost lab "<LAB NAME>" in Cloud Shell.
Lab region: <REGION>, zone: <ZONE>, project: <PROJECT_ID>.
Check these commands against labs/<LAB FILE>.md in this repo.
Replace placeholders with my values, flag anything that won't work in
Cloud Shell, and explain in one line what each command does.
Do not run anything yourself.

<PASTE COMMANDS>
```

## After the labs: ACE exam prep (22 Oct to early Dec)

Six weeks at 6 to 10 hours a week, following the four sections of the ACE exam guide. Section weights are approximate, from memory; confirm them on the [official exam guide](https://cloud.google.com/learn/certification/cloud-engineer).

| Week | Dates | Focus | Exam guide section |
| --- | --- | --- | --- |
| 1 | 22 to 28 Oct | Resource hierarchy, projects, billing, IAM basics, `gcloud config` | 1. Setting up a cloud solution environment (~23%) |
| 2 | 29 Oct to 4 Nov | Compute Engine, instance templates, managed instance groups, GKE basics, Cloud Run and Cloud Functions | 2. Planning and implementing (~30%) |
| 3 | 5 to 11 Nov | Storage classes and lifecycle, Cloud SQL, Spanner, Firestore, Bigtable, BigQuery; VPC, load balancers, Cloud DNS, VPN | 2. Planning and implementing |
| 4 | 12 to 18 Nov | Cloud Monitoring and Logging, snapshots and images, managing GKE and Cloud Run deployments | 3. Ensuring successful operation (~27%) |
| 5 | 19 to 25 Nov | IAM roles, service accounts, audit logs; first full practice exam | 4. Configuring access and security (~20%) |
| 6 | 26 Nov to early Dec | Practice exams, fix weak areas, book and sit the exam | All |

- [ ] Weekly: one hands-on Skills Boost lab from the ACE learning path
- [ ] Weekly: 20 practice questions, log every miss in the repo's `sessions/` folder
- [ ] Book the exam once two practice exams score 80% or more
