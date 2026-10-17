# 02

### Comprehensive Technical Presentation & Study Guide

> **Course / Domain:** Computer Science & Engineering · **Academic Term:** Academic Lecture Series
> **Lecturer / Author:** Course Instructor · **Source:** Official Lecture Presentation Slides
> **Documentation Standard:** DTCM-v3 High-Fidelity Architecture (`ptcm-pdf-v1`)

---

## Table of Contents

* [Slide 1: Resources and  Access in the Cloud 02](#slide-1-resources-and-access-in-the-cloud-02)
* [Slide 2: Resources and Access in the Cloud](#slide-2-resources-and-access-in-the-cloud)
* [Slide 3: Resources and Access in the Cloud](#slide-3-resources-and-access-in-the-cloud)
* [Slide 4: Resources are hierarchical](#slide-4-resources-are-hierarchical)
* [Slide 5: Resource hierarchy determines policies](#slide-5-resource-hierarchy-determines-policies)
* [Slide 6: Projects can have different owners  and users 03](#slide-6-projects-can-have-different-owners-and-users-03)
* [Slide 7: Project attributes vary in uniqueness and immutability](#slide-7-project-attributes-vary-in-uniqueness-and-immutability)
* [Slide 8: Resource Manager manages projects](#slide-8-resource-manager-manages-projects)
* [Slide 9: Folders can contain subfolders  and projects](#slide-9-folders-can-contain-subfolders-and-projects)
* [Slide 10: Folders group projects](#slide-10-folders-group-projects)
* [Slide 11: Folders facilitate policy  inheritance](#slide-11-folders-facilitate-policy-inheritance)
* [Slide 12: Organization node is the topmost resource](#slide-12-organization-node-is-the-topmost-resource)
* [Slide 13: Special roles are associated with the Organization Node](#slide-13-special-roles-are-associated-with-the-organization-node)
* [Slide 14: Creating an organization node](#slide-14-creating-an-organization-node)
* [Slide 15: Resources and Access in the Cloud](#slide-15-resources-and-access-in-the-cloud)
* [Slide 16: Identity and Access Management applies policies](#slide-16-identity-and-access-management-applies-policies)
* [Slide 17: Policies are managed and applied by IAM](#slide-17-policies-are-managed-and-applied-by-iam)
* [Slide 18: Deny policies prevent specific IAM permissions](#slide-18-deny-policies-prevent-specific-iam-permissions)
* [Slide 19: Resources and Access in the Cloud](#slide-19-resources-and-access-in-the-cloud)
* [Slide 20: There are three kinds of IAM roles](#slide-20-there-are-three-kinds-of-iam-roles)
* [Slide 21: Basic IAM roles are broad in scope](#slide-21-basic-iam-roles-are-broad-in-scope)
* [Slide 22: Predefined roles match job needs](#slide-22-predefined-roles-match-job-needs)
* [Slide 23: Custom roles are more specific and flexible](#slide-23-custom-roles-are-more-specific-and-flexible)
* [Slide 24: Custom roles are created at the project or organization  level using IAM](#slide-24-custom-roles-are-created-at-the-project-or-organization-level-using-iam)
* [Slide 25: Resources and Access in the Cloud](#slide-25-resources-and-access-in-the-cloud)
* [Slide 26: Service accounts are assigned roles](#slide-26-service-accounts-are-assigned-roles)
* [Slide 27: Service accounts are identified with email addresses](#slide-27-service-accounts-are-identified-with-email-addresses)
* [Slide 28: Service accounts are also managed by IAM](#slide-28-service-accounts-are-also-managed-by-iam)
* [Slide 29: Resources and Access in the Cloud](#slide-29-resources-and-access-in-the-cloud)
* [Slide 30: Cloud Identity manages team and organization access](#slide-30-cloud-identity-manages-team-and-organization-access)
* [Slide 31: Cloud Identity defines user and group policies](#slide-31-cloud-identity-defines-user-and-group-policies)
* [Slide 32: Cloud Identity capabilities](#slide-32-cloud-identity-capabilities)
* [Slide 33: Resources and Access in the Cloud](#slide-33-resources-and-access-in-the-cloud)
* [Slide 34: You can interact with Google Cloud in four ways](#slide-34-you-can-interact-with-google-cloud-in-four-ways)
* [Slide 35: Google Cloud console provides web-based interaction](#slide-35-google-cloud-console-provides-web-based-interaction)
* [Slide 36: Google Cloud SDK is a collection of command line tools](#slide-36-google-cloud-sdk-is-a-collection-of-command-line-tools)
* [Slide 37: Cloud Shell provides command line access to resources](#slide-37-cloud-shell-provides-command-line-access-to-resources)
* [Slide 38: APIs allow code to control your Cloud resources](#slide-38-apis-allow-code-to-control-your-cloud-resources)
* [Slide 39: Manage your resources with the Google Cloud app](#slide-39-manage-your-resources-with-the-google-cloud-app)
* [Slide 40: Module Quiz](#slide-40-module-quiz)
* [Slide 41: Quiz | Question 1](#slide-41-quiz-question-1)
* [Slide 42: Quiz | Question 1](#slide-42-quiz-question-1)
* [Slide 43: Quiz | Question 2](#slide-43-quiz-question-2)
* [Slide 44: Quiz | Question 2](#slide-44-quiz-question-2)
* [Slide 45: Quiz | Question 3](#slide-45-quiz-question-3)
* [Slide 46: Quiz | Question 3](#slide-46-quiz-question-3)
* [Slide 47: Lab Intro](#slide-47-lab-intro)

---

## List of Figures

* **Figure 1:** [Slide 1] Resources and  Access in the Cloud 02 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 2:** [Slide 1] Resources and  Access in the Cloud 02 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 3:** [Slide 2] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 4:** [Slide 2] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 5:** [Slide 3] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 6:** [Slide 3] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 7:** [Slide 4] Resources are hierarchical — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 8:** [Slide 4] Resources are hierarchical — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 9:** [Slide 5] Resource hierarchy determines policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 10:** [Slide 5] Resource hierarchy determines policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 11:** [Slide 6] Projects can have different owners  and users 03 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 12:** [Slide 6] Projects can have different owners  and users 03 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 13:** [Slide 7] Project attributes vary in uniqueness and immutability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 14:** [Slide 7] Project attributes vary in uniqueness and immutability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 15:** [Slide 7] Project attributes vary in uniqueness and immutability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 16:** [Slide 7] Project attributes vary in uniqueness and immutability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 17:** [Slide 8] Resource Manager manages projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 18:** [Slide 8] Resource Manager manages projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 19:** [Slide 8] Resource Manager manages projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 20:** [Slide 9] Folders can contain subfolders  and projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 21:** [Slide 9] Folders can contain subfolders  and projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 22:** [Slide 10] Folders group projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 23:** [Slide 10] Folders group projects — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 24:** [Slide 11] Folders facilitate policy  inheritance — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 25:** [Slide 11] Folders facilitate policy  inheritance — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 26:** [Slide 12] Organization node is the topmost resource — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 27:** [Slide 12] Organization node is the topmost resource — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 28:** [Slide 13] Special roles are associated with the Organization Node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 29:** [Slide 13] Special roles are associated with the Organization Node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 30:** [Slide 14] Creating an organization node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 31:** [Slide 14] Creating an organization node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 32:** [Slide 14] Creating an organization node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 33:** [Slide 14] Creating an organization node — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 34:** [Slide 15] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 35:** [Slide 15] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 36:** [Slide 16] Identity and Access Management applies policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 37:** [Slide 16] Identity and Access Management applies policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 38:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 39:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 40:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 41:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 42:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 43:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 44:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 45:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 46:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 47:** [Slide 17] Policies are managed and applied by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 48:** [Slide 18] Deny policies prevent specific IAM permissions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 49:** [Slide 18] Deny policies prevent specific IAM permissions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 50:** [Slide 18] Deny policies prevent specific IAM permissions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 51:** [Slide 18] Deny policies prevent specific IAM permissions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 52:** [Slide 19] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 53:** [Slide 19] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 54:** [Slide 20] There are three kinds of IAM roles — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 55:** [Slide 20] There are three kinds of IAM roles — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 56:** [Slide 21] Basic IAM roles are broad in scope — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 57:** [Slide 21] Basic IAM roles are broad in scope — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 58:** [Slide 22] Predefined roles match job needs — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 59:** [Slide 22] Predefined roles match job needs — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 60:** [Slide 22] Predefined roles match job needs — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 61:** [Slide 22] Predefined roles match job needs — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 62:** [Slide 23] Custom roles are more specific and flexible — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 63:** [Slide 23] Custom roles are more specific and flexible — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 64:** [Slide 23] Custom roles are more specific and flexible — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 65:** [Slide 23] Custom roles are more specific and flexible — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 66:** [Slide 24] Custom roles are created at the project or organization  level using IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 67:** [Slide 24] Custom roles are created at the project or organization  level using IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 68:** [Slide 24] Custom roles are created at the project or organization  level using IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 69:** [Slide 25] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 70:** [Slide 25] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 71:** [Slide 26] Service accounts are assigned roles — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 72:** [Slide 26] Service accounts are assigned roles — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 73:** [Slide 26] Service accounts are assigned roles — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 74:** [Slide 27] Service accounts are identified with email addresses — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 75:** [Slide 27] Service accounts are identified with email addresses — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 76:** [Slide 28] Service accounts are also managed by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 77:** [Slide 28] Service accounts are also managed by IAM — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 78:** [Slide 29] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 79:** [Slide 29] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 80:** [Slide 30] Cloud Identity manages team and organization access — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 81:** [Slide 30] Cloud Identity manages team and organization access — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 82:** [Slide 31] Cloud Identity defines user and group policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 83:** [Slide 31] Cloud Identity defines user and group policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 84:** [Slide 31] Cloud Identity defines user and group policies — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 85:** [Slide 32] Cloud Identity capabilities — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 86:** [Slide 32] Cloud Identity capabilities — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 87:** [Slide 32] Cloud Identity capabilities — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 88:** [Slide 32] Cloud Identity capabilities — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 89:** [Slide 33] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 90:** [Slide 33] Resources and Access in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 91:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 92:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 93:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 94:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 95:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 96:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 97:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 98:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 99:** [Slide 34] You can interact with Google Cloud in four ways — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 100:** [Slide 35] Google Cloud console provides web-based interaction — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 101:** [Slide 35] Google Cloud console provides web-based interaction — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 102:** [Slide 35] Google Cloud console provides web-based interaction — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 103:** [Slide 36] Google Cloud SDK is a collection of command line tools — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 104:** [Slide 36] Google Cloud SDK is a collection of command line tools — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 105:** [Slide 36] Google Cloud SDK is a collection of command line tools — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 106:** [Slide 36] Google Cloud SDK is a collection of command line tools — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 107:** [Slide 37] Cloud Shell provides command line access to resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 108:** [Slide 37] Cloud Shell provides command line access to resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 109:** [Slide 37] Cloud Shell provides command line access to resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 110:** [Slide 37] Cloud Shell provides command line access to resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 111:** [Slide 37] Cloud Shell provides command line access to resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 112:** [Slide 38] APIs allow code to control your Cloud resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 113:** [Slide 38] APIs allow code to control your Cloud resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 114:** [Slide 38] APIs allow code to control your Cloud resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 115:** [Slide 38] APIs allow code to control your Cloud resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 116:** [Slide 38] APIs allow code to control your Cloud resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 117:** [Slide 39] Manage your resources with the Google Cloud app — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 118:** [Slide 39] Manage your resources with the Google Cloud app — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 119:** [Slide 39] Manage your resources with the Google Cloud app — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 120:** [Slide 39] Manage your resources with the Google Cloud app — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 121:** [Slide 39] Manage your resources with the Google Cloud app — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 122:** [Slide 40] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 123:** [Slide 40] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 124:** [Slide 41] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 125:** [Slide 42] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 126:** [Slide 42] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 127:** [Slide 43] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 128:** [Slide 44] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 129:** [Slide 44] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 130:** [Slide 45] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 131:** [Slide 46] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 132:** [Slide 46] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 133:** [Slide 47] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 134:** [Slide 47] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)

---

<a id="slide-1-resources-and-access-in-the-cloud-02"></a>
### Slide 1: Resources and  Access in the Cloud 02

* Proprietary + Confidential
* Resources and
* Access in the Cloud
* 02

<!-- INJECT_START: slide_01_img_02 -->
![Resources and  Access in the Cloud 02 (slide_01_img_02)](media/slide_01_img_02.jpeg)

**Figure 2:** [Slide 1] Resources and  Access in the Cloud 02 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_02 -->


<!-- INJECT_START: slide_01_img_01 -->
![Resources and  Access in the Cloud 02 (slide_01_img_01)](media/slide_01_img_01.jpeg)

**Figure 1:** [Slide 1] Resources and  Access in the Cloud 02 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_01 -->

* Now that you've had a chance to explore what cloud computing is, the pricing
* structure and billing practices available with Google Cloud, and the ways that Google
* strives to make the platform secure and environmentally friendly, let's now work to
* understand the functional structure of Google Cloud.

---

<a id="slide-2-resources-and-access-in-the-cloud"></a>
### Slide 2: Resources and Access in the Cloud


<!-- INJECT_START: slide_02_img_02 -->
![Resources and Access in the Cloud (slide_02_img_02)](media/slide_02_img_02.jpeg)

**Figure 4:** [Slide 2] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_02_img_01 -->
![Resources and Access in the Cloud (slide_02_img_01)](media/slide_02_img_01.jpeg)

**Figure 3:** [Slide 2] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_01 -->

* In this section of the course, we'll see how resources get organized with projects, and
* how access to those resources gets shared with the right part of a workforce through
* a tool called Identity and Access Management, or IAM.
* We'll also look into the different ways in which you can interact with Google Cloud,
* including our web user interface, command-line interface, and our mobile apps.

---

<a id="slide-3-resources-and-access-in-the-cloud"></a>
### Slide 3: Resources and Access in the Cloud


<!-- INJECT_START: slide_03_img_02 -->
![Resources and Access in the Cloud (slide_03_img_02)](media/slide_03_img_02.jpeg)

**Figure 6:** [Slide 3] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_03_img_01 -->
![Resources and Access in the Cloud (slide_03_img_01)](media/slide_03_img_01.jpeg)

**Figure 5:** [Slide 3] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_01 -->

* We'll begin with the Google Cloud Resource Hierarchy.

---

<a id="slide-4-resources-are-hierarchical"></a>
### Slide 4: Resources are hierarchical


<!-- INJECT_START: slide_04_img_02 -->
![Resources are hierarchical (slide_04_img_02)](media/slide_04_img_02.jpeg)

**Figure 8:** [Slide 4] Resources are hierarchical — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_02 -->


<!-- INJECT_START: slide_04_img_01 -->
![Resources are hierarchical (slide_04_img_01)](media/slide_04_img_01.jpeg)

**Figure 7:** [Slide 4] Resources are hierarchical — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_01 -->

* This hierarchy is made up of four levels, and starting from the bottom up they are:
* resources, projects, folders, and an organization node.
* At the first level are resources. These represent virtual machines, Cloud Storage
* buckets, Virtual Private Networks (VPCs), tables in BigQuery, or anything else in
* Google Cloud.
* Resources get organized into projects, which sit on the second level.
* Projects can be organized into folders, or even subfolders. These sit at the third level.
* And then at the top level is an organization node, which encompasses all the projects,
* folders, and resources in your organization.

---

<a id="slide-5-resource-hierarchy-determines-policies"></a>
### Slide 5: Resource hierarchy determines policies


<!-- INJECT_START: slide_05_img_02 -->
![Resource hierarchy determines policies (slide_05_img_02)](media/slide_05_img_02.jpeg)

**Figure 10:** [Slide 5] Resource hierarchy determines policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_02 -->


<!-- INJECT_START: slide_05_img_01 -->
![Resource hierarchy determines policies (slide_05_img_01)](media/slide_05_img_01.jpeg)

**Figure 9:** [Slide 5] Resource hierarchy determines policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_01 -->

* It's important to understand this resource hierarchy, as it directly relates to how
* policies are managed and applied when using Google Cloud.
* Policies can be defined at the project, folder, and organization node levels. Some
* Google Cloud services allow policies to be applied to individual resources, too.
* Policies are also inherited downward. This means that if you apply a policy to a folder,
* it will also apply to all of the projects within that folder.

---

<a id="slide-6-projects-can-have-different-owners-and-users-03"></a>
### Slide 6: Projects can have different owners  and users 03


<!-- INJECT_START: slide_06_img_02 -->
![Projects can have different owners  and users 03 (slide_06_img_02)](media/slide_06_img_02.jpeg)

**Figure 12:** [Slide 6] Projects can have different owners  and users 03 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_02 -->


<!-- INJECT_START: slide_06_img_01 -->
![Projects can have different owners  and users 03 (slide_06_img_01)](media/slide_06_img_01.jpeg)

**Figure 11:** [Slide 6] Projects can have different owners  and users 03 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_01 -->

* Let's spend a little more time on the second level of the resource hierarchy, projects.
* Projects are the basis for enabling and using Google Cloud services, like managing
* APIs, enabling billing, adding and removing collaborators, and enabling other Google
* services.
* Each project is a separate compartment, and each resource belongs to exactly one
* project. Projects can have different owners and users, as they're billed and managed
* separately.

---

<a id="slide-7-project-attributes-vary-in-uniqueness-and-immutability"></a>
### Slide 7: Project attributes vary in uniqueness and immutability

* Proprietary + Confidential

<!-- INJECT_START: slide_07_img_02 -->
![Project attributes vary in uniqueness and immutability (slide_07_img_02)](media/slide_07_img_02.jpeg)

**Figure 14:** [Slide 7] Project attributes vary in uniqueness and immutability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_02 -->


<!-- INJECT_START: slide_07_img_03 -->
![Project attributes vary in uniqueness and immutability (slide_07_img_03)](media/slide_07_img_03.jpeg)

**Figure 15:** [Slide 7] Project attributes vary in uniqueness and immutability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_03 -->


<!-- INJECT_START: slide_07_img_04 -->
![Project attributes vary in uniqueness and immutability (slide_07_img_04)](media/slide_07_img_04.jpeg)

**Figure 16:** [Slide 7] Project attributes vary in uniqueness and immutability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_04 -->

* Project ID
* Project name
* Project number
* Need not be unique
* Globally unique
* Assigned by
* Google Cloud
* Chosen by you
* Mutable
* Immutable

<!-- INJECT_START: slide_07_img_01 -->
![Project attributes vary in uniqueness and immutability (slide_07_img_01)](media/slide_07_img_01.jpeg)

**Figure 13:** [Slide 7] Project attributes vary in uniqueness and immutability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_01 -->

* Each Google Cloud project has three identifying attributes: a project ID, a project
* name, and a project number.
  * ●
  * The project ID is a globally unique identifier assigned by Google that cannot be
  * changedthey are immutableafter creation. Project IDs are used in different
  * contexts to inform Google Cloud of the exact project to work with.
  * ●
  * The project names, however, are user-created. They don't have to be unique
  * and they can be changed at any time, so they are not immutable.
  * ●
  * Google Cloud also assigns each project a unique project number. It's helpful
  * to know that these Google-generated numbers exist, but we won't explore
  * them much in this course. They are mainly used internally, by Google Cloud, to
  * keep track of resources.

---

<a id="slide-8-resource-manager-manages-projects"></a>
### Slide 8: Resource Manager manages projects


<!-- INJECT_START: slide_08_img_02 -->
![Resource Manager manages projects (slide_08_img_02)](media/slide_08_img_02.jpeg)

**Figure 18:** [Slide 8] Resource Manager manages projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_02 -->


<!-- INJECT_START: slide_08_img_03 -->
![Resource Manager manages projects (slide_08_img_03)](media/slide_08_img_03.jpeg)

**Figure 19:** [Slide 8] Resource Manager manages projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_03 -->


<!-- INJECT_START: slide_08_img_01 -->
![Resource Manager manages projects (slide_08_img_01)](media/slide_08_img_01.jpeg)

**Figure 17:** [Slide 8] Resource Manager manages projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_01 -->

* So, how is one expected to manage projects? Google Cloud has the Resource
* Manager tool, designed to programmatically help do just that.
* It's an API that can gather a list of all the projects associated with an account, create
* new projects, update existing projects, and delete projects. It can even recover
* projects that were previously deleted and can be accessed through the RPC API and
* the REST API.

---

<a id="slide-9-folders-can-contain-subfolders-and-projects"></a>
### Slide 9: Folders can contain subfolders  and projects


<!-- INJECT_START: slide_09_img_02 -->
![Folders can contain subfolders  and projects (slide_09_img_02)](media/slide_09_img_02.jpeg)

**Figure 21:** [Slide 9] Folders can contain subfolders  and projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_02 -->


<!-- INJECT_START: slide_09_img_01 -->
![Folders can contain subfolders  and projects (slide_09_img_01)](media/slide_09_img_01.jpeg)

**Figure 20:** [Slide 9] Folders can contain subfolders  and projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_01 -->

* The third level of the Google Cloud resource hierarchy is folders.
* Folders let you assign policies to resources at a level of granularity you choose. The
* projects and subfolders in a folder contain resources that inherit policies and
* permissions assigned to that folder.
* A folder can contain projects, other folders, or a combination of both.

---

<a id="slide-10-folders-group-projects"></a>
### Slide 10: Folders group projects


<!-- INJECT_START: slide_10_img_02 -->
![Folders group projects (slide_10_img_02)](media/slide_10_img_02.jpeg)

**Figure 23:** [Slide 10] Folders group projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_02 -->


<!-- INJECT_START: slide_10_img_01 -->
![Folders group projects (slide_10_img_01)](media/slide_10_img_01.jpeg)

**Figure 22:** [Slide 10] Folders group projects — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_01 -->

* You can use folders to group projects under an organization in a hierarchy.
* For example, your organization might contain multiple departments, each with its own
* set of Google Cloud resources. Folders allow you to group these resources on a
* per-department basis.
* Folders give teams the ability to delegate administrative rights so that they can work
* independently.

---

<a id="slide-11-folders-facilitate-policy-inheritance"></a>
### Slide 11: Folders facilitate policy  inheritance


<!-- INJECT_START: slide_11_img_02 -->
![Folders facilitate policy  inheritance (slide_11_img_02)](media/slide_11_img_02.jpeg)

**Figure 25:** [Slide 11] Folders facilitate policy  inheritance — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_02 -->


<!-- INJECT_START: slide_11_img_01 -->
![Folders facilitate policy  inheritance (slide_11_img_01)](media/slide_11_img_01.jpeg)

**Figure 24:** [Slide 11] Folders facilitate policy  inheritance — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_01 -->

* As previously mentioned, the resources in a folder inherit policies and permissions
* from that folder.
* For example, if you have two different projects that are administered by the same
* team, you can put policies into a common folder so they have the same permissions.
  * Doing it the other way--putting duplicate copies of those policies on both
  * projectscould be tedious and error-prone. If you needed to change permissions on
  * both resources, you would now have to do that in two places instead of just one.

---

<a id="slide-12-organization-node-is-the-topmost-resource"></a>
### Slide 12: Organization node is the topmost resource


<!-- INJECT_START: slide_12_img_02 -->
![Organization node is the topmost resource (slide_12_img_02)](media/slide_12_img_02.jpeg)

**Figure 27:** [Slide 12] Organization node is the topmost resource — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_02 -->


<!-- INJECT_START: slide_12_img_01 -->
![Organization node is the topmost resource (slide_12_img_01)](media/slide_12_img_01.jpeg)

**Figure 26:** [Slide 12] Organization node is the topmost resource — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_01 -->

* To use folders, you must have an organization node, which is the very topmost
* resource in the Google Cloud hierarchy.
* Everything else attached to that account goes under this node, which includes
* projects, folders, and other resources.

---

<a id="slide-13-special-roles-are-associated-with-the-organization-node"></a>
### Slide 13: Special roles are associated with the Organization Node


<!-- INJECT_START: slide_13_img_02 -->
![Special roles are associated with the Organization Node (slide_13_img_02)](media/slide_13_img_02.jpeg)

**Figure 29:** [Slide 13] Special roles are associated with the Organization Node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_02 -->


<!-- INJECT_START: slide_13_img_01 -->
![Special roles are associated with the Organization Node (slide_13_img_01)](media/slide_13_img_01.jpeg)

**Figure 28:** [Slide 13] Special roles are associated with the Organization Node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_01 -->

* There are some special roles associated with this top level organization node.
* For example, you can designate an organization policy administrator, so that only
* people with privilege can change policies. You can also assign a project creator role,
* which is a great way to control who can create projects and, therefore, who can spend
* money.

---

<a id="slide-14-creating-an-organization-node"></a>
### Slide 14: Creating an organization node


<!-- INJECT_START: slide_14_img_02 -->
![Creating an organization node (slide_14_img_02)](media/slide_14_img_02.jpeg)

**Figure 31:** [Slide 14] Creating an organization node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_02 -->


<!-- INJECT_START: slide_14_img_03 -->
![Creating an organization node (slide_14_img_03)](media/slide_14_img_03.jpeg)

**Figure 32:** [Slide 14] Creating an organization node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_03 -->


<!-- INJECT_START: slide_14_img_04 -->
![Creating an organization node (slide_14_img_04)](media/slide_14_img_04.jpeg)

**Figure 33:** [Slide 14] Creating an organization node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_04 -->


<!-- INJECT_START: slide_14_img_01 -->
![Creating an organization node (slide_14_img_01)](media/slide_14_img_01.jpeg)

**Figure 30:** [Slide 14] Creating an organization node — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_01 -->

* So how do you create an organization node? In part the answer depends on whether
* your company is also a Google Workspace customer. If you have a Workspace
* domain, Google Cloud projects will automatically belong to your organization node.
* Otherwise, you can use Cloud Identity, Google's identity, access, application, and
* endpoint management platform, to create one.
* When you get a new organization node, it lets anyone in the domain create projects
* and billing accounts, just as they could before. That's to avoid surprises and
* disruption.
* After you have an organization node, you can create folders underneath it and put
* projects into it. Both folders and projects are considered to be "children" of the
* organization node.

---

<a id="slide-15-resources-and-access-in-the-cloud"></a>
### Slide 15: Resources and Access in the Cloud


<!-- INJECT_START: slide_15_img_02 -->
![Resources and Access in the Cloud (slide_15_img_02)](media/slide_15_img_02.jpeg)

**Figure 35:** [Slide 15] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_15_img_01 -->
![Resources and Access in the Cloud (slide_15_img_01)](media/slide_15_img_01.jpeg)

**Figure 34:** [Slide 15] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_01 -->


---

<a id="slide-16-identity-and-access-management-applies-policies"></a>
### Slide 16: Identity and Access Management applies policies


<!-- INJECT_START: slide_16_img_02 -->
![Identity and Access Management applies policies (slide_16_img_02)](media/slide_16_img_02.jpeg)

**Figure 37:** [Slide 16] Identity and Access Management applies policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_02 -->


<!-- INJECT_START: slide_16_img_01 -->
![Identity and Access Management applies policies (slide_16_img_01)](media/slide_16_img_01.jpeg)

**Figure 36:** [Slide 16] Identity and Access Management applies policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_01 -->

* When an organization node contains lots of folders, projects, and resources, it's likely
* that a workforce might need to restrict who has access to what.
* To help with this task, administrators can use Identity and Access Management, or
* IAM. With IAM, administrators can apply policies that define who can do what on
* which resources.
* ●
* The "who" part of an IAM policy can be a Google account, a Google group, a
* service account, or Cloud Identity domain. A "who" is also called a "principal."
* Each principal has its own identifier, usually an email address.
* ●
* The "can do what" part of an IAM policy is defined by a role. An IAM role is a
* collection of permissions. When you grant a role to a principal, you grant all
* the permissions that the role contains. For example, to manage virtual
* machine instances in a project, you have to be able to create, delete, start, stop
* and change virtual machines. So these permissions are grouped together into
* a role to make them easier to understand and easier to manage.

---

<a id="slide-17-policies-are-managed-and-applied-by-iam"></a>
### Slide 17: Policies are managed and applied by IAM


<!-- INJECT_START: slide_17_img_02 -->
![Policies are managed and applied by IAM (slide_17_img_02)](media/slide_17_img_02.jpeg)

**Figure 39:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_02 -->


<!-- INJECT_START: slide_17_img_09 -->
![Policies are managed and applied by IAM (slide_17_img_09)](media/slide_17_img_09.jpeg)

**Figure 44:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_09 -->


<!-- INJECT_START: slide_17_img_08 -->
![Policies are managed and applied by IAM (slide_17_img_08)](media/slide_17_img_08.jpeg)

**Figure 43:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_08 -->


<!-- INJECT_START: slide_17_img_10 -->
![Policies are managed and applied by IAM (slide_17_img_10)](media/slide_17_img_10.jpeg)

**Figure 45:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_10 -->


<!-- INJECT_START: slide_17_img_11 -->
![Policies are managed and applied by IAM (slide_17_img_11)](media/slide_17_img_11.jpeg)

**Figure 46:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_11 -->


<!-- INJECT_START: slide_17_img_12 -->
![Policies are managed and applied by IAM (slide_17_img_12)](media/slide_17_img_12.jpeg)

**Figure 47:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_12 -->


<!-- INJECT_START: slide_17_img_06 -->
![Policies are managed and applied by IAM (slide_17_img_06)](media/slide_17_img_06.jpeg)

**Figure 42:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_06 -->


<!-- INJECT_START: slide_17_img_05 -->
![Policies are managed and applied by IAM (slide_17_img_05)](media/slide_17_img_05.jpeg)

**Figure 41:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_05 -->


<!-- INJECT_START: slide_17_img_03 -->
![Policies are managed and applied by IAM (slide_17_img_03)](media/slide_17_img_03.jpeg)

**Figure 40:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_03 -->


<!-- INJECT_START: slide_17_img_01 -->
![Policies are managed and applied by IAM (slide_17_img_01)](media/slide_17_img_01.jpeg)

**Figure 38:** [Slide 17] Policies are managed and applied by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_01 -->

* When a principal (user, group, or service account) is given a role on a specific element
* of the resource hierarchy, the resulting policy applies to the chosen element, as well
* as to all of the elements below it in the hierarchy.

---

<a id="slide-18-deny-policies-prevent-specific-iam-permissions"></a>
### Slide 18: Deny policies prevent specific IAM permissions

* Proprietary + Confidential

<!-- INJECT_START: slide_18_img_02 -->
![Deny policies prevent specific IAM permissions (slide_18_img_02)](media/slide_18_img_02.jpeg)

**Figure 49:** [Slide 18] Deny policies prevent specific IAM permissions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_02 -->


<!-- INJECT_START: slide_18_img_03 -->
![Deny policies prevent specific IAM permissions (slide_18_img_03)](media/slide_18_img_03.jpeg)

**Figure 50:** [Slide 18] Deny policies prevent specific IAM permissions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_03 -->


<!-- INJECT_START: slide_18_img_04 -->
![Deny policies prevent specific IAM permissions (slide_18_img_04)](media/slide_18_img_04.jpeg)

**Figure 51:** [Slide 18] Deny policies prevent specific IAM permissions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_04 -->


<!-- INJECT_START: slide_18_img_01 -->
![Deny policies prevent specific IAM permissions (slide_18_img_01)](media/slide_18_img_01.jpeg)

**Figure 48:** [Slide 18] Deny policies prevent specific IAM permissions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_01 -->

* You can define deny rules that prevent certain principals from using certain
* permissions, regardless of the roles they're granted. This is because IAM always
* checks relevant deny policies before checking relevant allow policies.
* Deny policies, like allow policies, are inherited through the resource hierarchy.

---

<a id="slide-19-resources-and-access-in-the-cloud"></a>
### Slide 19: Resources and Access in the Cloud


<!-- INJECT_START: slide_19_img_02 -->
![Resources and Access in the Cloud (slide_19_img_02)](media/slide_19_img_02.jpeg)

**Figure 53:** [Slide 19] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_19_img_01 -->
![Resources and Access in the Cloud (slide_19_img_01)](media/slide_19_img_01.jpeg)

**Figure 52:** [Slide 19] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_01 -->


---

<a id="slide-20-there-are-three-kinds-of-iam-roles"></a>
### Slide 20: There are three kinds of IAM roles


<!-- INJECT_START: slide_20_img_02 -->
![There are three kinds of IAM roles (slide_20_img_02)](media/slide_20_img_02.jpeg)

**Figure 55:** [Slide 20] There are three kinds of IAM roles — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_02 -->


<!-- INJECT_START: slide_20_img_01 -->
![There are three kinds of IAM roles (slide_20_img_01)](media/slide_20_img_01.jpeg)

**Figure 54:** [Slide 20] There are three kinds of IAM roles — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_01 -->

* There are three kinds of roles in IAM: basic, predefined, and custom.

---

<a id="slide-21-basic-iam-roles-are-broad-in-scope"></a>
### Slide 21: Basic IAM roles are broad in scope


<!-- INJECT_START: slide_21_img_02 -->
![Basic IAM roles are broad in scope (slide_21_img_02)](media/slide_21_img_02.jpeg)

**Figure 57:** [Slide 21] Basic IAM roles are broad in scope — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_02 -->


<!-- INJECT_START: slide_21_img_01 -->
![Basic IAM roles are broad in scope (slide_21_img_01)](media/slide_21_img_01.jpeg)

**Figure 56:** [Slide 21] Basic IAM roles are broad in scope — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_01 -->

* The first role type is basic. Basic roles are quite broad in scope. When applied to a
* Google Cloud project, they affect all resources in that project. Basic roles include
* owner, editor, viewer, and billing administrator.
* Let's have a look at these basic roles:
* ●
* Project viewers can examine resources, but can make no changes.
* ●
* Project editors can examine and make changes to a resource.
* ●
* And project owners can also examine and make changes to a resource. In
* addition, project owners can manage the associate roles and permissions, as
* well as set up billing.
* ●
* Often companies want someone to be able to control the billing for a project,
* but not have permissions to change the resources in the project. This is
* possible through a billing administrator role.
* **A word of caution:** If several people are working together on a project that contains
* sensitive data, basic roles are probably too broad. Fortunately, IAM provides other
* ways to assign permissions that are more specifically tailored to meet the needs of
* typical job roles.

---

<a id="slide-22-predefined-roles-match-job-needs"></a>
### Slide 22: Predefined roles match job needs


<!-- INJECT_START: slide_22_img_02 -->
![Predefined roles match job needs (slide_22_img_02)](media/slide_22_img_02.jpeg)

**Figure 59:** [Slide 22] Predefined roles match job needs — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_02 -->


<!-- INJECT_START: slide_22_img_04 -->
![Predefined roles match job needs (slide_22_img_04)](media/slide_22_img_04.jpeg)

**Figure 60:** [Slide 22] Predefined roles match job needs — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_04 -->


<!-- INJECT_START: slide_22_img_05 -->
![Predefined roles match job needs (slide_22_img_05)](media/slide_22_img_05.jpeg)

**Figure 61:** [Slide 22] Predefined roles match job needs — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_05 -->


<!-- INJECT_START: slide_22_img_01 -->
![Predefined roles match job needs (slide_22_img_01)](media/slide_22_img_01.jpeg)

**Figure 58:** [Slide 22] Predefined roles match job needs — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_01 -->

* This brings us to the second type of role, predefined roles.
* Specific Google Cloud services offer sets of predefined roles, and they even define
* where those roles can be applied.
* Let's take Compute Engine for example, a Google Cloud product that offers virtual
* machines as a service. With Compute Engine, you can apply specific predefined roles
* **- such as "instanceAdmin":** to Compute Engine resources in a given project, a given
* folder, or an entire organization. This then allows whoever has these roles to perform
* a specific set of pre-defined actions.

---

<a id="slide-23-custom-roles-are-more-specific-and-flexible"></a>
### Slide 23: Custom roles are more specific and flexible


<!-- INJECT_START: slide_23_img_02 -->
![Custom roles are more specific and flexible (slide_23_img_02)](media/slide_23_img_02.jpeg)

**Figure 63:** [Slide 23] Custom roles are more specific and flexible — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_02 -->


<!-- INJECT_START: slide_23_img_04 -->
![Custom roles are more specific and flexible (slide_23_img_04)](media/slide_23_img_04.jpeg)

**Figure 64:** [Slide 23] Custom roles are more specific and flexible — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_04 -->


<!-- INJECT_START: slide_23_img_05 -->
![Custom roles are more specific and flexible (slide_23_img_05)](media/slide_23_img_05.jpeg)

**Figure 65:** [Slide 23] Custom roles are more specific and flexible — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_05 -->


<!-- INJECT_START: slide_23_img_01 -->
![Custom roles are more specific and flexible (slide_23_img_01)](media/slide_23_img_01.jpeg)

**Figure 62:** [Slide 23] Custom roles are more specific and flexible — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_01 -->

* But what if you need to assign a role that has even more specific permissions? That's
* when you'd use a custom role.
* A lot of companies use a "least-privilege" model, in which each person in your
* organization is given the minimal amount of privilege needed to do their job. So, for
* example, maybe you want to define an "instanceOperator" role to allow some users to
* stop and start Compute Engine virtual machines, but not reconfigure them. Custom
* roles allow for that.

---

<a id="slide-24-custom-roles-are-created-at-the-project-or-organization-level-using-iam"></a>
### Slide 24: Custom roles are created at the project or organization  level using IAM


<!-- INJECT_START: slide_24_img_02 -->
![Custom roles are created at the project or organization  level using IAM (slide_24_img_02)](media/slide_24_img_02.jpeg)

**Figure 67:** [Slide 24] Custom roles are created at the project or organization  level using IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_24_img_02 -->

* Proprietary + Confidential

<!-- INJECT_START: slide_24_img_03 -->
![Custom roles are created at the project or organization  level using IAM (slide_24_img_03)](media/slide_24_img_03.jpeg)

**Figure 68:** [Slide 24] Custom roles are created at the project or organization  level using IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_24_img_03 -->


<!-- INJECT_START: slide_24_img_01 -->
![Custom roles are created at the project or organization  level using IAM (slide_24_img_01)](media/slide_24_img_01.jpeg)

**Figure 66:** [Slide 24] Custom roles are created at the project or organization  level using IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_24_img_01 -->

* You can create a custom role at the project or organization level. You cannot define
* custom roles at the folder level. If you need to use a custom role within a folder, define
* the custom role at the organization level.
* An organization-level custom role can include any of the IAM permissions that are
* supported in custom roles.
* A project-level custom role can contain any supported permission except for
* permissions that can only be used at the organization or folder level, such as
* resourcemanager.organizations.get.

---

<a id="slide-25-resources-and-access-in-the-cloud"></a>
### Slide 25: Resources and Access in the Cloud


<!-- INJECT_START: slide_25_img_02 -->
![Resources and Access in the Cloud (slide_25_img_02)](media/slide_25_img_02.jpeg)

**Figure 70:** [Slide 25] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_25_img_01 -->
![Resources and Access in the Cloud (slide_25_img_01)](media/slide_25_img_01.jpeg)

**Figure 69:** [Slide 25] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_01 -->

* Imagine you have a Compute Engine virtual machine running a program that needs to
* access other cloud services regularly. Instead of requiring a person to manually grant
* access each time the program runs, you can give the virtual machine itself the
* necessary permissions. This is where service accounts come in. Service accounts
* allow you to assign specific permissions to a virtual machine, so it can interact with
* other cloud services without human intervention.

---

<a id="slide-26-service-accounts-are-assigned-roles"></a>
### Slide 26: Service accounts are assigned roles


<!-- INJECT_START: slide_26_img_02 -->
![Service accounts are assigned roles (slide_26_img_02)](media/slide_26_img_02.jpeg)

**Figure 72:** [Slide 26] Service accounts are assigned roles — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_02 -->


<!-- INJECT_START: slide_26_img_03 -->
![Service accounts are assigned roles (slide_26_img_03)](media/slide_26_img_03.jpeg)

**Figure 73:** [Slide 26] Service accounts are assigned roles — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_03 -->


<!-- INJECT_START: slide_26_img_01 -->
![Service accounts are assigned roles (slide_26_img_01)](media/slide_26_img_01.jpeg)

**Figure 71:** [Slide 26] Service accounts are assigned roles — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_01 -->

  * Let's say you have an application running in a virtual machine that needs to store data
  * in Google Cloud Storage, but you don't want just anyone on the Internet to have
  * access to that datajust that particular virtual machine.
* You can create a service account to authenticate that VM to Cloud Storage.

---

<a id="slide-27-service-accounts-are-identified-with-email-addresses"></a>
### Slide 27: Service accounts are identified with email addresses


<!-- INJECT_START: slide_27_img_02 -->
![Service accounts are identified with email addresses (slide_27_img_02)](media/slide_27_img_02.jpeg)

**Figure 75:** [Slide 27] Service accounts are identified with email addresses — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_02 -->


<!-- INJECT_START: slide_27_img_01 -->
![Service accounts are identified with email addresses (slide_27_img_01)](media/slide_27_img_01.jpeg)

**Figure 74:** [Slide 27] Service accounts are identified with email addresses — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_01 -->

* Service accounts are named with an email address, but instead of passwords they
* use cryptographic keys to access resources.
* So, if a service account has been granted Compute Engine's Instance Admin role, this
* would allow an application running in a VM with that service account to create,
* modify, and delete other VMs.

---

<a id="slide-28-service-accounts-are-also-managed-by-iam"></a>
### Slide 28: Service accounts are also managed by IAM


<!-- INJECT_START: slide_28_img_02 -->
![Service accounts are also managed by IAM (slide_28_img_02)](media/slide_28_img_02.jpeg)

**Figure 77:** [Slide 28] Service accounts are also managed by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_02 -->


<!-- INJECT_START: slide_28_img_01 -->
![Service accounts are also managed by IAM (slide_28_img_01)](media/slide_28_img_01.jpeg)

**Figure 76:** [Slide 28] Service accounts are also managed by IAM — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_01 -->

* Service accounts do need to be managed.
* For example, maybe Alice needs to manage which Google accounts can act as
* service accounts, while Bob just needs to be able to view a list of service accounts.
* Fortunately, in addition to being an identity, a service account is also a resource!
* So it can have IAM policies of its own attached to it.
* This means that Alice can have the editor role on a service account, and Bob can have
* the viewer role. This is just like granting roles for any other Google Cloud resource.

---

<a id="slide-29-resources-and-access-in-the-cloud"></a>
### Slide 29: Resources and Access in the Cloud


<!-- INJECT_START: slide_29_img_02 -->
![Resources and Access in the Cloud (slide_29_img_02)](media/slide_29_img_02.jpeg)

**Figure 79:** [Slide 29] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_29_img_01 -->
![Resources and Access in the Cloud (slide_29_img_01)](media/slide_29_img_01.jpeg)

**Figure 78:** [Slide 29] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_01 -->


---

<a id="slide-30-cloud-identity-manages-team-and-organization-access"></a>
### Slide 30: Cloud Identity manages team and organization access


<!-- INJECT_START: slide_30_img_02 -->
![Cloud Identity manages team and organization access (slide_30_img_02)](media/slide_30_img_02.jpeg)

**Figure 81:** [Slide 30] Cloud Identity manages team and organization access — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_02 -->


<!-- INJECT_START: slide_30_img_01 -->
![Cloud Identity manages team and organization access (slide_30_img_01)](media/slide_30_img_01.jpeg)

**Figure 80:** [Slide 30] Cloud Identity manages team and organization access — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_01 -->

* When new Google Cloud customers start using the platform, it's common to log into
* the Google Cloud console with a Gmail account, and then use Google Groups to
* collaborate with teammates who are in similar roles.
* Although this approach is easy to start with, it can present challenges later because
* the team's identities are not centrally managed. This can be problematic if, for
* example, someone leaves the organization. With this setup, there is no easy way to
* immediately remove a user's access to the team's cloud resources.

---

<a id="slide-31-cloud-identity-defines-user-and-group-policies"></a>
### Slide 31: Cloud Identity defines user and group policies

* Proprietary + Confidential

<!-- INJECT_START: slide_31_img_02 -->
![Cloud Identity defines user and group policies (slide_31_img_02)](media/slide_31_img_02.jpeg)

**Figure 83:** [Slide 31] Cloud Identity defines user and group policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_02 -->


<!-- INJECT_START: slide_31_img_03 -->
![Cloud Identity defines user and group policies (slide_31_img_03)](media/slide_31_img_03.jpeg)

**Figure 84:** [Slide 31] Cloud Identity defines user and group policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_03 -->


<!-- INJECT_START: slide_31_img_01 -->
![Cloud Identity defines user and group policies (slide_31_img_01)](media/slide_31_img_01.jpeg)

**Figure 82:** [Slide 31] Cloud Identity defines user and group policies — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_01 -->

* With a tool called Cloud Identity, organizations can define policies and manage their
* users and groups using the Google Admin console.

---

<a id="slide-32-cloud-identity-capabilities"></a>
### Slide 32: Cloud Identity capabilities


<!-- INJECT_START: slide_32_img_02 -->
![Cloud Identity capabilities (slide_32_img_02)](media/slide_32_img_02.jpeg)

**Figure 86:** [Slide 32] Cloud Identity capabilities — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_02 -->


<!-- INJECT_START: slide_32_img_04 -->
![Cloud Identity capabilities (slide_32_img_04)](media/slide_32_img_04.jpeg)

**Figure 88:** [Slide 32] Cloud Identity capabilities — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_04 -->


<!-- INJECT_START: slide_32_img_03 -->
![Cloud Identity capabilities (slide_32_img_03)](media/slide_32_img_03.jpeg)

**Figure 87:** [Slide 32] Cloud Identity capabilities — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_03 -->


<!-- INJECT_START: slide_32_img_01 -->
![Cloud Identity capabilities (slide_32_img_01)](media/slide_32_img_01.jpeg)

**Figure 85:** [Slide 32] Cloud Identity capabilities — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_01 -->

* Admins can log in and manage Google Cloud resources using the same usernames
* and passwords they already use in existing Active Directory or LDAP systems.
* Using Cloud Identity also means that when someone leaves an organization, an
* administrator can use the Google Admin console to disable their account and remove
* them from groups.
* Cloud Identity is available in a free edition, and also a premium edition that provides
* capabilities to manage mobile devices.
* If you're a Google Cloud customer who is also a Google Workspace customer, this
* functionality is already available to you in the Google Admin console.

---

<a id="slide-33-resources-and-access-in-the-cloud"></a>
### Slide 33: Resources and Access in the Cloud


<!-- INJECT_START: slide_33_img_02 -->
![Resources and Access in the Cloud (slide_33_img_02)](media/slide_33_img_02.jpeg)

**Figure 90:** [Slide 33] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_02 -->

* 01
* 02
* Google Cloud resource hierarchy
* Identity and Access Management (IAM)
* 03
* 04
* IAM roles
* Service accounts
* 05
* 06
* Cloud Identity
* Interacting with Google Cloud

<!-- INJECT_START: slide_33_img_01 -->
![Resources and Access in the Cloud (slide_33_img_01)](media/slide_33_img_01.jpeg)

**Figure 89:** [Slide 33] Resources and Access in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_01 -->


---

<a id="slide-34-you-can-interact-with-google-cloud-in-four-ways"></a>
### Slide 34: You can interact with Google Cloud in four ways

* Proprietary + Confidential

<!-- INJECT_START: slide_34_img_02 -->
![You can interact with Google Cloud in four ways (slide_34_img_02)](media/slide_34_img_02.jpeg)

**Figure 92:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_02 -->


<!-- INJECT_START: slide_34_img_03 -->
![You can interact with Google Cloud in four ways (slide_34_img_03)](media/slide_34_img_03.jpeg)

**Figure 93:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_03 -->


<!-- INJECT_START: slide_34_img_04 -->
![You can interact with Google Cloud in four ways (slide_34_img_04)](media/slide_34_img_04.jpeg)

**Figure 94:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_04 -->


<!-- INJECT_START: slide_34_img_05 -->
![You can interact with Google Cloud in four ways (slide_34_img_05)](media/slide_34_img_05.jpeg)

**Figure 95:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_05 -->


<!-- INJECT_START: slide_34_img_06 -->
![You can interact with Google Cloud in four ways (slide_34_img_06)](media/slide_34_img_06.jpeg)

**Figure 96:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_06 -->


<!-- INJECT_START: slide_34_img_07 -->
![You can interact with Google Cloud in four ways (slide_34_img_07)](media/slide_34_img_07.jpeg)

**Figure 97:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_07 -->


<!-- INJECT_START: slide_34_img_09 -->
![You can interact with Google Cloud in four ways (slide_34_img_09)](media/slide_34_img_09.jpeg)

**Figure 99:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_09 -->


<!-- INJECT_START: slide_34_img_08 -->
![You can interact with Google Cloud in four ways (slide_34_img_08)](media/slide_34_img_08.jpeg)

**Figure 98:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_08 -->

* 03
* 02
* 04
* Google Cloud SDK
* APIs
* Google Cloud
* and Cloud Shell
* app

<!-- INJECT_START: slide_34_img_01 -->
![You can interact with Google Cloud in four ways (slide_34_img_01)](media/slide_34_img_01.jpeg)

**Figure 91:** [Slide 34] You can interact with Google Cloud in four ways — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_01 -->

* There are four ways to access and interact with Google Cloud.
* **Let's explore the list, which includes:** the Google Cloud console, the Google Cloud
* SDK and Cloud Shell, the APIs, and the Google Cloud app.

---

<a id="slide-35-google-cloud-console-provides-web-based-interaction"></a>
### Slide 35: Google Cloud console provides web-based interaction

* Proprietary + Confidential

<!-- INJECT_START: slide_35_img_02 -->
![Google Cloud console provides web-based interaction (slide_35_img_02)](media/slide_35_img_02.jpeg)

**Figure 101:** [Slide 35] Google Cloud console provides web-based interaction — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_02 -->


<!-- INJECT_START: slide_35_img_03 -->
![Google Cloud console provides web-based interaction (slide_35_img_03)](media/slide_35_img_03.jpeg)

**Figure 102:** [Slide 35] Google Cloud console provides web-based interaction — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_03 -->

* Simple web-based graphical user interface
* Easily find resources, check their health,
* have full management control over them,
* and set budgets
* Provides a search facility to quickly find
* resources and connect to instances
* via SSH in the browser

<!-- INJECT_START: slide_35_img_01 -->
![Google Cloud console provides web-based interaction (slide_35_img_01)](media/slide_35_img_01.jpeg)

**Figure 100:** [Slide 35] Google Cloud console provides web-based interaction — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_01 -->

* First is the Google Cloud console, which is Google Cloud's Graphical User Interface
* (GUI) which helps you deploy, scale, and diagnose production issues in a simple
* web-based interface. With the console, you can easily find your resources, check their
* health, have full management control over them, and set budgets to control how
* much you spend on them. The console also provides a search facility to quickly find
* resources and connect to instances via SSH in the browser.

---

<a id="slide-36-google-cloud-sdk-is-a-collection-of-command-line-tools"></a>
### Slide 36: Google Cloud SDK is a collection of command line tools

* Proprietary + Confidential

<!-- INJECT_START: slide_36_img_04 -->
![Google Cloud SDK is a collection of command line tools (slide_36_img_04)](media/slide_36_img_04.jpeg)

**Figure 106:** [Slide 36] Google Cloud SDK is a collection of command line tools — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_04 -->


<!-- INJECT_START: slide_36_img_02 -->
![Google Cloud SDK is a collection of command line tools (slide_36_img_02)](media/slide_36_img_02.jpeg)

**Figure 104:** [Slide 36] Google Cloud SDK is a collection of command line tools — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_02 -->


<!-- INJECT_START: slide_36_img_03 -->
![Google Cloud SDK is a collection of command line tools (slide_36_img_03)](media/slide_36_img_03.jpeg)

**Figure 105:** [Slide 36] Google Cloud SDK is a collection of command line tools — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_03 -->

* Set of tools to manage resources and
* applications hosted on Google Cloud
* **Includes:**
* **Google Cloud CLI:** Provides the main
* command-line interface for Google Cloud
* products and services
* **bq command-line tool:** A command-line
* tool for BigQuery

<!-- INJECT_START: slide_36_img_01 -->
![Google Cloud SDK is a collection of command line tools (slide_36_img_01)](media/slide_36_img_01.jpeg)

**Figure 103:** [Slide 36] Google Cloud SDK is a collection of command line tools — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_01 -->

* Second is through the Google Cloud SDK and Cloud Shell.
* The Google Cloud SDK is a set of tools that you can use to manage resources and
* applications hosted on Google Cloud. It includes the gcloud CLI, which provides the
* main command-line interface for Google Cloud products and services, as well as
* dedicated tools like bq, a command-line tool for BigQuery. When installed, all of the
* tools within the Google Cloud SDK are located under the bin directory.

---

<a id="slide-37-cloud-shell-provides-command-line-access-to-resources"></a>
### Slide 37: Cloud Shell provides command line access to resources

* Proprietary + Confidential

<!-- INJECT_START: slide_37_img_05 -->
![Cloud Shell provides command line access to resources (slide_37_img_05)](media/slide_37_img_05.jpeg)

**Figure 111:** [Slide 37] Cloud Shell provides command line access to resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_05 -->


<!-- INJECT_START: slide_37_img_02 -->
![Cloud Shell provides command line access to resources (slide_37_img_02)](media/slide_37_img_02.jpeg)

**Figure 108:** [Slide 37] Cloud Shell provides command line access to resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_02 -->


<!-- INJECT_START: slide_37_img_03 -->
![Cloud Shell provides command line access to resources (slide_37_img_03)](media/slide_37_img_03.jpeg)

**Figure 109:** [Slide 37] Cloud Shell provides command line access to resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_03 -->


<!-- INJECT_START: slide_37_img_04 -->
![Cloud Shell provides command line access to resources (slide_37_img_04)](media/slide_37_img_04.jpeg)

**Figure 110:** [Slide 37] Cloud Shell provides command line access to resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_04 -->

* Provides instant command-line access to cloud
* resources directly from a browser
* Debian-based environment with a persistent
* 5-GB home directory
* Pre-authenticated and pre-loaded with the
* Google Cloud SDK and popular tools, always
* updated and ready for immediate use

<!-- INJECT_START: slide_37_img_01 -->
![Cloud Shell provides command line access to resources (slide_37_img_01)](media/slide_37_img_01.jpeg)

**Figure 107:** [Slide 37] Cloud Shell provides command line access to resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_01 -->

* Cloud Shell provides instant command-line access to cloud resources directly from a
* browser. It is a Debian-based environment featuring a persistent 5-GB home directory,
* making it easy to manage Google Cloud projects without local setup. Because it
* comes pre-authenticated and pre-loaded with the Google Cloud SDK and popular
* tools, it's always updated and ready for immediate use.

---

<a id="slide-38-apis-allow-code-to-control-your-cloud-resources"></a>
### Slide 38: APIs allow code to control your Cloud resources

* Proprietary + Confidential

<!-- INJECT_START: slide_38_img_05 -->
![APIs allow code to control your Cloud resources (slide_38_img_05)](media/slide_38_img_05.jpeg)

**Figure 116:** [Slide 38] APIs allow code to control your Cloud resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_05 -->


<!-- INJECT_START: slide_38_img_02 -->
![APIs allow code to control your Cloud resources (slide_38_img_02)](media/slide_38_img_02.jpeg)

**Figure 113:** [Slide 38] APIs allow code to control your Cloud resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_02 -->


<!-- INJECT_START: slide_38_img_03 -->
![APIs allow code to control your Cloud resources (slide_38_img_03)](media/slide_38_img_03.jpeg)

**Figure 114:** [Slide 38] APIs allow code to control your Cloud resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_03 -->


<!-- INJECT_START: slide_38_img_04 -->
![APIs allow code to control your Cloud resources (slide_38_img_04)](media/slide_38_img_04.jpeg)

**Figure 115:** [Slide 38] APIs allow code to control your Cloud resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_04 -->

* Google Cloud services offer APIs that allow
* code to be written to control them
* The Google APIs Explorer shows what APIs
* are available, and in what versions
* Google provides Cloud Client and Google API
* Client libraries
* **Languages currently represented:**
* Java, Python, PHP, C#, Go, Node.js,
* Ruby and C++

<!-- INJECT_START: slide_38_img_01 -->
![APIs allow code to control your Cloud resources (slide_38_img_01)](media/slide_38_img_01.jpeg)

**Figure 112:** [Slide 38] APIs allow code to control your Cloud resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_01 -->

* The third way to access Google Cloud is through application programming interfaces,
* or APIs.
* The services that make up Google Cloud offer APIs, so that code you write can
* control them. The Google Cloud console includes a tool called the Google APIs
* Explorer that shows what APIs are available, and in what versions. You can try these
* APIs interactively, even those that require user authentication.
* Suppose you've explored an API, and you're ready to build an application that uses it.
* Do you have to start coding from scratch? No. Google provides Cloud Client and
* Google API  Client libraries in many popular languages to take a lot of the drudgery
* out of the task of calling Google Cloud from your code. Languages currently
* **represented in these libraries are:** Java, Python, PHP, C#, Go, Node.js, Ruby and C++.

---

<a id="slide-39-manage-your-resources-with-the-google-cloud-app"></a>
### Slide 39: Manage your resources with the Google Cloud app

* Proprietary + Confidential

<!-- INJECT_START: slide_39_img_02 -->
![Manage your resources with the Google Cloud app (slide_39_img_02)](media/slide_39_img_02.jpeg)

**Figure 118:** [Slide 39] Manage your resources with the Google Cloud app — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_02 -->

* Start, stop, and use SSH to connect into

<!-- INJECT_START: slide_39_img_03 -->
![Manage your resources with the Google Cloud app (slide_39_img_03)](media/slide_39_img_03.jpeg)

**Figure 119:** [Slide 39] Manage your resources with the Google Cloud app — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_03 -->


<!-- INJECT_START: slide_39_img_04 -->
![Manage your resources with the Google Cloud app (slide_39_img_04)](media/slide_39_img_04.jpeg)

**Figure 120:** [Slide 39] Manage your resources with the Google Cloud app — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_04 -->


<!-- INJECT_START: slide_39_img_05 -->
![Manage your resources with the Google Cloud app (slide_39_img_05)](media/slide_39_img_05.jpeg)

**Figure 121:** [Slide 39] Manage your resources with the Google Cloud app — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_05 -->

* Compute Engine instances, and see logs
* Stop and start Cloud SQL instances
* Administer applications deployed on App Engine
* Up-to-date billing information for projects and
* alerts for those going over budget
* Customizable graphs showing key metrics
* Alerts and incident management

<!-- INJECT_START: slide_39_img_01 -->
![Manage your resources with the Google Cloud app (slide_39_img_01)](media/slide_39_img_01.jpeg)

**Figure 117:** [Slide 39] Manage your resources with the Google Cloud app — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_01 -->

* And finally, the fourth way is with the Google Cloud app, which can be used to start,
* stop, and use SSH to connect to Compute Engine instances, and to see logs from
* each instance. It also lets you stop and start Cloud SQL instances. Additionally, you
* can administer applications deployed on App Engine, by viewing errors, rolling back
* deployments, and changing traffic splitting.
* The Google Cloud app provides up-to-date billing information for your projects,  and
* billing alerts for projects that are going over budget.
* You can set up customizable graphs showing key metrics such as CPU usage,
* network usage, requests per second, and server errors.
* The Google Cloud app also offers alerts and incident management.
* Download the Google Cloud app at cloud.google.com/app.

---

<a id="slide-40-module-quiz"></a>
### Slide 40: Module Quiz


<!-- INJECT_START: slide_40_img_02 -->
![Module Quiz (slide_40_img_02)](media/slide_40_img_02.jpeg)

**Figure 123:** [Slide 40] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_02 -->


<!-- INJECT_START: slide_40_img_01 -->
![Module Quiz (slide_40_img_01)](media/slide_40_img_01.jpeg)

**Figure 122:** [Slide 40] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_01 -->


---

<a id="slide-41-quiz-question-1"></a>
### Slide 41: Quiz | Question 1

* Proprietary + Confidential
* Question
* **Choose the correct completion:** Services and APIs are enabled on a per-__________ basis.
* A.
* Folder
* B.
* Project
* C.
* Organization
* D.
* Billing account

<!-- INJECT_START: slide_41_img_01 -->
![Quiz | Question 1 (slide_41_img_01)](media/slide_41_img_01.jpeg)

**Figure 124:** [Slide 41] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_41_img_01 -->


---

<a id="slide-42-quiz-question-1"></a>
### Slide 42: Quiz | Question 1

* Proprietary + Confidential
* Answer
* **Choose the correct completion:** Services and APIs are enabled on a per-__________ basis.
* A.
* Folder

<!-- INJECT_START: slide_42_img_02 -->
![Quiz | Question 1 (slide_42_img_02)](media/slide_42_img_02.jpeg)

**Figure 126:** [Slide 42] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_02 -->

* B.
* Project
* C.
* Organization
* D.
* Billing account

<!-- INJECT_START: slide_42_img_01 -->
![Quiz | Question 1 (slide_42_img_01)](media/slide_42_img_01.jpeg)

**Figure 125:** [Slide 42] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_01 -->

* **Choose the correct completion:** Services and APIs are enabled on a per-__________
* basis.
* **A:** Folder
* **Feedback:** Enable or disable APIs on a per-project basis.
* **B:** Project
* **Feedback:** Correct!
* **C:** Organization
* **Feedback:** Enable or disable APIs on a per-project basis.
* **D:** Billing account
* **Feedback:** Enable or disable APIs on a per-project basis.

---

<a id="slide-43-quiz-question-2"></a>
### Slide 43: Quiz | Question 2

* Proprietary + Confidential
* Question
* Select the list of IAM role types that are ordered from broadest to finest-grained.
* A.
* Custom roles, predefined roles, basic roles
* B.
* Predefined roles, custom roles, basic roles
* C.
* Basic roles, predefined roles, custom roles

<!-- INJECT_START: slide_43_img_01 -->
![Quiz | Question 2 (slide_43_img_01)](media/slide_43_img_01.jpeg)

**Figure 127:** [Slide 43] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_43_img_01 -->


---

<a id="slide-44-quiz-question-2"></a>
### Slide 44: Quiz | Question 2

* Proprietary + Confidential
* Answer
* Select the list of IAM role types that are ordered from broadest to finest-grained.
* A.
* Custom roles, predefined roles, basic roles
* B.
* Predefined roles, custom roles, basic roles

<!-- INJECT_START: slide_44_img_02 -->
![Quiz | Question 2 (slide_44_img_02)](media/slide_44_img_02.jpeg)

**Figure 129:** [Slide 44] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_02 -->

* C.
* Basic roles, predefined roles, custom roles

<!-- INJECT_START: slide_44_img_01 -->
![Quiz | Question 2 (slide_44_img_01)](media/slide_44_img_01.jpeg)

**Figure 128:** [Slide 44] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_01 -->

* Select the list of IAM role types that are ordered from broadest to finest-grained.
* **A:** Custom roles, predefined roles, basic roles
* **Feedback:** Basic roles affect all resources in a project.
* **B:** Predefined roles, custom roles, basic roles
* **Feedback:** Basic roles affect all resources in a project.
* **C:** Basic roles, predefined roles, custom roles
* **Feedback:** Correct!

---

<a id="slide-45-quiz-question-3"></a>
### Slide 45: Quiz | Question 3

* Proprietary + Confidential
* Question
* Which of these values is globally unique, permanent, and unchangeable, but can be
* modified by the customer during creation?
* A.
* The project name
* B.
* The project ID
* C.
* The project number
* D.
* The project's billing credit-card number

<!-- INJECT_START: slide_45_img_01 -->
![Quiz | Question 3 (slide_45_img_01)](media/slide_45_img_01.jpeg)

**Figure 130:** [Slide 45] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_45_img_01 -->


---

<a id="slide-46-quiz-question-3"></a>
### Slide 46: Quiz | Question 3

* Proprietary + Confidential
* Answer
* Which of these values is globally unique, permanent, and unchangeable, but can be
* modified by the customer during creation?
* A.
* The project name

<!-- INJECT_START: slide_46_img_02 -->
![Quiz | Question 3 (slide_46_img_02)](media/slide_46_img_02.jpeg)

**Figure 132:** [Slide 46] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_02 -->

* B.
* The project ID
* C.
* The project number
* D.
* The project's billing credit-card number

<!-- INJECT_START: slide_46_img_01 -->
![Quiz | Question 3 (slide_46_img_01)](media/slide_46_img_01.jpeg)

**Figure 131:** [Slide 46] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_01 -->

* Which of these values is globally unique, permanent, and unchangeable, but can be
* modified by the customer during creation?
* **A:** The project name
* **Feedback:** Review the lecture "The Google Cloud resource hierarchy."
* **B:** The project ID
* **Feedback:** Correct!  The project ID is immutable (cannot be changed) after creation,
* but can be changed during creation.
* **C:** The project number
* **Feedback:** Review the lecture "The Google Cloud resource hierarchy."
* **D:** The project's billing credit-card number
* **Feedback:** Review the lecture "The Google Cloud resource hierarchy.

---

<a id="slide-47-lab-intro"></a>
### Slide 47: Lab Intro

* Proprietary + Confidential

<!-- INJECT_START: slide_47_img_02 -->
![Lab Intro (slide_47_img_02)](media/slide_47_img_02.jpeg)

**Figure 134:** [Slide 47] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_02 -->

* Getting Started with Cloud Marketplace
* In this lab you use Cloud Marketplace to quickly
* and easily deploy a LAMP stack on a Compute
* Engine instance.
* The LAMP stack provides a complete web
* development environment for Linux that can be
* launched in one click.

<!-- INJECT_START: slide_47_img_01 -->
![Lab Intro (slide_47_img_01)](media/slide_47_img_01.jpeg)

**Figure 133:** [Slide 47] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_01 -->


---
