# Lab 4 Study Notes: M5 Containers and M6 Applications in the Cloud

Oct 19, 2026 · @Abdo

Containers, Kubernetes, GKE, Cloud Run and Cloud Run functions, condensed for Lab 4 and the ACE exam. The diagrams and the collapsible quiz answers live in the repo copy, study-notes/Lab4\_M5-M6\_Study\_Notes.md; this Doc carries the same text.

## What Lab 4 covers

Lab 4 puts a tiny web app on the internet without touching a server: you package it as a container image, store it in Artifact Registry, and have Cloud Run run it behind a public HTTPS URL. The flow is: your 3 files (package.json, index.js, Dockerfile) in Cloud Shell, then Cloud Build builds the image, then Artifact Registry stores it, then Cloud Run serves it at https://helloworld-...run.app.

Nothing from M5 and M6 is cut. Kubernetes and GKE are half of M5 and the lab never touches them, but the exam asks about them often; those parts say so. Where a point shows up in the lab, a note says which task.

> **Lessons that carry over:** from Lab 1, if a step fails with a permission error right after an API was enabled, wait a minute or two and retry. From Lab 3, Cloud Shell is a Google-run Linux machine already signed in as the lab user, and $GOOGLE\_CLOUD\_PROJECT already holds your project ID.

## What each service does

AWS comparisons only where you know the service: EC2 or Lambda.

| Service | Role it plays | Familiar? |
| --- | --- | --- |
| Artifact Registry | Private store for container images (and other packages). Cloud Run and GKE pull from it. Used in Lab 4 | A private Docker Hub in your project |
| Cloud Build | Builds your image on Google's machines from your Dockerfile and pushes it to the registry. Used in Lab 4 |  |
| Cloud Run | Runs a stateless container that answers web requests, scales to zero, bills per request time. No servers. Used in Lab 4 | Like Lambda, but for any container |
| Cloud Run functions | Runs one small function when an event happens (upload, message, HTTP call). You write the function, not a container | Lambda |
| GKE | Google-managed Kubernetes: orchestrates many containers across a cluster of VMs | EC2 machines with a container manager on top |
| Compute Engine | Plain VMs (Labs 1 to 3). GKE nodes are Compute Engine VMs | EC2 |

Key idea: M5 and M6 are one question asked five ways: how much of the machine do I want to manage? A VM: all of it. GKE: the containers and cluster rules. Cloud Run: only the container. Cloud Run functions: only a function.

## Part 1: Containers (M5)

### 1.1 Container vs virtual machine

A container is a box around your code and everything it needs (libraries, runtime), with a limited view of the file system and hardware. Many containers share the host's OS kernel; each VM carries a whole guest OS.

|  | Virtual machine | Container |
| --- | --- | --- |
| Contains | App, libraries and a full guest OS | App and libraries only |
| Start time | Minutes (OS must boot) | Seconds or less (starts like a process) |
| Size | GBs | Usually MBs |
| Portability | Tied to the VM image format | Code once, run anywhere: laptop, Cloud Shell, GKE, Cloud Run |
| Isolation | Strong (separate kernels) | Lighter (shared kernel) |
| Scales like | IaaS (you size the machines) | PaaS (add copies), with nearly IaaS flexibility |

Key idea: a container gives you the best of two worlds: it scales like a platform service yet keeps nearly the flexibility of infrastructure.

### 1.2 Image, container, Dockerfile and registry

| Word | What it is | Lab 4 example |
| --- | --- | --- |
| Dockerfile | Text recipe: start from this base, copy these files, run these commands, start with this command | The file from nano Dockerfile |
| Image | The finished read-only package built from the recipe. A template, not running | .../my-repository/helloworld in Artifact Registry |
| Container | A running instance of an image. Many can run from one image | The one docker run starts, and every instance Cloud Run starts |
| Registry | A store for images so other machines can pull them | Artifact Registry |

- Artifact Registry stores container images (format docker) and other packages (Maven, npm, Python, apt). It lives in a location, and an image path reads: LOCATION-docker.pkg.dev / PROJECT / REPOSITORY / IMAGE : TAG, for example us-central1-docker.pkg.dev/my-project-id/my-repository/helloworld:latest.
- The older Container Registry (gcr.io paths) has been replaced by Artifact Registry. If an exam question mentions gcr.io, treat it as the previous generation of the same idea.
- Cloud Build runs build steps, each in its own container, on Google's machines. With --tag it reads your Dockerfile, builds the image and pushes it in one command.
- Docker builds and runs images. In Lab 4 Cloud Shell has it preinstalled and you use it once, to test before deploying.
- Layers and caching: each Dockerfile instruction is a layer. Copying package.json and installing dependencies before copying the rest of the code means a code change doesn't reinstall everything.

Where you meet this in Lab 4: Task 3 creates the registry, Task 4 writes the Dockerfile and builds with Cloud Build.

### 1.3 Scaling with containers and microservices

- Scale one container: a web server in a container can be duplicated in seconds, dozens or hundreds of copies on one host.
- Microservices: real apps are several containers, each doing one job, connected over the network. Each is deployed and scaled independently across a group of hosts, which can come and go as demand changes or hosts fail.
- Running that group by hand (placing containers, restarting failed ones, rolling out versions) is orchestration, and Kubernetes does it.

## Part 2: Kubernetes

Not in Lab 4. You won't create a cluster or type kubectl. This part and Part 3 are exam material, the best place to lose marks by mixing up words.

### 2.1 The cluster: control plane and nodes

Kubernetes is an open-source platform for orchestrating many containers on many hosts: deploying, scaling, rollouts and rollbacks. It is a set of APIs to deploy containers onto a set of machines called a cluster. You describe what you want; Kubernetes works out how.

- Control plane: the brain. It holds the desired state and decides where things run. In GKE, Google runs it.
- Node: a machine that runs containers. In GKE every node is a Compute Engine VM.

### 2.2 Pods, Deployments and Services

| Object | What it is | Remember |
| --- | --- | --- |
| Pod | A wrapper around one or more containers, the smallest thing you deploy. Own IP and ports; containers inside share networking and storage | Usually one container per pod |
| Deployment | A group of replicas of the same pod. Keeps the right number running even when a node fails, and handles updates | I want 3 copies of this pod |
| Service | A stable fixed IP and name in front of a changing set of pods | Frontend pods talk to the backend Service, never to backend pods |
| Load balancer | For a Service of type LoadBalancer, GKE creates a Google Cloud network load balancer with a public IP that sends clients to a pod behind the Service | How the outside world reaches the cluster |

Service types: ClusterIP (default, inside the cluster only), NodePort (opens a port on each node), LoadBalancer (external IP through a Google load balancer). Key idea: pod IPs are not stable, which is exactly why Services exist.

### 2.3 Declarative config, scaling and rolling updates

- Imperative: commands one by one (expose, scale). Good for learning and quick tests.
- Declarative: a YAML configuration file states the desired state and Kubernetes makes it so. This is the recommended way. To change anything, edit the file and kubectl apply again.

| kubectl command | What it does |
| --- | --- |
| kubectl get pods | Lists the pods running in the cluster |
| kubectl get deployments / describe deployments | Shows each deployment and how many replicas are ready |
| kubectl get services | Lists Services, including the external IP to reach the app |
| kubectl scale deployment NAME --replicas=3 | Changes the number of pods now |
| kubectl apply -f FILE.yaml | Makes the cluster match the file. To go from 3 to 5 replicas, edit the file and apply |
| kubectl rollout ... | Starts, watches or undoes a rolling update |

- Autoscaling: a deployment can scale on a measure such as CPU utilization.
- Rolling update: replacing everything at once is risky, so new-version pods are created one at a time, each awaited before an old one is removed. No downtime, and you can roll back.

## Part 3: GKE

Google Kubernetes Engine is Google's managed Kubernetes. The cluster is built from Compute Engine instances, so it inherits Compute Engine and VPC features. GKE runs the control plane for you (you still get one API IP address) and, depending on the mode, the nodes too.

### 3.1 Autopilot vs Standard

|  | Autopilot (recommended) | Standard |
| --- | --- | --- |
| Who manages the nodes | GKE: node configuration, autoscaling, auto-upgrades, baseline security and networking | You configure, manage and optimize the cluster and nodes |
| What you think about | Your workloads | Node pools, machine types, sizing |
| Billing | By the CPU, memory and storage your pods request | By the nodes (VMs) you run, used or not |
| Fits | Most production work: strong security posture, less operations effort | When you need node-level control Autopilot doesn't give |

The course's rule: unless you need the control Standard offers, use Autopilot.

### 3.2 What GKE adds and how you create a cluster

- Google Cloud load balancing for Compute Engine instances.
- Node pools: subsets of nodes with the same configuration, so one cluster can hold different machine types.
- Automatic scaling of the node count, automatic upgrades of node software, node auto-repair.
- Logging and monitoring through Google Cloud Observability.

Create a cluster in the Console (Kubernetes Engine > Clusters > Create) or with one command: gcloud container clusters create-auto k1 --region $CLUSTER\_REGION. Reading it: gcloud container clusters is the GKE cluster group, create-auto creates an Autopilot one, k1 is the name, --region says where.

## Part 4: Cloud Run (M6)

### 4.1 What it is and the three-step workflow

Cloud Run is a managed compute platform that runs stateless containers that answer web requests (or Pub/Sub events). It is serverless: no infrastructure to manage. It is built on Knative, an open API and runtime on top of Kubernetes, so the same workloads can run on GKE or anywhere Knative runs.

Workflow: 1. Write the code (a server that listens for web requests). 2. Build and package it into a container image. 3. Deploy the image from Artifact Registry to Cloud Run. You get a unique HTTPS URL back.

The container contract. Your container must:

- Be a Linux 64-bit program (any language: Java, Python, Node.js, PHP, Go, C++, even Cobol or Perl) that starts an HTTP server.
- Listen on the port in the PORT environment variable (default 8080), on all interfaces.
- Be stateless: any instance can be created or destroyed at any moment and instances don't share a disk. Anything that must survive goes to Cloud Storage, a database or similar.

Where you meet this in Lab 4: index.js reads process.env.PORT (falls back to 8080). That is the contract.

### 4.2 Revisions, traffic, scaling and limits

- Service and revision: a service is the named thing with a URL (helloworld). Every deploy creates a new immutable revision (helloworld-00001-xit). The service sends traffic to one or more revisions.
- Traffic splitting: send percentages to different revisions (90/10 canary), or roll back by sending 100% to the previous revision.
- Autoscaling: adds instances as requests arrive and scales down to zero when idle. Minimum instances keep some warm (no cold start, but costs money while idle); maximum instances cap scale and cost.
- Concurrency: one instance handles many requests at once (default 80, up to 1000).
- Resources and limits: you choose CPU and memory per instance (the course quotes up to 4 vCPU and 8 GB; limits have grown since, check current docs). Request timeout defaults to 5 minutes, configurable up to 60.
- Configuration at deploy time: environment variables (--set-env-vars NAME=Abdo would make the lab app say Hello Abdo!) and secrets from Secret Manager.

### 4.3 Billing

- You pay for CPU and memory only while a container handles requests, plus while it starts up and shuts down, in 100 ms steps. With no request in flight you pay nothing for compute.
- A small fee per million requests applies, with a free tier for light use.
- A bigger instance costs more per second.
- Compute Engine and most other compute bills while running, even idle. That is the key difference.
- Exceptions to nothing when idle: minimum instances, and the instance-based billing option (CPU always allocated).
- The stored image in Artifact Registry costs storage. That is why the lab's last task deletes it.

### 4.4 Access: who can call your service

- A new service is private by default: callers need the IAM role Cloud Run Invoker (roles/run.invoker).
- --allow-unauthenticated (Allow public access in the Console) grants that role to allUsers, making the service public. The lab does this so you can open the URL.
- For a private service a caller sends an identity token (gcloud auth print-identity-token prints one) in an Authorization: Bearer header.
- The ingress setting controls where requests may come from (anywhere, internal only, internal plus load balancer).
- The service runs as a service account (by default the Compute Engine default one). Give it only the roles the app needs.
- To deploy you need Cloud Run admin rights and permission to act as the runtime service account.

### 4.5 Source-based deploys and Cloud Run jobs

- Container-based workflow (the lab): you write the Dockerfile and build the image. Full transparency and flexibility.
- Source-based workflow: you deploy source code and Cloud Run builds the container using Buildpacks (open source), so the image is secure, well-configured and consistent. In the CLI: gcloud run deploy --source .
- Cloud Run jobs run a container to completion (a batch task) rather than serving requests.

## Part 5: Cloud Run functions

Many apps have event-driven parts, such as an image upload that should create thumbnails and save them. Coding that into the app means providing compute for it whether it happens every millisecond or once a day.

Cloud Run functions (the newer name for Cloud Functions) is a lightweight, event-based, asynchronous compute solution:

- You write a small single-purpose function. No server, runtime or container to manage.
- Billed to the nearest 100 ms, only while your code runs.
- Languages: Node.js, Python, Go, Java, .NET Core, Ruby, PHP.
- Triggers: events from Cloud Storage and Pub/Sub run it asynchronously, or you call it by HTTP for synchronous use. Not HTTP only: a quiz favourite.
- Integrated with Cloud Logging and Monitoring; used to connect and extend other cloud services.

|  | Cloud Run | Cloud Run functions |
| --- | --- | --- |
| You provide | A container (or source for buildpacks) | A single function |
| Best for | A whole web app or API, any language or binary | One small reaction to an event: thumbnail on upload, email on a new file |
| Triggered by | HTTP requests (and Pub/Sub events) | Events (Cloud Storage, Pub/Sub) or HTTP |
| Familiar | Like a web server | Lambda |

## Part 6: Which compute do I pick?

Ordered from most control to least to manage:

| Service | You manage | Pick it when the question says... |
| --- | --- | --- |
| Compute Engine | The whole VM: OS, patches, software, scaling | Lift-and-shift, a specific OS or kernel, license or hardware needs, full control (Labs 1 to 3) |
| GKE | Containers and cluster rules (Autopilot also hands you the nodes) | Many containers, microservices, you want the Kubernetes API or portability, long-running or stateful work |
| App Engine | Just your source code | A web app on a managed platform, no containers needed |
| Cloud Run | Just one container | A stateless HTTP service, scale to zero, pay per request, no cluster |
| Cloud Run functions | Just a function | Small event-driven code: react to a file upload or a Pub/Sub message |

| The question says... | Think |
| --- | --- |
| Kubernetes, orchestrate, pods, multi-container | GKE |
| stateless container, scale to zero, pay only when handling requests | Cloud Run |
| when a file is uploaded, on a message, single-purpose, respond to an event | Cloud Run functions |
| I need to install a custom OS or driver | Compute Engine |
| no clusters or servers to manage | Cloud Run (or functions) |

## Part 7: The lab's shortcuts vs how you'd do it properly

| In the lab | Why it's a shortcut | The proper way |
| --- | --- | --- |
| --allow-unauthenticated | The URL is open to the entire internet | Only for public sites. Otherwise keep the service private and grant roles/run.invoker to the callers that need it |
| No tag on the image | It gets the latest tag, which changes under you | Tag images with a version or commit (:v1) so deploys are repeatable and rollbackable |
| Runs as the default Compute Engine service account | That account is broadly privileged | A dedicated service account with only the roles the app needs |
| Settings as plain environment variables | Fine for NAME, not for passwords | Secret Manager for secrets |
| docker run -d leaves a container running in Cloud Shell | A leftover test container | docker ps to find it, docker stop ID to end it (harmless, Cloud Shell resets eventually) |
| The image stays in Artifact Registry | It costs storage until deleted | Delete it (Task 6), or set a cleanup policy on the repository |

## Part 8: Self-check quiz

Q1 to Q5 are the course's own module quizzes. Choice questions are lettered. Answers follow the questions; try them first.

1. What is a Kubernetes pod? A. A group of clusters B. A group of nodes C. A group of VMs D. A group of containers
2. Where do the resources used to build GKE clusters come from? A. Compute Engine B. App Engine C. Bare-metal servers D. Cloud Storage
3. Which scenario suits Cloud Run rather than Cloud Run functions? A. Email whenever a new document lands in a Cloud Storage folder B. Hosting a dynamic web app where users upload and share photos C. Resizing images on demand through a web interface D. Generating thumbnails for images uploaded to a bucket
4. Which three statements about Cloud Run functions are correct? A. A scalable functions-as-a-service platform B. Can be used to extend Cloud services C. Requires servers or VMs to be provisioned D. Integrated with Cloud Logging E. Can only be invoked by HTTP requests
5. Why would a customer choose Cloud Run functions? A. Event-driven code they don't want to provision compute for B. Primary way to run C++ applications C. It is a free service D. To split a legacy monolith into microservices
6. A container starts in about a second and a VM takes minutes. Why?
7. You wrote a Dockerfile and ran a build. What did you produce, and what is a running copy called? A. A container; a running copy is an image B. An image; a running copy is a container C. A registry; a running copy is a repository D. A pod; a running copy is a node
8. Where do you store the images Cloud Run and GKE will pull? A. Cloud Storage Archive class B. Cloud SQL C. Artifact Registry D. Persistent Disk
9. Which port must a Cloud Run container listen on? A. Always 80 B. The port in the PORT environment variable (default 8080) C. Any port, Cloud Run scans for it D. Only 443
10. A Cloud Run service gets no traffic for a day. What do you pay for compute, with default settings? A. The same as when busy B. Half C. Nothing D. A flat hourly fee for one VM
11. A new revision has a bug. Quickest safe fix on Cloud Run? A. Delete the project B. Send 100% of traffic back to the previous revision C. Recreate the Artifact Registry repository D. Resize the instance
12. Which is true of GKE Autopilot vs Standard? A. You manage the nodes in Autopilot B. GKE manages the nodes in Autopilot and you are billed for the resources your pods request C. Autopilot has no control plane D. Autopilot needs no containers
13. Pod IPs change every time pods are recreated. What gives other pods a stable address? A. A Deployment B. A Node pool C. A Service D. A Namespace
14. You need 3 replicas, then 5 later, reproducible and reviewable in version control. What do you use? A. Manual kubectl scale commands B. A declarative Deployment config file re-applied with kubectl apply C. Editing pods by hand in the Console D. Recreating the cluster
15. Pick the service for each: (1) a stateless HTTP API that should scale to zero; (2) a multi-service app that needs Kubernetes; (3) a custom OS with a kernel module; (4) resize a photo when it lands in a bucket. A. 1 Cloud Run, 2 GKE, 3 Compute Engine, 4 Cloud Run functions B. 1 GKE, 2 Cloud Run, 3 Cloud Run functions, 4 Compute Engine C. 1 Compute Engine, 2 Cloud Run, 3 GKE, 4 Cloud Run D. 1 Cloud Run functions, 2 Compute Engine, 3 GKE, 4 Cloud Run
16. In Lab 4, what does --allow-unauthenticated do? A. Disables HTTPS B. Grants the Cloud Run Invoker role to allUsers, making the service public C. Skips the build D. Lets the service write to Cloud Storage
17. Your Cloud Run app saves uploads to the container's local disk. What happens? A. Safe forever B. Lost when the instance is replaced or scaled to zero; use Cloud Storage or a database C. Cloud Run backs them up daily D. Shared across instances
18. What can trigger a Cloud Run function? A. Only HTTP requests B. Only Cloud Storage events C. HTTP requests and events such as Cloud Storage and Pub/Sub D. Only a cron schedule
19. After Task 6 (image and service deleted), what is still in your project? A. Nothing from the lab B. The empty my-repository repository and the source bucket Cloud Build created C. The running container D. The Cloud Run service
20. You ran gcloud config set compute/region in Task 1, yet gcloud run deploy still gets --region=$LOCATION. Why?

### Answers

1. D. A pod is one or more containers deployed together; the simplest workload is a pod with one container.
2. A. GKE nodes are Compute Engine VMs, so GKE uses Compute Engine's and VPC's capabilities.
3. B. A whole web app fits a container on Cloud Run. A, C and D are single-purpose event-driven jobs for functions.
4. A, B and D. C is wrong (serverless). E is wrong: functions are triggered by HTTP or by events.
5. A. Functions run only when the event happens and bill only while the code runs. Splitting a monolith points to containers.
6. A container doesn't boot an OS. It shares the host kernel and starts like a process; a VM boots a full guest OS.
7. B. The Dockerfile is the recipe, the build produces an image (read-only template), and each running copy is a container.
8. C. Artifact Registry replaced the older Container Registry.
9. B. Cloud Run tells your container the port through PORT; Cloud Run handles HTTPS at the URL.
10. C. It scales to zero and bills only while requests are handled (plus start-up and shutdown), in 100 ms steps. Minimum instances or instance-based billing would change that.
11. B. Revisions are immutable, so the old one is still there. Traffic splitting also allows canaries.
12. B. In Autopilot GKE handles node configuration, scaling, upgrades and baseline security. In Standard you manage and pay for nodes.
13. C. A Service is a stable IP and name in front of changing pods. A Deployment keeps the count right but gives no stable address.
14. B. Declarative config states the desired state in a file; change replicas and apply again.
15. A. Follow the clue words in Part 6.
16. B. Without it the deploy asks, or the URL answers 403 Forbidden to anyone without the Invoker role.
17. B. Cloud Run containers must be stateless; local disk is temporary and per instance.
18. C. Events run it asynchronously, HTTP gives synchronous use.
19. B. Task 6 deletes the image and the service, not the repository. End Lab deletes the lab project; in a real project you'd remove those too.
20. compute/region is the default for Compute Engine commands. gcloud run has its own setting (run/region), so it needs the region on the command line unless you set that property too.

## Part 9: Bridge to Lab 4: Hello Cloud Run

About 45 minutes, almost all in Cloud Shell. Your recorded walkthrough shows the steps; use these notes for the why and for what to do when a step goes wrong.

### 9.1 The big picture

1. Write a tiny web app (3 files) that answers Hello World!.
2. Package it: the Dockerfile describes the box, Cloud Build builds it and Artifact Registry keeps it.
3. Test it in Cloud Shell with Docker, so you know the box works before shipping.
4. Deploy the same box to Cloud Run and open the HTTPS URL.

Then clean up so nothing keeps costing money. The point is the Cloud Run workflow end to end, with no server ever created.

### 9.2 What each step teaches

| In the lab you... | The theory behind it |
| --- | --- |
| Enable run.googleapis.com and artifactregistry.googleapis.com | Services are switched on per project first (Lab 1 lesson: wait a minute if a permission error follows) |
| Create package.json and index.js | Workflow step 1: a server that listens on PORT |
| Create the Artifact Registry repository my-repository (format Docker) | Where the image will live |
| gcloud auth configure-docker | Lets Docker in Cloud Shell sign in to Artifact Registry to pull your image |
| Write the Dockerfile | The recipe for the image |
| gcloud builds submit --tag ... | Cloud Build builds and pushes the image: workflow step 2 |
| docker run -d -p 8080:8080 ... and Web preview | Test the container locally before deploying |
| gcloud run deploy ... --allow-unauthenticated | Workflow step 3: Cloud Run creates a service and the first revision, and makes it public |
| Delete the image and the service | Avoid storage charges; Cloud Run itself is free when idle |

### 9.3 The three files, line by line

package.json tells Node what the project is and how to start it.

| Part | What it means |
| --- | --- |
| name, description, version, author, license | Labels. Not used to run it |
| main: index.js | The main file |
| scripts: start: node index.js | The important one. npm start runs node index.js. The Dockerfile's last line calls it |
| dependencies: express ^4.17.1 | The one library needed, Express (a web framework). ^4.17.1 means 4.17.1 or any later 4.x |

index.js is the whole app.

| Line | What it means |
| --- | --- |
| const express = require('express'); const app = express(); | Load Express and create the app |
| const port = process.env.PORT or 8080 | Use the PORT environment variable, or 8080 if unset. The Cloud Run contract |
| app.get('/', ...) | When someone requests the home page, run this function |
| const name = process.env.NAME or 'World'; res.send Hello name | Say Hello plus an environment variable NAME, or World. Deploying with --set-env-vars NAME=Abdo changes the greeting without touching code |
| app.listen(port, ...) | Start the web server on that port and log a line |

Dockerfile is the recipe (the lab page prints the exact FROM image; the manual file shows only a placeholder).

| Line | What it means |
| --- | --- |
| FROM node image | Start from an official lightweight Node.js image: Linux plus Node preinstalled |
| WORKDIR /usr/src/app | Create this folder in the image and work from it |
| COPY package\*.json ./ | Copy package.json (and a lock file if any). Done first on purpose so the next step can be cached |
| RUN npm install --only=production | Install the dependencies (Express) inside the image. RUN happens at build time |
| COPY . ./ | Copy the rest of your files (index.js) in |
| CMD npm start | What the container does when it starts at run time: npm start, which runs node index.js |

### 9.4 Checklist

- [ ] Read this section and watch the walkthrough video
- [ ] Start the lab, open the console in an incognito window with the lab student account, open Cloud Shell
- [ ] Task 1: enable the Cloud Run and Artifact Registry APIs, approve the authorization prompt if asked
- [ ] Task 1: gcloud config set compute/region with the lab's region, then LOCATION= the same region
- [ ] Task 2: mkdir helloworld && cd helloworld, then create package.json and index.js with nano (paste, then CTRL+X, Y, Enter)
- [ ] Task 3: create the Docker repository my-repository in your region, then gcloud auth configure-docker with the LOCATION-docker.pkg.dev host (answer Y), Check my progress
- [ ] Task 4: create the Dockerfile (use the FROM image the lab page shows), save
- [ ] Task 4: gcloud builds submit --tag ... from inside helloworld, wait for SUCCESS (say yes if asked to enable Cloud Build)
- [ ] Task 4: docker run -d -p 8080:8080 ..., then Web preview on port 8080 shows Hello World!, Check my progress
- [ ] Task 5: gcloud run deploy helloworld ..., answer Y to enabling APIs, open the Service URL, check the Cloud Run page, Check my progress
- [ ] Task 6: delete the image (Y), then the service (Y)
- [ ] All checks green, End Lab

### 9.5 Expected results and fixes

| Moment | You should see | If not |
| --- | --- | --- |
| Enabling the APIs | Operation ... finished successfully | A permission error right after: wait a minute, retry |
| Build log, npm install step | Lines about installing Express | An npm WARN or deprecation notice is only a warning (--only=production is an older flag spelling); the build still succeeds |
| Creating the repository | No error; it appears in Artifact Registry | already exists: fine. Permission denied right after enabling the API: wait and retry |
| gcloud builds submit | Build output ending in SUCCESS and the image name | Dockerfile not found: you are not in helloworld, or the file name is wrong (capital D, no extension). Repository not found: the name or region in the path doesn't match what you created |
| docker run -d ... | A long container ID and nothing else | Unauthorized: rerun gcloud auth configure-docker. It runs in the background, so the prompt returns at once |
| Web preview on 8080 | A page saying Hello World! | Choose port 8080, not the default. Or curl localhost:8080 |
| gcloud run deploy | Service \[helloworld\] revision \[helloworld-00001-...\] has been deployed and is serving 100 percent of traffic, and a Service URL | If asked to allow unauthenticated invocations, answer y. If asked to enable an API, answer Y |
| Opening the Service URL | Hello World! over HTTPS | 403 Forbidden: not public, redeploy with --allow-unauthenticated. Service Unavailable right after deploy: wait a few seconds and reload |
| Cleanup | Image and service gone | Prompts need Y and Enter. Deleting the service needs the same --region you deployed to |

Tip: if a Check my progress fails, read which objective it names (repository, image, service) and look at that resource in the Console. Most fails are a region mismatch between steps.

### 9.6 The commands, explained, and the Console route

Reading a command: gcloud (the tool), a group (run, artifacts, builds), a noun, a verb, then the target and --flags. gcloud run deploy helloworld reads: tool, Cloud Run, deploy, the service named helloworld. In the image path, Cloud Shell presets two shell variables: the project ID variable (GOOGLE\_CLOUD\_PROJECT) and the LOCATION variable you set in Task 1.

| Command piece | What it means | Console equivalent |
| --- | --- | --- |
| gcloud services enable run.googleapis.com artifactregistry.googleapis.com | Switches on the two APIs in the project | APIs & Services > Library > search each > Enable |
| gcloud config set compute/region REGION | Default region for Compute Engine commands. Cloud Run commands don't read it | Not applicable |
| LOCATION="REGION" | Saves the region in a variable so later commands can reuse it | Not applicable |
| mkdir helloworld && cd helloworld | mkdir makes a folder, && means and then if that worked, cd moves into it | Not applicable |
| nano package.json | nano is a small terminal text editor. CTRL+X, Y, Enter saves and quits | Cloud Shell Open Editor button |
| gcloud artifacts repositories create my-repository | Creates a repository named my-repository | Artifact Registry > Create repository |
| --repository-format=docker | This repository holds container images | The Format dropdown |
| --location | Region of the repository | The Region dropdown |
| gcloud auth configure-docker (LOCATION)-docker.pkg.dev | Edits Docker's config to use your Google credentials for that registry host. Needed because docker run must pull the image | Not applicable |
| gcloud builds submit --tag IMAGE | Zips the current folder, sends it to Cloud Build, which follows the Dockerfile and pushes the result as IMAGE. Run it from the folder with the Dockerfile | Possible from the Console, but simplest as a command |
| LOCATION-docker.pkg.dev/PROJECT/my-repository/helloworld | The image path: region host, project ID, repository, image name. No tag, so latest | Shown on the image in Artifact Registry |
| docker run -d -p 8080:8080 IMAGE | Starts a container from the image. -d runs it in the background. -p 8080:8080 connects Cloud Shell port 8080 to port 8080 in the container | Not applicable |
| Web preview > Preview on port 8080 | Cloud Shell opens a browser tab to its own port 8080 | The Web preview button in the Cloud Shell toolbar |
| gcloud run deploy helloworld | Creates (or updates) a Cloud Run service named helloworld | Cloud Run > Create service |
| --image IMAGE | Which image to run | Deploy one revision from an existing container image > Select |
| --allow-unauthenticated | Makes the service public | Authentication: Allow public access |
| --region | Where the service runs | The Region dropdown |
| gcloud artifacts docker images delete IMAGE | Deletes the image from the registry; asks to confirm | Artifact Registry > repository > the image > Delete |
| gcloud run services delete helloworld --region=... | Deletes the Cloud Run service; asks to confirm | Cloud Run > tick the service > Delete |

The exact commands with variables are in the repo copy of these notes and in the lab manual.

Console route for the deploy: Cloud Run > Create service > Deploy one revision from an existing container image > Select > Artifact Registry > my-repository > helloworld > service name helloworld > Region > Authentication Allow public access > Create.

Optional checks, only if something looks wrong:

| Command | What it does |
| --- | --- |
| gcloud run services list | Lists your services, regions and URLs. Console: the Cloud Run page |
| gcloud artifacts docker images list REPOSITORY\_PATH | Lists images in the repository. Console: Artifact Registry |
| docker ps | Lists running containers on Cloud Shell with their IDs |
| docker stop CONTAINER\_ID | Stops the test container from docker run |
| curl localhost:8080 | Fetches the page from Cloud Shell's own port 8080 and prints it as text |
