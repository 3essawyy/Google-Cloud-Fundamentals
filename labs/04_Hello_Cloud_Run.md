# Lab 4: Hello Cloud Run

> **Progression Rank:** 4 of 4 (Medium / Hard)
> **Estimated Time:** 45 Minutes · **Target Track:** Module 5 & 6: Containers & Applications in the Cloud
> **Role Trajectory:** Google Cloud Associate Cloud Engineer (ACE)

---

## ⚡ Cloud Shell Quick-Reference Script
*Consolidated CLI commands ready for pasting into Google Cloud Shell:*

```bash
#!/usr/bin/env bash
# Lab 4: Hello Cloud Run - Quick Execution Script
set -euo pipefail

# Step Command block 1
gcloud auth list

# Step Command block 2
Credentialed accounts:
 - @.com (active)

# Step Command block 3
Credentialed accounts:
 - google1623327_student@qwiklabs.net

# Step Command block 4
gcloud config list project

# Step Command block 5
[core]
project =

# Step Command block 6
[core]
project = qwiklabs-gcp-44776a13dea667a6

# Step Command block 7
gcloud services enable run.googleapis.com artifactregistry.googleapis.com

# Step Command block 8
Operation "operations/acf.cc11852d-40af-47ad-9d59-477a12847c9e" finished successfully.

# Step Command block 9
gcloud config set compute/region {{{project_0.default_region | "REGION"}}}

# Step Command block 10
LOCATION="{{{project_0.default_region | Region}}}"

# Step Command block 11
mkdir helloworld && cd helloworld

# Step Command block 12
nano package.json

# Step Command block 13
nano index.js

# Step Command block 14
const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  const name = process.env.NAME || 'World';
  res.send(`Hello ${name}!`);
});

app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});

# Step Command block 15
gcloud artifacts repositories create my-repository \
    --repository-format=docker \
    --location=$LOCATION \
    --description="Docker repository"

# Step Command block 16
gcloud auth configure-docker $LOCATION-docker.pkg.dev

# Step Command block 17
nano Dockerfile

# Step Command block 18
# Use the official lightweight Node.js image.
# https://hub.docker.com/_/node
FROM {{{project_0.startup_script.node_docker_image | node_docker_image}}}

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
# Copying this first prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# If you add a package-lock.json, speed your build by switching to 'npm ci'.
# RUN npm ci --only=production
RUN npm install --only=production

# Copy local code to the container image.
COPY . ./

# Run the web service on container startup.
CMD [ "npm", "start" ]

# Step Command block 19
gcloud builds submit --tag $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld

# Step Command block 20
docker run -d -p 8080:8080 $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld

# Step Command block 21
gcloud run deploy helloworld \
    --image $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld \
    --allow-unauthenticated \
    --region=$LOCATION

# Step Command block 22
Service [helloworld] revision [helloworld-00001-xit] has been deployed
and is serving 100 percent of traffic.

Service URL: https://helloworld-h6cp412q3a-uc.a.run.app

# Step Command block 23
gcloud artifacts docker images delete $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld

# Step Command block 24
gcloud run services delete helloworld --region={{{project_0.default_region | "REGION"}}}

```

---

## 📖 Lab Instructions & Walkthrough


## Overview

Cloud Runis a managed compute platform that enables you to run stateless containers that are invocable via HTTP requests. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most — building great applications.

The goal of this lab is for you to build a simple containerized application image and deploy it to Cloud Run.

### Objectives

In this lab, you learn to:

* Enable the Cloud Run and Artifact Registry APIs.
* Create a simple Node.js application that can be deployed as a serverless, stateless container.
* Create an Artifact Registry repository.
* Containerize your application and upload it to Artifact Registry.
* Deploy a containerized application on Cloud Run.
* Delete unneeded images to avoid incurring extra storage charges.

## Setup and requirements

For each lab, you get a new Google Cloud project and set of resources for a fixed time at no cost.

1. Click theStart Labbutton. If you need to pay for the lab, a pop-up opens for you to select your payment method.
On the right is theLab setup and accesspanel with the following:TheOpen Google Cloud consolebuttonThe temporary credentials (username and password) that you must use for this labOther information, if needed, to step through this labNote that the lab timer is located near the top of the page, showing the remaining time.
2. ClickOpen Google Cloud console(or right-click and selectOpen Link in Incognito Windowif you are running the Chrome browser).The lab spins up resources, and then opens another tab that shows theSign inpage.Tip:Arrange the tabs in separate windows, side-by-side.Note:If you see theChoose an accountdialog, clickUse Another Account.
3. If necessary, copy theUsernamebelow and paste it into theSign indialog.{{{user_0.username | "Username"}}}You can also find theUsernamein theLab setup and accesspanel.
4. ClickNext.
5. Copy thePasswordbelow and paste it into theWelcomedialog.{{{user_0.password | "Password"}}}You can also find thePasswordin theLab setup and accesspanel.
6. ClickNext.Important:You must use the credentials the lab provides you. Do not use your Google Cloud account credentials.Note:Using your own Google Cloud account for this lab may incur extra charges.
7. Click through the subsequent pages:Accept the terms and conditions.Do not add recovery options or two-factor authentication (because this is a temporary account).Do not sign up for free trials.

After a few moments, the Google Cloud console opens in this tab.

> ℹ️ **Note:**
> Note:To view a menu with a list of Google Cloud products and services, click theNavigation menuat the top-left, or type the service or product name in theSearchfield.

### Activate Google Cloud Shell

Google Cloud Shell is a virtual machine that is loaded with development tools. It offers a persistent 5GB home directory and runs on the Google Cloud.

Google Cloud Shell provides command-line access to your Google Cloud resources.

1. In Cloud console, on the top right toolbar, click the Open Cloud Shell button.
2. ClickContinue.

It takes a few moments to provision and connect to the environment. When you are connected, you are already authenticated, and the project is set to yourPROJECT_ID. For example:

gcloudis the command-line tool for Google Cloud. It comes pre-installed on Cloud Shell and supports tab-completion.

* You can list the active account name with this command:

```bash
gcloud auth list
```

Output:

```bash
Credentialed accounts:
 - @.com (active)
```

Example output:

```bash
Credentialed accounts:
 - google1623327_student@qwiklabs.net
```

* You can list the project ID with this command:

```bash
gcloud config list project
```

Output:

```bash
[core]
project =
```

Example output:

```bash
[core]
project = qwiklabs-gcp-44776a13dea667a6
```

> ℹ️ **Note:**
> Note:Full documentation ofgcloudis available in thegcloud CLI overview guide.

### Reference

### Basic Linux Commands

Below you will find a reference list of a few very basic Linux commands which may be included in the instructions or code blocks for this lab.

| Command --> | Action | . | Command --> | Action |
| --- | --- | --- | --- | --- |
| mkdir(make directory) | create a new folder | . | cd(change directory) | change location to another folder |
| ls(list) | list files and folders in the directory | . | cat(concatenate) | read contents of a file without using an editor |
| apt-get update | update package manager library | . | ping | signal to test reachability of a host |
| mv(move) | moves a file | . | cp(copy) | makes a file copy |
| pwd(present working directory) | returns your current location | . | sudo(super user do) | gives higher administration privileges |

## Task 1. Enable the Cloud Run API and configure your Shell environment

In this task, you enable the necessary APIs and set up environment variables to simplify your commands.

1. From Cloud Shell, enable theCloud Run APIandArtifact Registry API. This allows your project to accept requests for these services:

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

1. If you are asked to authorize the use of your credentials, do so.  You should then see a successful message similar to this one:

```bash
Operation "operations/acf.cc11852d-40af-47ad-9d59-477a12847c9e" finished successfully.
```

> ℹ️ **Note:**
> Note:You can also enable the API using theAPIs & Servicessection of the Google Cloud console.

1. Set the compute region:

```bash
gcloud config set compute/region {{{project_0.default_region | "REGION"}}}
```

1. Create a LOCATION environment variable:

```bash
LOCATION="{{{project_0.default_region | Region}}}"
```

## Task 2. Write the sample application

In this task, you will build a simple express-based NodeJS application which responds to HTTP requests.

1. In Cloud Shell create a new directory namedhelloworld, then move your view into that directory:

```bash
mkdir helloworld && cd helloworld
```

1. Next you'll be creating and editing files. To edit files, usenanoor the Cloud Shell Code Editor by clicking on theOpen Editorbutton in Cloud Shell.
2. Create apackage.jsonfile, then add the following content to it:

```bash
nano package.json
```

```bash
{
  "name": "helloworld",
  "description": "Simple hello world sample in Node",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "author": "Google LLC",
  "license": "Apache-2.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

Most importantly, the file above contains a start script command and a dependency on the Express web application framework.

1. PressCTRL+X, thenY, thenEnterto save thepackage.jsonfile.
2. Next, in the same directory, create anindex.jsfile, and copy the following lines into it:

```bash
nano index.js
```

```bash
const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  const name = process.env.NAME || 'World';
  res.send(`Hello ${name}!`);
});

app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});
```

This code creates a basic web server that listens on the port defined by thePORTenvironment variable. Your app is now finished and ready to be containerized and uploaded to Artifact Registry.

1. PressCTRL+X, thenY, thenEnterto save theindex.jsfile

> ℹ️ **Note:**
> Note:You can use many other languages to get started with Cloud Run. You can find instructions for Go, Python, Java, PHP, Ruby, Shell scripts, and others from theQuickstarts guide.

## Task 3. Create an Artifact Registry repository

In this task, you create a repository in Artifact Registry. This repository will act as the storage location for your container images, allowing Google Cloud services to access and pull them.

1. Create a new Docker repository namedmy-repositoryin your region:

```bash
gcloud artifacts repositories create my-repository \
    --repository-format=docker \
    --location=$LOCATION \
    --description="Docker repository"
```

1. Configure Docker to authenticate requests for Artifact Registry in your region:

```bash
gcloud auth configure-docker $LOCATION-docker.pkg.dev
```

ClickCheck my progressto verify the objective.Create an Artifact Registry repository

## Task 4. Containerize your app and upload it to Artifact Registry

In this task, you containerize your sample application and push the image to Artifact Registry.

1. To containerize the sample app, create a new file namedDockerfilein the same directory as the source files. This file acts as a recipe, instructing Docker how to build your image:

```bash
nano Dockerfile
```

```bash
# Use the official lightweight Node.js image.
# https://hub.docker.com/_/node
FROM {{{project_0.startup_script.node_docker_image | node_docker_image}}}

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
# Copying this first prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# If you add a package-lock.json, speed your build by switching to 'npm ci'.
# RUN npm ci --only=production
RUN npm install --only=production

# Copy local code to the container image.
COPY . ./

# Run the web service on container startup.
CMD [ "npm", "start" ]
```

1. PressCTRL+X, thenY, thenEnterto save theDockerfilefile.
2. Now, build your container image using Cloud Build by running the following command from the directory containing theDockerfile. (Note the $GOOGLE_CLOUD_PROJECT environmental variable in the command, which contains your lab's Project ID):

```bash
gcloud builds submit --tag $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
```

Cloud Build is a service that executes your builds on Google Cloud. It executes a series of build steps, where each build step is run in a Docker container to produce your application container (or other artifacts) and push it to Artifact Registry, all in one command.

Once pushed to the registry, you will see a SUCCESS message containing the image name. The image is stored in Artifact Registry and can be re-used if desired.

1. To run and test the application locally from Cloud Shell, start it using this standarddockercommand:

```bash
docker run -d -p 8080:8080 $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
```

1. In the Cloud Shell window, click onWeb previewand selectPreview on port 8080.

This should open a browser window showing the "Hello World!" message. You could also simply usecurl localhost:8080.

ClickCheck my progressto verify the objective.Containerize your app and upload it to Artifact Registry

## Task 5.  Deploy to Cloud Run

In this task, you deploy your containerized application to Cloud Run. This process spins up a service that can respond to web requests via a secure HTTPS URL.

1. Deploy your containerized application to Cloud Run using the following command:

```bash
gcloud run deploy helloworld \
    --image $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld \
    --allow-unauthenticated \
    --region=$LOCATION
```

The allow-unauthenticated flag in the command above makes your service publicly accessible.

1. If prompted to enable APIs, typeY.

Wait a few moments until the deployment is complete. On success, the command line displays the service URL:

```bash
Service [helloworld] revision [helloworld-00001-xit] has been deployed
and is serving 100 percent of traffic.

Service URL: https://helloworld-h6cp412q3a-uc.a.run.app
```

You can now visit your deployed container by opening the service URL in any browser window.

Congratulations!You have just deployed an application packaged in a container image to Cloud Run. Cloud Run automatically and horizontally scales your container image to handle the received requests, then scales down when demand decreases. In your own environment, you only pay for the CPU, memory, and networking consumed during request handling.

For this lab you used thegcloudcommand-line. Cloud Run is also available via Cloud console.

1. In the Google Cloud console, on theNavigation menu(), clickCloud Runand you should see yourhelloworldservice listed:

ClickCheck my progressto verify the objective.Deploy a containerized application on Cloud Run

## Task 6. Clean up

In this task, you delete the deployed service and the container image to avoid incurring charges.

While Cloud Run does not charge when the service is not in use, you might still be charged for storing the built container image.

1. You can delete yourhelloworldimage using the following command:

```bash
gcloud artifacts docker images delete $LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/my-repository/helloworld
```

1. When prompted to continue typeY, and pressEnter.
2. To delete the Cloud Run service, use this command :

```bash
gcloud run services delete helloworld --region={{{project_0.default_region | "REGION"}}}
```

1. When prompted to continue typeY, and pressEnter.

## End your lab

When you have completed your lab, clickEnd Lab. Google Skills removes the resources you’ve used and cleans the account for you.

You will be given an opportunity to rate the lab experience. Select the applicable number of stars, type a comment, and then clickSubmit.

The number of stars indicates the following:

* 1 star = Very dissatisfied
* 2 stars = Dissatisfied
* 3 stars = Neutral
* 4 stars = Satisfied
* 5 stars = Very satisfied

You can close the dialog box if you don't want to provide feedback.

For feedback, suggestions, or corrections, please use theSupporttab.

## Congratulations!

You have completed this lab!

### Next steps / learn more

For more information on building a stateless HTTP container suitable for Cloud Run from code source and pushing it to Artifact Registry, view:

* Developing Cloud Run services
* Building Containers

Copyright 2026 Google LLC All rights reserved. Google and the Google logo are trademarks of Google LLC. All other company and product names may be trademarks of the respective companies with which they are associated.


---

## 🎓 Associate Cloud Engineer (ACE) Exam Anchors
| Core Exam Domain | Practical Architectural Takeaway |
| :--- | :--- |
| **Cloud Run architecture** | Fully managed serverless container runtime (Knative-based) |
| **Artifact Registry** | Storing and managing Docker container images in GCP |
| **Container contract** | Listening on PORT environment variable (default 8080), statelessness |
| **Deployment & Traffic Management** | `--allow-unauthenticated`, traffic splitting between revisions |

## ✅ Objective Verification Checklist
- [ ] Lab sandbox environment provisioned and active.
- [ ] Task 1 completed and verified.
- [ ] Task 2 completed and verified.
- [ ] Task 3 completed and verified.
- [ ] Task 4 completed and verified.
- [ ] Task 5 completed and verified.
- [ ] Task 6 completed and verified.
- [ ] All Qwiklabs progress checkmarks scored 100%.
- [ ] Lab ended cleanly to avoid quota leakage.