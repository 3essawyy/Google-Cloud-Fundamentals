# 06

### Comprehensive Technical Presentation & Study Guide

> **Course / Domain:** Computer Science & Engineering · **Academic Term:** Academic Lecture Series
> **Lecturer / Author:** Course Instructor · **Source:** Official Lecture Presentation Slides
> **Documentation Standard:** DTCM-v3 High-Fidelity Architecture (`ptcm-pdf-v1`)

---

## Table of Contents

* [Slide 1: 06](#slide-1-06)
* [Slide 2: So far in this course ...](#slide-2-so-far-in-this-course)
* [Slide 3: Applications in the Cloud](#slide-3-applications-in-the-cloud)
* [Slide 4: Applications in the Cloud](#slide-4-applications-in-the-cloud)
* [Slide 5: Cloud Run is managed serverless computing](#slide-5-cloud-run-is-managed-serverless-computing)
* [Slide 6: Google Cloud Run workflow is a three-step process](#slide-6-google-cloud-run-workflow-is-a-three-step-process)
* [Slide 7: Cloud Run also has a source-based workflow](#slide-7-cloud-run-also-has-a-source-based-workflow)
* [Slide 8: You are only charged when your  container handles requests](#slide-8-you-are-only-charged-when-your-container-handles-requests)
* [Slide 9: Cloud Run can run any binary](#slide-9-cloud-run-can-run-any-binary)
* [Slide 10: Applications in the Cloud](#slide-10-applications-in-the-cloud)
* [Slide 11: Integrated cloud functions handle application events](#slide-11-integrated-cloud-functions-handle-application-events)
* [Slide 12: Cloud Run functions allows your code to respond to events](#slide-12-cloud-run-functions-allows-your-code-to-respond-to-events)
* [Slide 13: Module Quiz](#slide-13-module-quiz)
* [Slide 14: Quiz | Question 1](#slide-14-quiz-question-1)
* [Slide 15: Quiz | Question 1](#slide-15-quiz-question-1)
* [Slide 16: Quiz | Question 2](#slide-16-quiz-question-2)
* [Slide 17: Quiz | Question 2](#slide-17-quiz-question-2)
* [Slide 18: Quiz | Question 3](#slide-18-quiz-question-3)
* [Slide 19: Quiz | Question 3](#slide-19-quiz-question-3)
* [Slide 20: Lab Intro](#slide-20-lab-intro)

---

## List of Figures

* **Figure 1:** [Slide 1] 06 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 2:** [Slide 1] 06 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 3:** [Slide 2] So far in this course ... — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 4:** [Slide 2] So far in this course ... — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 5:** [Slide 2] So far in this course ... — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 6:** [Slide 2] So far in this course ... — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 7:** [Slide 3] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 8:** [Slide 3] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 9:** [Slide 4] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 10:** [Slide 4] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 11:** [Slide 5] Cloud Run is managed serverless computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 12:** [Slide 5] Cloud Run is managed serverless computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 13:** [Slide 6] Google Cloud Run workflow is a three-step process — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 14:** [Slide 6] Google Cloud Run workflow is a three-step process — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 15:** [Slide 6] Google Cloud Run workflow is a three-step process — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 16:** [Slide 6] Google Cloud Run workflow is a three-step process — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 17:** [Slide 7] Cloud Run also has a source-based workflow — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 18:** [Slide 7] Cloud Run also has a source-based workflow — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 19:** [Slide 7] Cloud Run also has a source-based workflow — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 20:** [Slide 7] Cloud Run also has a source-based workflow — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 21:** [Slide 8] You are only charged when your  container handles requests — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 22:** [Slide 9] Cloud Run can run any binary — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 23:** [Slide 9] Cloud Run can run any binary — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 24:** [Slide 10] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 25:** [Slide 10] Applications in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 26:** [Slide 11] Integrated cloud functions handle application events — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 27:** [Slide 11] Integrated cloud functions handle application events — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 28:** [Slide 11] Integrated cloud functions handle application events — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 29:** [Slide 12] Cloud Run functions allows your code to respond to events — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 30:** [Slide 13] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 31:** [Slide 13] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 32:** [Slide 14] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 33:** [Slide 15] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 34:** [Slide 15] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 35:** [Slide 16] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 36:** [Slide 17] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 37:** [Slide 17] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 38:** [Slide 18] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 39:** [Slide 19] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 40:** [Slide 19] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 41:** [Slide 20] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 42:** [Slide 20] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)

---

<a id="slide-1-06"></a>
### Slide 1: 06

* Proprietary + Confidential
* Applications
* in the Cloud

<!-- INJECT_START: slide_01_img_02 -->
![06 (slide_01_img_02)](media/slide_01_img_02.jpeg)

**Figure 2:** [Slide 1] 06 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_02 -->


<!-- INJECT_START: slide_01_img_01 -->
![06 (slide_01_img_01)](media/slide_01_img_01.jpeg)

**Figure 1:** [Slide 1] 06 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_01 -->


---

<a id="slide-2-so-far-in-this-course"></a>
### Slide 2: So far in this course ...


<!-- INJECT_START: slide_02_img_02 -->
![So far in this course ... (slide_02_img_02)](media/slide_02_img_02.jpeg)

**Figure 4:** [Slide 2] So far in this course ... — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_02 -->

* Proprietary + Confidential

<!-- INJECT_START: slide_02_img_04 -->
![So far in this course ... (slide_02_img_04)](media/slide_02_img_04.jpeg)

**Figure 6:** [Slide 2] So far in this course ... — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_04 -->


<!-- INJECT_START: slide_02_img_03 -->
![So far in this course ... (slide_02_img_03)](media/slide_02_img_03.jpeg)

**Figure 5:** [Slide 2] So far in this course ... — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_03 -->


<!-- INJECT_START: slide_02_img_01 -->
![So far in this course ... (slide_02_img_01)](media/slide_02_img_01.jpeg)

**Figure 3:** [Slide 2] So far in this course ... — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_01 -->

* So far in this course, we've provided an introduction to Google Cloud and explored the
* options and benefits related to using virtual machines, networks, storage, and
* containers in the Cloud.

---

<a id="slide-3-applications-in-the-cloud"></a>
### Slide 3: Applications in the Cloud


<!-- INJECT_START: slide_03_img_02 -->
![Applications in the Cloud (slide_03_img_02)](media/slide_03_img_02.jpeg)

**Figure 8:** [Slide 3] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_02 -->

* Cloud Run functions
* 01
* 02
* 01
* 02
* Cloud Run

<!-- INJECT_START: slide_03_img_01 -->
![Applications in the Cloud (slide_03_img_01)](media/slide_03_img_01.jpeg)

**Figure 7:** [Slide 3] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_01 -->

* In this final section of the course, we'll turn our attention to developing applications in
* the cloud by exploring Cloud Run and Cloud Run functions.

---

<a id="slide-4-applications-in-the-cloud"></a>
### Slide 4: Applications in the Cloud


<!-- INJECT_START: slide_04_img_02 -->
![Applications in the Cloud (slide_04_img_02)](media/slide_04_img_02.jpeg)

**Figure 10:** [Slide 4] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_02 -->

* Google Cloud API management tools
* 01
* 02
* Cloud Run functions
* 01
* 02
* App Engine
* Cloud Run

<!-- INJECT_START: slide_04_img_01 -->
![Applications in the Cloud (slide_04_img_01)](media/slide_04_img_01.jpeg)

**Figure 9:** [Slide 4] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_01 -->

* Let's begin with Cloud Run.

---

<a id="slide-5-cloud-run-is-managed-serverless-computing"></a>
### Slide 5: Cloud Run is managed serverless computing

* Proprietary + Confidential
* A managed compute platform that can run stateless containers

<!-- INJECT_START: slide_05_img_02 -->
![Cloud Run is managed serverless computing (slide_05_img_02)](media/slide_05_img_02.jpeg)

**Figure 12:** [Slide 5] Cloud Run is managed serverless computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_02 -->

* Serverless, removing the need for infrastructure management
* Built on Knative, an open API and runtime environment built on Kubernetes
* Can automatically scale up and down from zero almost instantaneously,
* charging only for the resources used

<!-- INJECT_START: slide_05_img_01 -->
![Cloud Run is managed serverless computing (slide_05_img_01)](media/slide_05_img_01.jpeg)

**Figure 11:** [Slide 5] Cloud Run is managed serverless computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_01 -->

* Cloud Run is a managed compute platform that lets you run stateless containers via
* web requests or Pub/Sub events.
* Cloud Run is serverless. That means it removes all infrastructure management tasks
* so you can focus on developing applications.
* It is built on Knative, an open API and runtime environment built on Kubernetes. It can
* be fully managed on Google Cloud, on Google Kubernetes Engine, or anywhere
* Knative runs.
* Cloud Run is fast. It can automatically scale up and down from zero almost
* instantaneously, and it charges only for the resources used, calculated down to the
* nearest 100 milliseconds, so you'll never pay for over-provisioned resources.

---

<a id="slide-6-google-cloud-run-workflow-is-a-three-step-process"></a>
### Slide 6: Google Cloud Run workflow is a three-step process

* Proprietary + Confidential
* 1
* 2
* 3
* Write your code
* Build and package
* Deploy to Cloud Run

<!-- INJECT_START: slide_06_img_02 -->
![Google Cloud Run workflow is a three-step process (slide_06_img_02)](media/slide_06_img_02.jpeg)

**Figure 14:** [Slide 6] Google Cloud Run workflow is a three-step process — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_02 -->

* Source code
* Container image

<!-- INJECT_START: slide_06_img_03 -->
![Google Cloud Run workflow is a three-step process (slide_06_img_03)](media/slide_06_img_03.jpeg)

**Figure 15:** [Slide 6] Google Cloud Run workflow is a three-step process — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_03 -->


<!-- INJECT_START: slide_06_img_04 -->
![Google Cloud Run workflow is a three-step process (slide_06_img_04)](media/slide_06_img_04.jpeg)

**Figure 16:** [Slide 6] Google Cloud Run workflow is a three-step process — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_04 -->

* Application
* (from Artifact Registry)
* Listen on a port and
* accept requests

<!-- INJECT_START: slide_06_img_01 -->
![Google Cloud Run workflow is a three-step process (slide_06_img_01)](media/slide_06_img_01.jpeg)

**Figure 13:** [Slide 6] Google Cloud Run workflow is a three-step process — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_01 -->

* The Cloud Run developer workflow is a straightforward three-step process.
* ●
* First, you write your application using your favorite programming language.
* This application should start a server that listens for web requests.
* ●
* Second, you build and package your application into a container image.
* ●
* Third, the container image is pushed to Artifact Registry, where Cloud Run will
* deploy it.
* Once you've deployed your container image, you'll get a unique HTTPS URL back.
* Cloud Run then starts your container on demand to handle requests, and ensures that
* all incoming requests are handled by dynamically adding and removing containers.
* Cloud Run is serverless, which means that you, as a developer, can focus on building
* your application and not on building and maintaining the infrastructure that powers it.

---

<a id="slide-7-cloud-run-also-has-a-source-based-workflow"></a>
### Slide 7: Cloud Run also has a source-based workflow

* Proprietary + Confidential
* 1
* 2
* Write your code
* Deploy to Cloud Run using Buildpacks

<!-- INJECT_START: slide_07_img_02 -->
![Cloud Run also has a source-based workflow (slide_07_img_02)](media/slide_07_img_02.jpeg)

**Figure 18:** [Slide 7] Cloud Run also has a source-based workflow — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_02 -->

* Buildpacks
* Source code

<!-- INJECT_START: slide_07_img_04 -->
![Cloud Run also has a source-based workflow (slide_07_img_04)](media/slide_07_img_04.jpeg)

**Figure 20:** [Slide 7] Cloud Run also has a source-based workflow — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_04 -->


<!-- INJECT_START: slide_07_img_03 -->
![Cloud Run also has a source-based workflow (slide_07_img_03)](media/slide_07_img_03.jpeg)

**Figure 19:** [Slide 7] Cloud Run also has a source-based workflow — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_03 -->

* Container image

<!-- INJECT_START: slide_07_img_01 -->
![Cloud Run also has a source-based workflow (slide_07_img_01)](media/slide_07_img_01.jpeg)

**Figure 17:** [Slide 7] Cloud Run also has a source-based workflow — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_01 -->

* For some use cases, a container-based workflow is great, because it gives you a great
* amount of transparency and flexibility. Sometimes, you're just looking for a way to
* turn source code into an HTTPS endpoint, and you want your vendor to make sure it
* your container image is secure, well-configured and built in a consistent way.
* With Cloud Run, you can do both. You can use a container-based workflow, as well as
* a source-based workflow.
* The source-based approach will deploy source code, instead of a container image.
* Cloud Run then builds the source and packages the application into a container
* image.
* Cloud Run does this using Buildpacks - an open source project.

---

<a id="slide-8-you-are-only-charged-when-your-container-handles-requests"></a>
### Slide 8: You are only charged when your  container handles requests

* Proprietary + Confidential
* You are only charged when your
* container handles requests
* Time
* Container lifespan
* Handling requests
* Shutdown
* Startup
* Billable
* Non-billable

<!-- INJECT_START: slide_08_img_01 -->
![You are only charged when your  container handles requests (slide_08_img_01)](media/slide_08_img_01.jpeg)

**Figure 21:** [Slide 8] You are only charged when your  container handles requests — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_01 -->

* The pricing model on Cloud Run is unique; as you only pay for the system resources
* you use while a container is handling web requests, with a granularity of 100ms, and
* when it is starting or shutting down.
* You do not pay for anything if your container does not handle requests. Additionally,
* there is a small fee for every one million requests you serve.
* The price of container time increases with CPU and memory. A container with more
* vCPU and memory is more expensive. Today, Cloud run can allocate up to 4 vCPUs
* and 8GB of memory.
* Most of the other compute products (such as Compute Engine), charge for servers as
* long as they are running, even if you are not using them. That means you're often
* paying for idle server capacity.

---

<a id="slide-9-cloud-run-can-run-any-binary"></a>
### Slide 9: Cloud Run can run any binary

* Proprietary + Confidential

<!-- INJECT_START: slide_09_img_02 -->
![Cloud Run can run any binary (slide_09_img_02)](media/slide_09_img_02.jpeg)

**Figure 23:** [Slide 9] Cloud Run can run any binary — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_02 -->

* Binaries
* Source code
* System packages
* Library dependencies
* Runtime
* Compiled for Linux 64-bit

<!-- INJECT_START: slide_09_img_01 -->
![Cloud Run can run any binary (slide_09_img_01)](media/slide_09_img_01.jpeg)

**Figure 22:** [Slide 9] Cloud Run can run any binary — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_01 -->

* You can use Cloud Run to run any binary, as long as it is compiled for Linux sixty-four
* bit.
* Now, this means you can use Cloud Run to run web applications written using popular
* **languages, such as:** Java, Python, Node.js, PHP, Go, and C++.
* And you can also run code written in less popular languages: Cobol, Haskell, and Perl.
* As long as your app handles web requests, you're good to go.

---

<a id="slide-10-applications-in-the-cloud"></a>
### Slide 10: Applications in the Cloud


<!-- INJECT_START: slide_10_img_02 -->
![Applications in the Cloud (slide_10_img_02)](media/slide_10_img_02.jpeg)

**Figure 25:** [Slide 10] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_02 -->

* Google Cloud API management tools
* 01
* 02
* Cloud Run functions
* 01
* 02
* App Engine
* Cloud Run

<!-- INJECT_START: slide_10_img_01 -->
![Applications in the Cloud (slide_10_img_01)](media/slide_10_img_01.jpeg)

**Figure 24:** [Slide 10] Applications in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_01 -->

* And then there is Cloud Run functions.

---

<a id="slide-11-integrated-cloud-functions-handle-application-events"></a>
### Slide 11: Integrated cloud functions handle application events


<!-- INJECT_START: slide_11_img_02 -->
![Integrated cloud functions handle application events (slide_11_img_02)](media/slide_11_img_02.jpeg)

**Figure 27:** [Slide 11] Integrated cloud functions handle application events — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_02 -->


<!-- INJECT_START: slide_11_img_03 -->
![Integrated cloud functions handle application events (slide_11_img_03)](media/slide_11_img_03.jpeg)

**Figure 28:** [Slide 11] Integrated cloud functions handle application events — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_03 -->


<!-- INJECT_START: slide_11_img_01 -->
![Integrated cloud functions handle application events (slide_11_img_01)](media/slide_11_img_01.jpeg)

**Figure 26:** [Slide 11] Integrated cloud functions handle application events — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_01 -->

* Many applications contain event-driven parts. For example, an application that lets
* users upload images. When that event takes place, the image might need to be
* processed in a few different ways, like converting the image to a standard format,
* converting a thumbnail into different sizes, and storing each new file in a repository.
  * This function could be integrated into an application, but then you'd have to provide
  * compute resources for itwhether it happens once a millisecond or once a day.

---

<a id="slide-12-cloud-run-functions-allows-your-code-to-respond-to-events"></a>
### Slide 12: Cloud Run functions allows your code to respond to events

* Proprietary + Confidential
* Lightweight, event-based, asynchronous compute solution
* Allows you to create small, single-purpose functions that respond to cloud events without the need
* to manage a server or a runtime environment
* Use these functions to construct applications from bite-sized business logic and connect and
* extend cloud services
* Billed to the nearest 100 milliseconds, and only while your code is running
* Supports writing source code in a number of programming languages, including Node.js, Python,
* Go, Java, .Net Core, Ruby, and PHP
* Events from Cloud Storage and Pub/Sub can trigger Cloud Run functions asynchronously, or use
* HTTP invocation for synchronous execution

<!-- INJECT_START: slide_12_img_01 -->
![Cloud Run functions allows your code to respond to events (slide_12_img_01)](media/slide_12_img_01.jpeg)

**Figure 29:** [Slide 12] Cloud Run functions allows your code to respond to events — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_01 -->

* With Cloud Run functions, you write a single-purpose function that completes the
* necessary image manipulations, and then arrange for it to automatically run whenever
* a new image is uploaded.
* Cloud Run functions is a lightweight, event-based, asynchronous compute solution
* that allows you to create small, single-purpose functions that respond to cloud events
* without the need to manage a server or a runtime environment. These functions can
* be used to construct applications from bite-sized business logic. Cloud Run functions
* can also be used to connect and extend cloud services. You are billed to the nearest
* 100 milliseconds, but only while your code is running.
* Cloud Run functions supports writing source code in a number of programming
* languages. These include Node.js, Python, Go, Java, .Net Core, Ruby, and PHP. For
* more information about the supported specific versions, refer to the runtimes
* documentation.
* Events from Cloud Storage and Pub/Sub can trigger Cloud Run functions
* asynchronously, or you can use HTTP invocation for synchronous execution.

---

<a id="slide-13-module-quiz"></a>
### Slide 13: Module Quiz


<!-- INJECT_START: slide_13_img_02 -->
![Module Quiz (slide_13_img_02)](media/slide_13_img_02.jpeg)

**Figure 31:** [Slide 13] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_02 -->


<!-- INJECT_START: slide_13_img_01 -->
![Module Quiz (slide_13_img_01)](media/slide_13_img_01.jpeg)

**Figure 30:** [Slide 13] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_01 -->


---

<a id="slide-14-quiz-question-1"></a>
### Slide 14: Quiz | Question 1

* Proprietary + Confidential
* Question
* Which scenario is best suited for using Cloud Run instead of Cloud Run functions?
* A.
* Sending an email notification whenever a new document is added to a specific folder
* in Cloud Storage.
* B.
* Hosting a dynamic web application that allows users to upload and share photos.
* C.
* Resizing images on demand when requested by a user through a web interface.
* D.
* Generating thumbnails for images uploaded to a Cloud Storage bucket.

<!-- INJECT_START: slide_14_img_01 -->
![Quiz | Question 1 (slide_14_img_01)](media/slide_14_img_01.jpeg)

**Figure 32:** [Slide 14] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_01 -->


---

<a id="slide-15-quiz-question-1"></a>
### Slide 15: Quiz | Question 1

* Proprietary + Confidential
* Answer
* Which scenario is best suited for using Cloud Run instead of Cloud Run functions?
* A.
* Sending an email notification whenever a new document is added to a specific folder
* in Cloud Storage.

<!-- INJECT_START: slide_15_img_02 -->
![Quiz | Question 1 (slide_15_img_02)](media/slide_15_img_02.jpeg)

**Figure 34:** [Slide 15] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_02 -->

* B.
* Hosting a dynamic web application that allows users to upload and share photos.
* C.
* Resizing images on demand when requested by a user through a web interface.
* D.
* Generating thumbnails for images uploaded to a Cloud Storage bucket.

<!-- INJECT_START: slide_15_img_01 -->
![Quiz | Question 1 (slide_15_img_01)](media/slide_15_img_01.jpeg)

**Figure 33:** [Slide 15] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_01 -->

* Which scenario is best suited for using Cloud Run instead of Cloud Run functions?
* A. Sending an email notification whenever a new document is added to a specific
* folder in Cloud Storage.
* **Feedback:** Incorrect. This event-driven task can be efficiently handled by Cloud Run
* functions, triggered by the upload event.
* B. Hosting a dynamic web application that allows users to upload and share photos.
* **Feedback:** Correct! This scenario requires a scalable web application with persistent
* connections and user interactions, making it ideal for Cloud Run's containerized
* environment and autoscaling capabilities.
* C. Resizing images on demand when requested by a user through a web interface.
* **Feedback:** Incorrect. While Cloud Run could handle this scenario, it's an event-driven
* task that can be efficiently handled by Cloud Run functions, triggered by the upload
* event.
* D. Generating thumbnails for images uploaded to a Cloud Storage bucket.
* **Feedback:** Incorrect. This event-driven image processing task is well-suited for Cloud
* Run functions.

---

<a id="slide-16-quiz-question-2"></a>
### Slide 16: Quiz | Question 2

* Proprietary + Confidential
* Question
* Which of these statements about Cloud Run functions are correct? Select three.
* **Cloud Run functions:**
* A.
* Is a scalable functions-as-a-service platform.
* B.
* Can be used to extend Cloud services.
* C.
* Require servers or VMs to be provisioned.
* D.
* Is integrated with Cloud Logging.
* E.
* Can only be invoked by sending HTTP requests.

<!-- INJECT_START: slide_16_img_01 -->
![Quiz | Question 2 (slide_16_img_01)](media/slide_16_img_01.jpeg)

**Figure 35:** [Slide 16] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_01 -->


---

<a id="slide-17-quiz-question-2"></a>
### Slide 17: Quiz | Question 2

* Proprietary + Confidential
* Answer
* Which of these statements about Cloud Run functions are correct? Select three.
* **Cloud Run functions:**

<!-- INJECT_START: slide_17_img_02 -->
![Quiz | Question 2 (slide_17_img_02)](media/slide_17_img_02.jpeg)

**Figure 37:** [Slide 17] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_02 -->

* A.
* Is a scalable functions-as-a-service platform.
* B.
* Can be used to extend Cloud services.
* C.
* Require servers or VMs to be provisioned.
* D.
* Is integrated with Cloud Logging.
* E.
* Can only be invoked by sending HTTP requests.

<!-- INJECT_START: slide_17_img_01 -->
![Quiz | Question 2 (slide_17_img_01)](media/slide_17_img_01.jpeg)

**Figure 36:** [Slide 17] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_01 -->

* **Cloud Run functions:**
* **A:** Is a scalable functions-as-a-service platform.
* Correct! Cloud Run functions is a service that enables you to build single-purpose
* functions that can automatically scale based on the number of requests to your
* function.
* **B:** Can be used to extend Cloud services.
* Correct! Cloud Run functions can be used as a connective layer to connect and extend
* other cloud services and create a serverless application.
* **C:** Require servers or VMs to be provisioned.
* Incorrect. Cloud Run functions is a serverless environment, so you do not need to
* provision infrastructure or manage servers.
* **D:** Is integrated with Cloud Logging.
* Correct! Cloud Run functions is integrated with Google Cloud Observability logging
* and monitoring services to make it fully observable.
* **E:** Can only be invoked by sending HTTP requests.
* Incorrect. Functions are triggered by HTTP requests or events from your cloud
* infrastructure.

---

<a id="slide-18-quiz-question-3"></a>
### Slide 18: Quiz | Question 3

* Proprietary + Confidential
* Question
* Why might a Google Cloud customer choose to use Cloud Run functions?
* A.
* Their application contains event-driven code that they don't want to provision
* compute resources for.
* B.
* Cloud Run functions is the primary way to run C++ applications in Google Cloud.
* C.
* Cloud Run functions is a free service for hosting compute operations.
* D.
* Their application has a legacy monolithic structure that they want to separate into
* microservices.

<!-- INJECT_START: slide_18_img_01 -->
![Quiz | Question 3 (slide_18_img_01)](media/slide_18_img_01.jpeg)

**Figure 38:** [Slide 18] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_01 -->


---

<a id="slide-19-quiz-question-3"></a>
### Slide 19: Quiz | Question 3

* Proprietary + Confidential
* Answer
* Why might a Google Cloud customer choose to use Cloud Run functions?
* A.
* Their application contains event-driven code that they don't want to provision
* compute resources for.

<!-- INJECT_START: slide_19_img_02 -->
![Quiz | Question 3 (slide_19_img_02)](media/slide_19_img_02.jpeg)

**Figure 40:** [Slide 19] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_02 -->

* B.
* Cloud Run functions is the primary way to run C++ applications in Google Cloud.
* C.
* Cloud Run functions is a free service for hosting compute operations.
* D.
* Their application has a legacy monolithic structure that they want to separate into
* microservices.

<!-- INJECT_START: slide_19_img_01 -->
![Quiz | Question 3 (slide_19_img_01)](media/slide_19_img_01.jpeg)

**Figure 39:** [Slide 19] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_01 -->

* Why might a Google Cloud customer choose to use Cloud Run functions?
* ***A:** Their application contains event-driven code that they don't want to provision
* compute resources for.
* **Feedback:** Correct!
* **B:** Cloud Run functions is the primary way to run C++ applications in Google Cloud.
* **Feedback:** Review the "Cloud Run functions" lecture.
* **C:** Cloud Run functions is a free service for hosting compute operations.
* **Feedback:** Review the "Cloud Run functions" lecture.
* **D:** Their application has a legacy monolithic structure that they want to separate into
* microservices.
* **Feedback:** Review the "Cloud Run functions" lecture.

---

<a id="slide-20-lab-intro"></a>
### Slide 20: Lab Intro

* Proprietary + Confidential

<!-- INJECT_START: slide_20_img_02 -->
![Lab Intro (slide_20_img_02)](media/slide_20_img_02.jpeg)

**Figure 42:** [Slide 20] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_02 -->

* Hello Cloud Run
* The goal of this lab is for you to build a
* simple containerized application image
* and deploy it to Cloud Run.

<!-- INJECT_START: slide_20_img_01 -->
![Lab Intro (slide_20_img_01)](media/slide_20_img_01.jpeg)

**Figure 41:** [Slide 20] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_01 -->


---
