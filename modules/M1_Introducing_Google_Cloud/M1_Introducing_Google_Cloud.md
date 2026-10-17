# Google Cloud — Fundamentals:

### Comprehensive Technical Presentation & Study Guide

> **Course / Domain:** Computer Science & Engineering · **Academic Term:** Academic Lecture Series
> **Lecturer / Author:** Course Instructor · **Source:** Official Lecture Presentation Slides
> **Documentation Standard:** DTCM-v3 High-Fidelity Architecture (`ptcm-pdf-v1`)

---

## Table of Contents

* [Slide 1: Google Cloud  Fundamentals:  Core Infrastructure](#slide-1-google-cloud-fundamentals-core-infrastructure)
* [Slide 2: Introducing Google Cloud 01](#slide-2-introducing-google-cloud-01)
* [Slide 3: Introducing Google Cloud](#slide-3-introducing-google-cloud)
* [Slide 4: What is Cloud Computing?](#slide-4-what-is-cloud-computing)
* [Slide 5: 01](#slide-5-01)
* [Slide 6: 01](#slide-6-01)
* [Slide 7: 03](#slide-7-03)
* [Slide 8: 01](#slide-8-01)
* [Slide 9: 01](#slide-9-01)
* [Slide 10: 01](#slide-10-01)
* [Slide 11: The history of cloud computing](#slide-11-the-history-of-cloud-computing)
* [Slide 12: The history of cloud computing](#slide-12-the-history-of-cloud-computing)
* [Slide 13: Enterprises still maintain the infrastructure](#slide-13-enterprises-still-maintain-the-infrastructure)
* [Slide 14: The history of cloud computing](#slide-14-the-history-of-cloud-computing)
* [Slide 15: Third-wave cloud is available to Google customers](#slide-15-third-wave-cloud-is-available-to-google-customers)
* [Slide 16: Introducing Google Cloud](#slide-16-introducing-google-cloud)
* [Slide 17: Cloud service offerings](#slide-17-cloud-service-offerings)
* [Slide 18: Infrastructure as a Service (IaaS)](#slide-18-infrastructure-as-a-service-iaas)
* [Slide 19: Platform as a Service (PaaS)](#slide-19-platform-as-a-service-paas)
* [Slide 20: Payment models](#slide-20-payment-models)
* [Slide 21: The evolution of cloud computing](#slide-21-the-evolution-of-cloud-computing)
* [Slide 22: What about SaaS?](#slide-22-what-about-saas)
* [Slide 23: Introducing Google Cloud](#slide-23-introducing-google-cloud)
* [Slide 24: Largest network of its kind](#slide-24-largest-network-of-its-kind)
* [Slide 25: Designed for high throughput](#slide-25-designed-for-high-throughput)
* [Slide 26: Infrastructure locations](#slide-26-infrastructure-locations)
* [Slide 27: Geographic locations contain regions and zones](#slide-27-geographic-locations-contain-regions-and-zones)
* [Slide 28: Regions contain multiple zones](#slide-28-regions-contain-multiple-zones)
* [Slide 29: Zones are where Cloud resources are deployed](#slide-29-zones-are-where-cloud-resources-are-deployed)
* [Slide 30: Resources can run in different regions](#slide-30-resources-can-run-in-different-regions)
* [Slide 31: Some services can run in multiple geographic locations](#slide-31-some-services-can-run-in-multiple-geographic-locations)
* [Slide 32: cloud.google.com/about/locations 130 43](#slide-32-cloudgooglecomaboutlocations-130-43)
* [Slide 33: Introducing Google Cloud](#slide-33-introducing-google-cloud)
* [Slide 34: 2%](#slide-34-2)
* [Slide 35: Google aims to improve efficiency and reduce waste](#slide-35-google-aims-to-improve-efficiency-and-reduce-waste)
* [Slide 36: Google's data center in Hamina, Finland](#slide-36-googles-data-center-in-hamina-finland)
* [Slide 37: Google's commitment to sustainability](#slide-37-googles-commitment-to-sustainability)
* [Slide 38: Introducing Google Cloud](#slide-38-introducing-google-cloud)
* [Slide 39: Google Cloud is  designed with  security in mind](#slide-39-google-cloud-is-designed-with-security-in-mind)
* [Slide 40: Hardware  infrastructure level](#slide-40-hardware-infrastructure-level)
* [Slide 41: Hardware  infrastructure level](#slide-41-hardware-infrastructure-level)
* [Slide 42: Service  Deployment level](#slide-42-service-deployment-level)
* [Slide 43: Service  deployment level](#slide-43-service-deployment-level)
* [Slide 44: User identity level](#slide-44-user-identity-level)
* [Slide 45: User  identity level](#slide-45-user-identity-level)
* [Slide 46: Storage  services level](#slide-46-storage-services-level)
* [Slide 47: Storage  services level](#slide-47-storage-services-level)
* [Slide 48: Internet  communication level](#slide-48-internet-communication-level)
* [Slide 49: Denial of Service ("DoS") protection Internet  communication level](#slide-49-denial-of-service-dos-protection-internet-communication-level)
* [Slide 50: Operational  security level](#slide-50-operational-security-level)
* [Slide 51: Operational  security level](#slide-51-operational-security-level)
* [Slide 52: cloud.google.com/security/security-design](#slide-52-cloudgooglecomsecuritysecurity-design)
* [Slide 53: Introducing Google Cloud](#slide-53-introducing-google-cloud)
* [Slide 54: Google Cloud is open-source friendly](#slide-54-google-cloud-is-open-source-friendly)
* [Slide 55: Open-source TensorFlow works with Google Cloud](#slide-55-open-source-tensorflow-works-with-google-cloud)
* [Slide 56: Interoperability at multiple layers of the stack](#slide-56-interoperability-at-multiple-layers-of-the-stack)
* [Slide 57: Introducing Google Cloud](#slide-57-introducing-google-cloud)
* [Slide 58: Google Compute products are billed per-second](#slide-58-google-compute-products-are-billed-per-second)
* [Slide 59: Compute Engine offers billing flexibility](#slide-59-compute-engine-offers-billing-flexibility)
* [Slide 60: Google Cloud Pricing Calculator](#slide-60-google-cloud-pricing-calculator)
* [Slide 61: Billing tools help to budget and monitor usage](#slide-61-billing-tools-help-to-budget-and-monitor-usage)
* [Slide 62: Quotas are allocated at project-level](#slide-62-quotas-are-allocated-at-project-level)
* [Slide 63: Module Quiz](#slide-63-module-quiz)
* [Slide 64: Quiz | Question 1](#slide-64-quiz-question-1)
* [Slide 65: Quiz | Question 1](#slide-65-quiz-question-1)
* [Slide 66: Quiz | Question 2](#slide-66-quiz-question-2)
* [Slide 67: Quiz | Question 2](#slide-67-quiz-question-2)
* [Slide 68: Feedback: Incorrect. While virtualization is a technology that powers cloud  computing, it is not a cloud service model. This describes a physical infrastructure  setup, often on-premises.](#slide-68-feedback-incorrect-while-virtualization-is-a-technology-that-powers-cloud-computing-it-is-not-a-cloud-service-model-this-describes-a-physical-infrastructure-setup-often-on-premises)
* [Slide 69: Quiz | Question 3](#slide-69-quiz-question-3)
* [Slide 70: Quiz | Question 3](#slide-70-quiz-question-3)

---

## List of Figures

* **Figure 1:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 2:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 3:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 4:** [Slide 2] Introducing Google Cloud 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 5:** [Slide 2] Introducing Google Cloud 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 6:** [Slide 3] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 7:** [Slide 3] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 8:** [Slide 4] What is Cloud Computing? — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 9:** [Slide 4] What is Cloud Computing? — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 10:** [Slide 5] 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 11:** [Slide 6] 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 12:** [Slide 7] 03 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 13:** [Slide 8] 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 14:** [Slide 9] 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 15:** [Slide 10] 01 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 16:** [Slide 11] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 17:** [Slide 11] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 18:** [Slide 12] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 19:** [Slide 12] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 20:** [Slide 13] Enterprises still maintain the infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 21:** [Slide 13] Enterprises still maintain the infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 22:** [Slide 13] Enterprises still maintain the infrastructure — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 23:** [Slide 14] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 24:** [Slide 14] The history of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 25:** [Slide 15] Third-wave cloud is available to Google customers — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 26:** [Slide 15] Third-wave cloud is available to Google customers — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 27:** [Slide 16] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 28:** [Slide 16] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 29:** [Slide 17] Cloud service offerings — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 30:** [Slide 17] Cloud service offerings — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 31:** [Slide 17] Cloud service offerings — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 32:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 33:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 34:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 35:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 36:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 37:** [Slide 18] Infrastructure as a Service (IaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 38:** [Slide 19] Platform as a Service (PaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 39:** [Slide 19] Platform as a Service (PaaS) — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 40:** [Slide 20] Payment models — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 41:** [Slide 20] Payment models — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 42:** [Slide 21] The evolution of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 43:** [Slide 21] The evolution of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 44:** [Slide 21] The evolution of cloud computing — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 45:** [Slide 22] What about SaaS? — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 46:** [Slide 22] What about SaaS? — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 47:** [Slide 23] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 48:** [Slide 23] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 49:** [Slide 24] Largest network of its kind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 50:** [Slide 24] Largest network of its kind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 51:** [Slide 25] Designed for high throughput — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 52:** [Slide 25] Designed for high throughput — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 53:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 54:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 55:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 56:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 57:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 58:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 59:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 60:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 61:** [Slide 26] Infrastructure locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 62:** [Slide 27] Geographic locations contain regions and zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 63:** [Slide 27] Geographic locations contain regions and zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 64:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 65:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 66:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 67:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 68:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 69:** [Slide 28] Regions contain multiple zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 70:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 71:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 72:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 73:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 74:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 75:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 76:** [Slide 29] Zones are where Cloud resources are deployed — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 77:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 78:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 79:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 80:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 81:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 82:** [Slide 30] Resources can run in different regions — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 83:** [Slide 31] Some services can run in multiple geographic locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 84:** [Slide 31] Some services can run in multiple geographic locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 85:** [Slide 31] Some services can run in multiple geographic locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 86:** [Slide 31] Some services can run in multiple geographic locations — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 87:** [Slide 32] cloud.google.com/about/locations 130 43 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 88:** [Slide 32] cloud.google.com/about/locations 130 43 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 89:** [Slide 32] cloud.google.com/about/locations 130 43 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 90:** [Slide 33] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 91:** [Slide 33] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 92:** [Slide 34] 2% — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 93:** [Slide 34] 2% — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 94:** [Slide 35] Google aims to improve efficiency and reduce waste — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 95:** [Slide 35] Google aims to improve efficiency and reduce waste — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 96:** [Slide 36] Google's data center in Hamina, Finland — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 97:** [Slide 36] Google's data center in Hamina, Finland — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 98:** [Slide 37] Google's commitment to sustainability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 99:** [Slide 37] Google's commitment to sustainability — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 100:** [Slide 38] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 101:** [Slide 38] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 102:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 103:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 104:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 105:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 106:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 107:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 108:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 109:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 110:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 111:** [Slide 39] Google Cloud is  designed with  security in mind — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 112:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 113:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 114:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 115:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 116:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 117:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 118:** [Slide 40] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 119:** [Slide 41] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 120:** [Slide 41] Hardware  infrastructure level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 121:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 122:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 123:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 124:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 125:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 126:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 127:** [Slide 42] Service  Deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 128:** [Slide 43] Service  deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 129:** [Slide 43] Service  deployment level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 130:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 131:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 132:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 133:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 134:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 135:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 136:** [Slide 44] User identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 137:** [Slide 45] User  identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 138:** [Slide 45] User  identity level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 139:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 140:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 141:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 142:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 143:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 144:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 145:** [Slide 46] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 146:** [Slide 47] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 147:** [Slide 47] Storage  services level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 148:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 149:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 150:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 151:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 152:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 153:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 154:** [Slide 48] Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 155:** [Slide 49] Denial of Service ("DoS") protection Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 156:** [Slide 49] Denial of Service ("DoS") protection Internet  communication level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 157:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 158:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 159:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 160:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 161:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 162:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 163:** [Slide 50] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 164:** [Slide 51] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 165:** [Slide 51] Operational  security level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 166:** [Slide 52] cloud.google.com/security/security-design — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 167:** [Slide 53] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 168:** [Slide 53] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 169:** [Slide 54] Google Cloud is open-source friendly — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 170:** [Slide 54] Google Cloud is open-source friendly — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 171:** [Slide 55] Open-source TensorFlow works with Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 172:** [Slide 55] Open-source TensorFlow works with Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 173:** [Slide 56] Interoperability at multiple layers of the stack — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 174:** [Slide 56] Interoperability at multiple layers of the stack — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 175:** [Slide 56] Interoperability at multiple layers of the stack — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 176:** [Slide 56] Interoperability at multiple layers of the stack — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 177:** [Slide 57] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 178:** [Slide 57] Introducing Google Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 179:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 180:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 181:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 182:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 183:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 184:** [Slide 58] Google Compute products are billed per-second — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 185:** [Slide 59] Compute Engine offers billing flexibility — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 186:** [Slide 59] Compute Engine offers billing flexibility — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 187:** [Slide 59] Compute Engine offers billing flexibility — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 188:** [Slide 60] Google Cloud Pricing Calculator — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 189:** [Slide 60] Google Cloud Pricing Calculator — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 190:** [Slide 61] Billing tools help to budget and monitor usage — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 191:** [Slide 61] Billing tools help to budget and monitor usage — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 192:** [Slide 62] Quotas are allocated at project-level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 193:** [Slide 62] Quotas are allocated at project-level — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 194:** [Slide 63] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 195:** [Slide 63] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 196:** [Slide 64] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 197:** [Slide 65] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 198:** [Slide 65] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 199:** [Slide 66] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 200:** [Slide 67] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 201:** [Slide 67] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 202:** [Slide 69] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 203:** [Slide 70] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 204:** [Slide 70] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)

---

<a id="slide-1-google-cloud-fundamentals-core-infrastructure"></a>
### Slide 1: Google Cloud  Fundamentals:  Core Infrastructure

* Proprietary + Confidential

<!-- INJECT_START: slide_01_img_02 -->
![Google Cloud  Fundamentals:  Core Infrastructure (slide_01_img_02)](media/slide_01_img_02.jpeg)

**Figure 2:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_02 -->


<!-- INJECT_START: slide_01_img_03 -->
![Google Cloud  Fundamentals:  Core Infrastructure (slide_01_img_03)](media/slide_01_img_03.jpeg)

**Figure 3:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_03 -->

* Google Cloud
* **Fundamentals:**
* Core Infrastructure
* Instructor-led training

<!-- INJECT_START: slide_01_img_01 -->
![Google Cloud  Fundamentals:  Core Infrastructure (slide_01_img_01)](media/slide_01_img_01.jpeg)

**Figure 1:** [Slide 1] Google Cloud  Fundamentals:  Core Infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_01 -->


---

<a id="slide-2-introducing-google-cloud-01"></a>
### Slide 2: Introducing Google Cloud 01

* Proprietary + Confidential

<!-- INJECT_START: slide_02_img_02 -->
![Introducing Google Cloud 01 (slide_02_img_02)](media/slide_02_img_02.jpeg)

**Figure 5:** [Slide 2] Introducing Google Cloud 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_02 -->

* Introducing
* Google Cloud
* 01

<!-- INJECT_START: slide_02_img_01 -->
![Introducing Google Cloud 01 (slide_02_img_01)](media/slide_02_img_01.jpeg)

**Figure 4:** [Slide 2] Introducing Google Cloud 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_01 -->


---

<a id="slide-3-introducing-google-cloud"></a>
### Slide 3: Introducing Google Cloud


<!-- INJECT_START: slide_03_img_02 -->
![Introducing Google Cloud (slide_03_img_02)](media/slide_03_img_02.jpeg)

**Figure 7:** [Slide 3] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_03_img_01 -->
![Introducing Google Cloud (slide_03_img_01)](media/slide_03_img_01.jpeg)

**Figure 6:** [Slide 3] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_01 -->

* Let's start at the beginning with an overview of cloud computing. Some of you might
* **be wondering about the basics:** What exactly is Google Cloud? How is it organized?
* And what makes it unique?
* In this module, we'll answer those questions.

---

<a id="slide-4-what-is-cloud-computing"></a>
### Slide 4: What is Cloud Computing?

* Proprietary + Confidential

<!-- INJECT_START: slide_04_img_02 -->
![What is Cloud Computing? (slide_04_img_02)](media/slide_04_img_02.jpeg)

**Figure 9:** [Slide 4] What is Cloud Computing? — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_02 -->


<!-- INJECT_START: slide_04_img_01 -->
![What is Cloud Computing? (slide_04_img_01)](media/slide_04_img_01.jpeg)

**Figure 8:** [Slide 4] What is Cloud Computing? — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_01 -->

* The cloud is a hot topic these days, but what exactly is it?
* The US National Institute of Standards and Technology created the term cloud
* computing, although, there is nothing US-specific about it.

---

<a id="slide-5-01"></a>
### Slide 5: 01

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 02
* Customers get access to those resources
* over the internet, from anywhere
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* 03
* The provider of those resources allocates
* them to users out of that pool
* 04
  * The resources are elasticwhich means
  * they're flexible, so customers can be
* 05
* Customers pay only for what they use,
* or reserve as they go

<!-- INJECT_START: slide_05_img_01 -->
![01 (slide_05_img_01)](media/slide_05_img_01.jpeg)

**Figure 10:** [Slide 5] 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_01 -->

* Cloud computing is a way of using information technology (IT) that has these five
* equally important traits.

---

<a id="slide-6-01"></a>
### Slide 6: 01

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 02
* Customers get access to those resources
* over the internet, from anywhere
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* 03
* The provider of those resources allocates
* them to users out of that pool
* 04
  * The resources are elasticwhich means
  * they're flexible, so customers can be
* 05
* Customers pay only for what they use,
* or reserve as they go

<!-- INJECT_START: slide_06_img_01 -->
![01 (slide_06_img_01)](media/slide_06_img_01.jpeg)

**Figure 11:** [Slide 6] 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_01 -->

* First, customers get computing resources that are on-demand and self-service.
* Through a web interface, users get the processing power, storage, and network they
* need with no need for human intervention.

---

<a id="slide-7-03"></a>
### Slide 7: 03

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 01
* Customers get access to those resources
* over the internet, from anywhere
* 02
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* The provider of those resources allocates
* them to users out of that pool
* 04
  * The resources are elasticwhich means
  * they're flexible, so customers can be
* 05
* Customers pay only for what they use,
* or reserve as they go

<!-- INJECT_START: slide_07_img_01 -->
![03 (slide_07_img_01)](media/slide_07_img_01.jpeg)

**Figure 12:** [Slide 7] 03 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_01 -->

* Second, customers get access to those resources over the internet, from anywhere
* they have a connection.

---

<a id="slide-8-01"></a>
### Slide 8: 01

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 02
* Customers get access to those resources
* over the internet, from anywhere
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* The provider of those resources allocates
* them to users out of that pool
* 03
* 04
  * The resources are elasticwhich means
  * they're flexible, so customers can be
* 05
* Customers pay only for what they use,
* or reserve as they go

<!-- INJECT_START: slide_08_img_01 -->
![01 (slide_08_img_01)](media/slide_08_img_01.jpeg)

**Figure 13:** [Slide 8] 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_01 -->

* Third, the provider of those resources has a big pool of them, and allocates them to
* users out of that pool. That allows the provider to buy in bulk and pass the savings on
* to the customers. Customers don't have to know or care about the exact physical
* location of those resources.

---

<a id="slide-9-01"></a>
### Slide 9: 01

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 02
* Customers get access to those resources
* over the internet, from anywhere
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* 03
* The provider of those resources allocates
* them to users out of that pool
  * The resources are elasticwhich means
  * they're flexible, so customers can be
  * 04
* 05
* Customers pay only for what they use,
* or reserve as they go

<!-- INJECT_START: slide_09_img_01 -->
![01 (slide_09_img_01)](media/slide_09_img_01.jpeg)

**Figure 14:** [Slide 9] 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_01 -->

  * Fourth, the resources are elasticwhich means they're flexible, so customers can be.
  * If they need more resources they can get more, and quickly. If they need less, they can
  * scale back.

---

<a id="slide-10-01"></a>
### Slide 10: 01

* Proprietary + Confidential
* Five traits of cloud
* computing
* Customers get computing resources that
* are on-demand and self-service
* 02
* Customers get access to those resources
* over the internet, from anywhere
* Cloud computing is a way of
* using information technology
* that has these five equally
* important traits.
* 03
* The provider of those resources allocates
* them to users out of that pool
* 04
  * The resources are elasticwhich means
  * they're flexible, so customers can be
* Customers pay only for what they use,
* or reserve as they go
* 05

<!-- INJECT_START: slide_10_img_01 -->
![01 (slide_10_img_01)](media/slide_10_img_01.jpeg)

**Figure 15:** [Slide 10] 01 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_01 -->

* And finally, the customers pay only for what they use, or reserve as they go. If they
* stop using resources, they stop paying.
* That's it. That's the definition of cloud.

---

<a id="slide-11-the-history-of-cloud-computing"></a>
### Slide 11: The history of cloud computing

* Proprietary + Confidential

<!-- INJECT_START: slide_11_img_02 -->
![The history of cloud computing (slide_11_img_02)](media/slide_11_img_02.jpeg)

**Figure 17:** [Slide 11] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_02 -->


<!-- INJECT_START: slide_11_img_01 -->
![The history of cloud computing (slide_11_img_01)](media/slide_11_img_01.jpeg)

**Figure 16:** [Slide 11] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_01 -->

* But why is the cloud model so compelling nowadays? To understand why, we need to
* look at some history.
* The trend towards cloud computing started with a first wave with something called
* colocation. Colocation gave users the financial efficiency of renting physical space,
* instead of investing in data center real estate.

---

<a id="slide-12-the-history-of-cloud-computing"></a>
### Slide 12: The history of cloud computing

* Proprietary + Confidential

<!-- INJECT_START: slide_12_img_02 -->
![The history of cloud computing (slide_12_img_02)](media/slide_12_img_02.jpeg)

**Figure 19:** [Slide 12] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_02 -->


<!-- INJECT_START: slide_12_img_01 -->
![The history of cloud computing (slide_12_img_01)](media/slide_12_img_01.jpeg)

**Figure 18:** [Slide 12] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_01 -->

  * Virtualized data centers of today, which is the second wave, share similarities with the
  * private data centers and colocation facilities of decades past. The components of
  * virtualized data centers match the physical building blocks of hosted
  * computingservers, CPUs, disks, load balancers, and so onbut now they're virtual
  * devices.

---

<a id="slide-13-enterprises-still-maintain-the-infrastructure"></a>
### Slide 13: Enterprises still maintain the infrastructure

* Proprietary + Confidential

<!-- INJECT_START: slide_13_img_02 -->
![Enterprises still maintain the infrastructure (slide_13_img_02)](media/slide_13_img_02.jpeg)

**Figure 21:** [Slide 13] Enterprises still maintain the infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_02 -->


<!-- INJECT_START: slide_13_img_03 -->
![Enterprises still maintain the infrastructure (slide_13_img_03)](media/slide_13_img_03.jpeg)

**Figure 22:** [Slide 13] Enterprises still maintain the infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_03 -->


<!-- INJECT_START: slide_13_img_01 -->
![Enterprises still maintain the infrastructure (slide_13_img_01)](media/slide_13_img_01.jpeg)

**Figure 20:** [Slide 13] Enterprises still maintain the infrastructure — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_01 -->

* With virtualization, enterprises still maintained the infrastructure; it's still a
* user-controlled and user-configured environment.

---

<a id="slide-14-the-history-of-cloud-computing"></a>
### Slide 14: The history of cloud computing

* Proprietary + Confidential

<!-- INJECT_START: slide_14_img_02 -->
![The history of cloud computing (slide_14_img_02)](media/slide_14_img_02.jpeg)

**Figure 24:** [Slide 14] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_02 -->


<!-- INJECT_START: slide_14_img_01 -->
![The history of cloud computing (slide_14_img_01)](media/slide_14_img_01.jpeg)

**Figure 23:** [Slide 14] The history of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_01 -->

  * Several years ago, Google realized that its business couldn't move fast enough within
  * the confines of the virtualization model. So Google switched to a container-based
  * architecturea fully automated, elastic third-wave cloud that consists of a
  * combination of automated services and scalable data. Services automatically
  * provision and configure the infrastructure used to run applications.

---

<a id="slide-15-third-wave-cloud-is-available-to-google-customers"></a>
### Slide 15: Third-wave cloud is available to Google customers

* Proprietary + Confidential

<!-- INJECT_START: slide_15_img_02 -->
![Third-wave cloud is available to Google customers (slide_15_img_02)](media/slide_15_img_02.jpeg)

**Figure 26:** [Slide 15] Third-wave cloud is available to Google customers — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_02 -->


<!-- INJECT_START: slide_15_img_01 -->
![Third-wave cloud is available to Google customers (slide_15_img_01)](media/slide_15_img_01.jpeg)

**Figure 25:** [Slide 15] Third-wave cloud is available to Google customers — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_01 -->

* Today, Google Cloud makes this third-wave cloud available to Google customers.
  * Google believes that, in the future, every companyregardless of size or industrywill
  * differentiate itself from its competitors through technology. Increasingly, that
  * technology will be in the form of software. Great software is based on high-quality
  * data. This means that every company is, or will eventually become, a data company.

---

<a id="slide-16-introducing-google-cloud"></a>
### Slide 16: Introducing Google Cloud


<!-- INJECT_START: slide_16_img_02 -->
![Introducing Google Cloud (slide_16_img_02)](media/slide_16_img_02.jpeg)

**Figure 28:** [Slide 16] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_16_img_01 -->
![Introducing Google Cloud (slide_16_img_01)](media/slide_16_img_01.jpeg)

**Figure 27:** [Slide 16] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_01 -->


---

<a id="slide-17-cloud-service-offerings"></a>
### Slide 17: Cloud service offerings


<!-- INJECT_START: slide_17_img_02 -->
![Cloud service offerings (slide_17_img_02)](media/slide_17_img_02.jpeg)

**Figure 30:** [Slide 17] Cloud service offerings — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_02 -->


<!-- INJECT_START: slide_17_img_03 -->
![Cloud service offerings (slide_17_img_03)](media/slide_17_img_03.jpeg)

**Figure 31:** [Slide 17] Cloud service offerings — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_03 -->


<!-- INJECT_START: slide_17_img_01 -->
![Cloud service offerings (slide_17_img_01)](media/slide_17_img_01.jpeg)

**Figure 29:** [Slide 17] Cloud service offerings — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_01 -->

* This move to virtualized data centers introduced customers to two new types of
* **offerings:** infrastructure as a service, commonly referred to as IaaS, and platform as a
* service, or PaaS.

---

<a id="slide-18-infrastructure-as-a-service-iaas"></a>
### Slide 18: Infrastructure as a Service (IaaS)


<!-- INJECT_START: slide_18_img_06 -->
![Infrastructure as a Service (IaaS) (slide_18_img_06)](media/slide_18_img_06.jpeg)

**Figure 37:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_06 -->


<!-- INJECT_START: slide_18_img_05 -->
![Infrastructure as a Service (IaaS) (slide_18_img_05)](media/slide_18_img_05.jpeg)

**Figure 36:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_05 -->


<!-- INJECT_START: slide_18_img_02 -->
![Infrastructure as a Service (IaaS) (slide_18_img_02)](media/slide_18_img_02.jpeg)

**Figure 33:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_02 -->


<!-- INJECT_START: slide_18_img_04 -->
![Infrastructure as a Service (IaaS) (slide_18_img_04)](media/slide_18_img_04.jpeg)

**Figure 35:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_04 -->


<!-- INJECT_START: slide_18_img_03 -->
![Infrastructure as a Service (IaaS) (slide_18_img_03)](media/slide_18_img_03.jpeg)

**Figure 34:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_03 -->


<!-- INJECT_START: slide_18_img_01 -->
![Infrastructure as a Service (IaaS) (slide_18_img_01)](media/slide_18_img_01.jpeg)

**Figure 32:** [Slide 18] Infrastructure as a Service (IaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_01 -->

* IaaS offerings provide raw compute, storage, and network capabilities, organized
* virtually into resources that are similar to physical data centers.
* Compute Engine is an example of a Google Cloud IaaS service.

---

<a id="slide-19-platform-as-a-service-paas"></a>
### Slide 19: Platform as a Service (PaaS)

* Proprietary + Confidential

<!-- INJECT_START: slide_19_img_02 -->
![Platform as a Service (PaaS) (slide_19_img_02)](media/slide_19_img_02.jpeg)

**Figure 39:** [Slide 19] Platform as a Service (PaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_02 -->


<!-- INJECT_START: slide_19_img_01 -->
![Platform as a Service (PaaS) (slide_19_img_01)](media/slide_19_img_01.jpeg)

**Figure 38:** [Slide 19] Platform as a Service (PaaS) — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_01 -->

* PaaS offerings, on the other hand, bind code to libraries that provide access to the
* infrastructure application needs. This allows more resources to be focused on
* application logic.
* App Engine is an example of a Google Cloud PaaS service.

---

<a id="slide-20-payment-models"></a>
### Slide 20: Payment models


<!-- INJECT_START: slide_20_img_02 -->
![Payment models (slide_20_img_02)](media/slide_20_img_02.jpeg)

**Figure 41:** [Slide 20] Payment models — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_02 -->


<!-- INJECT_START: slide_20_img_01 -->
![Payment models (slide_20_img_01)](media/slide_20_img_01.jpeg)

**Figure 40:** [Slide 20] Payment models — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_01 -->

* In the IaaS model, customers pay for the resources they allocate ahead of time; in the
* PaaS model, customers pay for the resources they actually use.

---

<a id="slide-21-the-evolution-of-cloud-computing"></a>
### Slide 21: The evolution of cloud computing

* Proprietary + Confidential

<!-- INJECT_START: slide_21_img_02 -->
![The evolution of cloud computing (slide_21_img_02)](media/slide_21_img_02.jpeg)

**Figure 43:** [Slide 21] The evolution of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_02 -->


<!-- INJECT_START: slide_21_img_03 -->
![The evolution of cloud computing (slide_21_img_03)](media/slide_21_img_03.jpeg)

**Figure 44:** [Slide 21] The evolution of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_03 -->


<!-- INJECT_START: slide_21_img_01 -->
![The evolution of cloud computing (slide_21_img_01)](media/slide_21_img_01.jpeg)

**Figure 42:** [Slide 21] The evolution of cloud computing — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_01 -->

* As cloud computing has evolved, the momentum has shifted toward managed
* infrastructure and managed services.
* Leveraging managed resources and services allows companies to concentrate more
* on their business goals and spend less time and money on creating and maintaining
* their technical infrastructure. It allows companies to deliver products and services to
* their customers more quickly and reliably.
* Although not shown on this slide, serverless is yet another step in the evolution of
* cloud computing.  Serverless computing allows developers to concentrate on their
* code, rather than on server configuration, by eliminating the need for any
* infrastructure management.  Serverless technologies offered by Google include Cloud
* Run, which allows customers to deploy their containerized microservices based
* application in a fully-managed environment, and Cloud Run functions, which manages
* event-driven code as a pay-as-you-go service.

---

<a id="slide-22-what-about-saas"></a>
### Slide 22: What about SaaS?

* Proprietary + Confidential

<!-- INJECT_START: slide_22_img_02 -->
![What about SaaS? (slide_22_img_02)](media/slide_22_img_02.jpeg)

**Figure 46:** [Slide 22] What about SaaS? — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_02 -->


<!-- INJECT_START: slide_22_img_01 -->
![What about SaaS? (slide_22_img_01)](media/slide_22_img_01.jpeg)

**Figure 45:** [Slide 22] What about SaaS? — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_01 -->

* You might have heard about Software as a Service (SaaS) and wondered what it is
* and how it fits into the Cloud ecosphere.
* Software as a Service applications are not installed on your local computer - they run
* in the cloud as a service and are consumed directly over the internet by end users.
* Google's popular applications like Gmail, Docs, and Drive, collectively known as
* Google Workspace, are all classified as SaaS.
* You can learn more about these products or our other course offerings, but they are
* outside the scope of this particular course.

---

<a id="slide-23-introducing-google-cloud"></a>
### Slide 23: Introducing Google Cloud


<!-- INJECT_START: slide_23_img_02 -->
![Introducing Google Cloud (slide_23_img_02)](media/slide_23_img_02.jpeg)

**Figure 48:** [Slide 23] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_23_img_01 -->
![Introducing Google Cloud (slide_23_img_01)](media/slide_23_img_01.jpeg)

**Figure 47:** [Slide 23] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_01 -->

* Now that we've learned about or had a refresher on the basics of cloud computing,
* let's explore Google's own network that Google Cloud runs on.

---

<a id="slide-24-largest-network-of-its-kind"></a>
### Slide 24: Largest network of its kind

* Proprietary + Confidential

<!-- INJECT_START: slide_24_img_02 -->
![Largest network of its kind (slide_24_img_02)](media/slide_24_img_02.jpeg)

**Figure 50:** [Slide 24] Largest network of its kind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_24_img_02 -->


<!-- INJECT_START: slide_24_img_01 -->
![Largest network of its kind (slide_24_img_01)](media/slide_24_img_01.jpeg)

**Figure 49:** [Slide 24] Largest network of its kind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_24_img_01 -->

* Google's network is the largest network of its kind, and Google has invested billions of
* dollars over the years to build it.

---

<a id="slide-25-designed-for-high-throughput"></a>
### Slide 25: Designed for high throughput

* Proprietary + Confidential

<!-- INJECT_START: slide_25_img_02 -->
![Designed for high throughput (slide_25_img_02)](media/slide_25_img_02.jpeg)

**Figure 52:** [Slide 25] Designed for high throughput — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_02 -->


<!-- INJECT_START: slide_25_img_01 -->
![Designed for high throughput (slide_25_img_01)](media/slide_25_img_01.jpeg)

**Figure 51:** [Slide 25] Designed for high throughput — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_01 -->

  * Google's global network is designed to give customers the highest possible
  * throughput and lowest possible latencies for their applications by leveraging more
  * than 100 content caching nodes worldwidewhich are locations where high demand
  * content is cached for quicker accessto respond to user requests from the location
  * that will provide the quickest response time.
* Google Cloud's locations underpin all of the important work we do for our customers.
* From redundant cloud regions to high-bandwidth connectivity via subsea cables,
* every aspect of our infrastructure is designed to deliver your services to your users, no
* matter where they are around the world.

---

<a id="slide-26-infrastructure-locations"></a>
### Slide 26: Infrastructure locations

* Proprietary + Confidential

<!-- INJECT_START: slide_26_img_02 -->
![Infrastructure locations (slide_26_img_02)](media/slide_26_img_02.jpeg)

**Figure 54:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_02 -->


<!-- INJECT_START: slide_26_img_06 -->
![Infrastructure locations (slide_26_img_06)](media/slide_26_img_06.jpeg)

**Figure 58:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_06 -->


<!-- INJECT_START: slide_26_img_03 -->
![Infrastructure locations (slide_26_img_03)](media/slide_26_img_03.jpeg)

**Figure 55:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_03 -->


<!-- INJECT_START: slide_26_img_05 -->
![Infrastructure locations (slide_26_img_05)](media/slide_26_img_05.jpeg)

**Figure 57:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_05 -->


<!-- INJECT_START: slide_26_img_08 -->
![Infrastructure locations (slide_26_img_08)](media/slide_26_img_08.jpeg)

**Figure 60:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_08 -->


<!-- INJECT_START: slide_26_img_04 -->
![Infrastructure locations (slide_26_img_04)](media/slide_26_img_04.jpeg)

**Figure 56:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_04 -->


<!-- INJECT_START: slide_26_img_09 -->
![Infrastructure locations (slide_26_img_09)](media/slide_26_img_09.jpeg)

**Figure 61:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_09 -->


<!-- INJECT_START: slide_26_img_07 -->
![Infrastructure locations (slide_26_img_07)](media/slide_26_img_07.jpeg)

**Figure 59:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_07 -->


<!-- INJECT_START: slide_26_img_01 -->
![Infrastructure locations (slide_26_img_01)](media/slide_26_img_01.jpeg)

**Figure 53:** [Slide 26] Infrastructure locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_01 -->

* Google Cloud's infrastructure is based in seven major geographic locations: North
* America, South America, Europe, Africa, the Middle East, Asia, and Australia. Having
* multiple service locations is important because choosing where to locate applications
* affects qualities like availability, durability, and latency, the latter of which measures
* the time a packet of information takes to travel from its source to its destination.

---

<a id="slide-27-geographic-locations-contain-regions-and-zones"></a>
### Slide 27: Geographic locations contain regions and zones

* Proprietary + Confidential

<!-- INJECT_START: slide_27_img_02 -->
![Geographic locations contain regions and zones (slide_27_img_02)](media/slide_27_img_02.jpeg)

**Figure 63:** [Slide 27] Geographic locations contain regions and zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_02 -->

* Zones
* Regions
* Location

<!-- INJECT_START: slide_27_img_01 -->
![Geographic locations contain regions and zones (slide_27_img_01)](media/slide_27_img_01.jpeg)

**Figure 62:** [Slide 27] Geographic locations contain regions and zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_01 -->

* Each of these locations are divided into a number of different regions and zones.

---

<a id="slide-28-regions-contain-multiple-zones"></a>
### Slide 28: Regions contain multiple zones


<!-- INJECT_START: slide_28_img_06 -->
![Regions contain multiple zones (slide_28_img_06)](media/slide_28_img_06.jpeg)

**Figure 69:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_06 -->


<!-- INJECT_START: slide_28_img_02 -->
![Regions contain multiple zones (slide_28_img_02)](media/slide_28_img_02.jpeg)

**Figure 65:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_02 -->


<!-- INJECT_START: slide_28_img_03 -->
![Regions contain multiple zones (slide_28_img_03)](media/slide_28_img_03.jpeg)

**Figure 66:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_03 -->


<!-- INJECT_START: slide_28_img_04 -->
![Regions contain multiple zones (slide_28_img_04)](media/slide_28_img_04.jpeg)

**Figure 67:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_04 -->


<!-- INJECT_START: slide_28_img_05 -->
![Regions contain multiple zones (slide_28_img_05)](media/slide_28_img_05.jpeg)

**Figure 68:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_05 -->


<!-- INJECT_START: slide_28_img_01 -->
![Regions contain multiple zones (slide_28_img_01)](media/slide_28_img_01.jpeg)

**Figure 64:** [Slide 28] Regions contain multiple zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_01 -->


---

<a id="slide-29-zones-are-where-cloud-resources-are-deployed"></a>
### Slide 29: Zones are where Cloud resources are deployed


<!-- INJECT_START: slide_29_img_03 -->
![Zones are where Cloud resources are deployed (slide_29_img_03)](media/slide_29_img_03.jpeg)

**Figure 72:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_03 -->


<!-- INJECT_START: slide_29_img_02 -->
![Zones are where Cloud resources are deployed (slide_29_img_02)](media/slide_29_img_02.jpeg)

**Figure 71:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_02 -->


<!-- INJECT_START: slide_29_img_05 -->
![Zones are where Cloud resources are deployed (slide_29_img_05)](media/slide_29_img_05.jpeg)

**Figure 74:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_05 -->


<!-- INJECT_START: slide_29_img_04 -->
![Zones are where Cloud resources are deployed (slide_29_img_04)](media/slide_29_img_04.jpeg)

**Figure 73:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_04 -->


<!-- INJECT_START: slide_29_img_06 -->
![Zones are where Cloud resources are deployed (slide_29_img_06)](media/slide_29_img_06.jpeg)

**Figure 75:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_06 -->


<!-- INJECT_START: slide_29_img_07 -->
![Zones are where Cloud resources are deployed (slide_29_img_07)](media/slide_29_img_07.jpeg)

**Figure 76:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_07 -->


<!-- INJECT_START: slide_29_img_01 -->
![Zones are where Cloud resources are deployed (slide_29_img_01)](media/slide_29_img_01.jpeg)

**Figure 70:** [Slide 29] Zones are where Cloud resources are deployed — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_01 -->

  * A zone is an area where Google Cloud resources get deployed. For example, let's say
  * you launch a virtual machine using Compute Enginemore about Compute Engine in
  * a bitit will run in the zone that you specify to ensure resource redundancy.

---

<a id="slide-30-resources-can-run-in-different-regions"></a>
### Slide 30: Resources can run in different regions


<!-- INJECT_START: slide_30_img_06 -->
![Resources can run in different regions (slide_30_img_06)](media/slide_30_img_06.jpeg)

**Figure 82:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_06 -->


<!-- INJECT_START: slide_30_img_05 -->
![Resources can run in different regions (slide_30_img_05)](media/slide_30_img_05.jpeg)

**Figure 81:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_05 -->


<!-- INJECT_START: slide_30_img_04 -->
![Resources can run in different regions (slide_30_img_04)](media/slide_30_img_04.jpeg)

**Figure 80:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_04 -->


<!-- INJECT_START: slide_30_img_02 -->
![Resources can run in different regions (slide_30_img_02)](media/slide_30_img_02.jpeg)

**Figure 78:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_02 -->


<!-- INJECT_START: slide_30_img_03 -->
![Resources can run in different regions (slide_30_img_03)](media/slide_30_img_03.jpeg)

**Figure 79:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_03 -->


<!-- INJECT_START: slide_30_img_01 -->
![Resources can run in different regions (slide_30_img_01)](media/slide_30_img_01.jpeg)

**Figure 77:** [Slide 30] Resources can run in different regions — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_01 -->

* You can run resources in different regions. This is useful for bringing applications
* closer to users around the world, and also for protection in case there are issues with
* an entire region, say, due to a natural disaster.

---

<a id="slide-31-some-services-can-run-in-multiple-geographic-locations"></a>
### Slide 31: Some services can run in multiple geographic locations


<!-- INJECT_START: slide_31_img_03 -->
![Some services can run in multiple geographic locations (slide_31_img_03)](media/slide_31_img_03.jpeg)

**Figure 85:** [Slide 31] Some services can run in multiple geographic locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_03 -->


<!-- INJECT_START: slide_31_img_04 -->
![Some services can run in multiple geographic locations (slide_31_img_04)](media/slide_31_img_04.jpeg)

**Figure 86:** [Slide 31] Some services can run in multiple geographic locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_04 -->


<!-- INJECT_START: slide_31_img_02 -->
![Some services can run in multiple geographic locations (slide_31_img_02)](media/slide_31_img_02.jpeg)

**Figure 84:** [Slide 31] Some services can run in multiple geographic locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_02 -->


<!-- INJECT_START: slide_31_img_01 -->
![Some services can run in multiple geographic locations (slide_31_img_01)](media/slide_31_img_01.jpeg)

**Figure 83:** [Slide 31] Some services can run in multiple geographic locations — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_01 -->


---

<a id="slide-32-cloudgooglecomaboutlocations-130-43"></a>
### Slide 32: cloud.google.com/about/locations 130 43

* Proprietary + Confidential
* Zones and regions supported
* cloud.google.com/about/locations
* 130
* 43

<!-- INJECT_START: slide_32_img_03 -->
![cloud.google.com/about/locations 130 43 (slide_32_img_03)](media/slide_32_img_03.jpeg)

**Figure 89:** [Slide 32] cloud.google.com/about/locations 130 43 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_03 -->


<!-- INJECT_START: slide_32_img_02 -->
![cloud.google.com/about/locations 130 43 (slide_32_img_02)](media/slide_32_img_02.jpeg)

**Figure 88:** [Slide 32] cloud.google.com/about/locations 130 43 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_02 -->

* Zones
* Regions

<!-- INJECT_START: slide_32_img_01 -->
![cloud.google.com/about/locations 130 43 (slide_32_img_01)](media/slide_32_img_01.jpeg)

**Figure 87:** [Slide 32] cloud.google.com/about/locations 130 43 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_01 -->

* The number of zones and regions Google Cloud supports is increasing all the time.
* The most up to date info can be found at cloud.google.com/about/locations.

---

<a id="slide-33-introducing-google-cloud"></a>
### Slide 33: Introducing Google Cloud


<!-- INJECT_START: slide_33_img_02 -->
![Introducing Google Cloud (slide_33_img_02)](media/slide_33_img_02.jpeg)

**Figure 91:** [Slide 33] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_33_img_01 -->
![Introducing Google Cloud (slide_33_img_01)](media/slide_33_img_01.jpeg)

**Figure 90:** [Slide 33] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_01 -->


---

<a id="slide-34-2"></a>
### Slide 34: 2%

* Proprietary + Confidential

<!-- INJECT_START: slide_34_img_02 -->
![2% (slide_34_img_02)](media/slide_34_img_02.jpeg)

**Figure 93:** [Slide 34] 2% — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_02 -->


<!-- INJECT_START: slide_34_img_01 -->
![2% (slide_34_img_01)](media/slide_34_img_01.jpeg)

**Figure 92:** [Slide 34] 2% — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_01 -->

* The virtual world, which includes Google Cloud's network, is built on physical
* infrastructure, and all those racks of humming servers use huge amounts of energy.
* Together, all existing data centers use roughly 2% of the world's electricity. So, Google
* works to make data centers run as efficiently as possible.

---

<a id="slide-35-google-aims-to-improve-efficiency-and-reduce-waste"></a>
### Slide 35: Google aims to improve efficiency and reduce waste


<!-- INJECT_START: slide_35_img_02 -->
![Google aims to improve efficiency and reduce waste (slide_35_img_02)](media/slide_35_img_02.jpeg)

**Figure 95:** [Slide 35] Google aims to improve efficiency and reduce waste — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_02 -->


<!-- INJECT_START: slide_35_img_01 -->
![Google aims to improve efficiency and reduce waste (slide_35_img_01)](media/slide_35_img_01.jpeg)

**Figure 94:** [Slide 35] Google aims to improve efficiency and reduce waste — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_01 -->

* Just like our customers, Google is trying to do the right things for the planet. We
* understand that Google Cloud customers have environmental goals of their own, and
* running their workloads in Google Cloud can be a part of meeting them.
* Therefore, it's important to note that Google's data centers were the first to achieve
* ISO 14001 certification, which is a standard that maps out a framework for improving
* resource efficiency and reducing waste.

---

<a id="slide-36-googles-data-center-in-hamina-finland"></a>
### Slide 36: Google's data center in Hamina, Finland

* Proprietary + Confidential

<!-- INJECT_START: slide_36_img_02 -->
![Google's data center in Hamina, Finland (slide_36_img_02)](media/slide_36_img_02.jpeg)

**Figure 97:** [Slide 36] Google's data center in Hamina, Finland — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_02 -->


<!-- INJECT_START: slide_36_img_01 -->
![Google's data center in Hamina, Finland (slide_36_img_01)](media/slide_36_img_01.jpeg)

**Figure 96:** [Slide 36] Google's data center in Hamina, Finland — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_01 -->


---

<a id="slide-37-googles-commitment-to-sustainability"></a>
### Slide 37: Google's commitment to sustainability


<!-- INJECT_START: slide_37_img_02 -->
![Google's commitment to sustainability (slide_37_img_02)](media/slide_37_img_02.jpeg)

**Figure 99:** [Slide 37] Google's commitment to sustainability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_02 -->


<!-- INJECT_START: slide_37_img_01 -->
![Google's commitment to sustainability (slide_37_img_01)](media/slide_37_img_01.jpeg)

**Figure 98:** [Slide 37] Google's commitment to sustainability — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_01 -->

* In our founding decade, Google became the first major company to be carbon neutral.
* In our second decade, we were the first company to achieve 100% renewable energy.
* By 2030, we aim to be the first major company to operate on carbon-free energy, 24
* hours a day, 7 days a week, 365 days a year.

---

<a id="slide-38-introducing-google-cloud"></a>
### Slide 38: Introducing Google Cloud


<!-- INJECT_START: slide_38_img_02 -->
![Introducing Google Cloud (slide_38_img_02)](media/slide_38_img_02.jpeg)

**Figure 101:** [Slide 38] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_38_img_01 -->
![Introducing Google Cloud (slide_38_img_01)](media/slide_38_img_01.jpeg)

**Figure 100:** [Slide 38] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_01 -->


---

<a id="slide-39-google-cloud-is-designed-with-security-in-mind"></a>
### Slide 39: Google Cloud is  designed with  security in mind


<!-- INJECT_START: slide_39_img_02 -->
![Google Cloud is  designed with  security in mind (slide_39_img_02)](media/slide_39_img_02.jpeg)

**Figure 103:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_02 -->


<!-- INJECT_START: slide_39_img_04 -->
![Google Cloud is  designed with  security in mind (slide_39_img_04)](media/slide_39_img_04.jpeg)

**Figure 105:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_04 -->


<!-- INJECT_START: slide_39_img_05 -->
![Google Cloud is  designed with  security in mind (slide_39_img_05)](media/slide_39_img_05.jpeg)

**Figure 106:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_05 -->


<!-- INJECT_START: slide_39_img_06 -->
![Google Cloud is  designed with  security in mind (slide_39_img_06)](media/slide_39_img_06.jpeg)

**Figure 107:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_06 -->


<!-- INJECT_START: slide_39_img_03 -->
![Google Cloud is  designed with  security in mind (slide_39_img_03)](media/slide_39_img_03.jpeg)

**Figure 104:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_03 -->

* Google Cloud is
* designed with
* security in mind

<!-- INJECT_START: slide_39_img_10 -->
![Google Cloud is  designed with  security in mind (slide_39_img_10)](media/slide_39_img_10.jpeg)

**Figure 111:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_10 -->


<!-- INJECT_START: slide_39_img_07 -->
![Google Cloud is  designed with  security in mind (slide_39_img_07)](media/slide_39_img_07.jpeg)

**Figure 108:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_07 -->


<!-- INJECT_START: slide_39_img_09 -->
![Google Cloud is  designed with  security in mind (slide_39_img_09)](media/slide_39_img_09.jpeg)

**Figure 110:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_09 -->


<!-- INJECT_START: slide_39_img_08 -->
![Google Cloud is  designed with  security in mind (slide_39_img_08)](media/slide_39_img_08.jpeg)

**Figure 109:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_08 -->


<!-- INJECT_START: slide_39_img_01 -->
![Google Cloud is  designed with  security in mind (slide_39_img_01)](media/slide_39_img_01.jpeg)

**Figure 102:** [Slide 39] Google Cloud is  designed with  security in mind — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_01 -->

* Because Google has nine* services with more than a billion users, you can bet
* security is always on the minds of Google's employees. Design for security is
* prevalent, throughout the infrastructure, that Google Cloud and Google services
* run-on.
* Let's talk about a few ways Google works to keep customers' data safe.
* *[Android, Chrome, Gmail, Drive, Maps, Photos, Search, Play Store, YouTube]

---

<a id="slide-40-hardware-infrastructure-level"></a>
### Slide 40: Hardware  infrastructure level

* Proprietary + Confidential
* Hardware
* infrastructure level

<!-- INJECT_START: slide_40_img_03 -->
![Hardware  infrastructure level (slide_40_img_03)](media/slide_40_img_03.jpeg)

**Figure 114:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_03 -->


<!-- INJECT_START: slide_40_img_02 -->
![Hardware  infrastructure level (slide_40_img_02)](media/slide_40_img_02.jpeg)

**Figure 113:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_02 -->


<!-- INJECT_START: slide_40_img_04 -->
![Hardware  infrastructure level (slide_40_img_04)](media/slide_40_img_04.jpeg)

**Figure 115:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_04 -->


<!-- INJECT_START: slide_40_img_05 -->
![Hardware  infrastructure level (slide_40_img_05)](media/slide_40_img_05.jpeg)

**Figure 116:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_05 -->


<!-- INJECT_START: slide_40_img_06 -->
![Hardware  infrastructure level (slide_40_img_06)](media/slide_40_img_06.jpeg)

**Figure 117:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_06 -->


<!-- INJECT_START: slide_40_img_07 -->
![Hardware  infrastructure level (slide_40_img_07)](media/slide_40_img_07.jpeg)

**Figure 118:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_07 -->


<!-- INJECT_START: slide_40_img_01 -->
![Hardware  infrastructure level (slide_40_img_01)](media/slide_40_img_01.jpeg)

**Figure 112:** [Slide 40] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_40_img_01 -->

* **At the Hardware infrastructure level:**

---

<a id="slide-41-hardware-infrastructure-level"></a>
### Slide 41: Hardware  infrastructure level

* Proprietary + Confidential
* Hardware design and provenance
* Server boards, chips, and the networking
* equipment in Google data centers custom
* designed by Google.

<!-- INJECT_START: slide_41_img_02 -->
![Hardware  infrastructure level (slide_41_img_02)](media/slide_41_img_02.jpeg)

**Figure 120:** [Slide 41] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_41_img_02 -->

* Secure boot stack
* Hardware
* infrastructure level
* Google's server machines ensure that they are
* booting the correct software stack.
* Premises security
* Google data centers  incorporate multiple layers
* of physical security protections.

<!-- INJECT_START: slide_41_img_01 -->
![Hardware  infrastructure level (slide_41_img_01)](media/slide_41_img_01.jpeg)

**Figure 119:** [Slide 41] Hardware  infrastructure level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_41_img_01 -->

* **Hardware design and provenance:** Both the server boards and the networking
* equipment in Google data centers are custom designed by Google. Google also
* designs custom chips, including a hardware security chip that's currently being
* deployed on both servers and peripherals.
* **Secure boot stack:** Google server machines use a variety of technologies to ensure
* that they are booting the correct software stack, such as cryptographic signatures
* over the BIOS, bootloader, kernel, and base operating system image.
* **Premises security:** Google designs and builds its own data centers, which incorporate
* multiple layers of physical security protections. Access to these data centers is
* limited to only a very small fraction of Google employees. Google additionally hosts
* some servers in third-party data centers, where we ensure that there are
* Google-controlled physical security measures on top of the security layers provided
* by the data center operator.

---

<a id="slide-42-service-deployment-level"></a>
### Slide 42: Service  Deployment level

* Proprietary + Confidential
* Service
* Deployment level

<!-- INJECT_START: slide_42_img_03 -->
![Service  Deployment level (slide_42_img_03)](media/slide_42_img_03.jpeg)

**Figure 123:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_03 -->


<!-- INJECT_START: slide_42_img_02 -->
![Service  Deployment level (slide_42_img_02)](media/slide_42_img_02.jpeg)

**Figure 122:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_02 -->


<!-- INJECT_START: slide_42_img_04 -->
![Service  Deployment level (slide_42_img_04)](media/slide_42_img_04.jpeg)

**Figure 124:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_04 -->


<!-- INJECT_START: slide_42_img_05 -->
![Service  Deployment level (slide_42_img_05)](media/slide_42_img_05.jpeg)

**Figure 125:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_05 -->


<!-- INJECT_START: slide_42_img_06 -->
![Service  Deployment level (slide_42_img_06)](media/slide_42_img_06.jpeg)

**Figure 126:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_06 -->


<!-- INJECT_START: slide_42_img_07 -->
![Service  Deployment level (slide_42_img_07)](media/slide_42_img_07.jpeg)

**Figure 127:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_07 -->


<!-- INJECT_START: slide_42_img_01 -->
![Service  Deployment level (slide_42_img_01)](media/slide_42_img_01.jpeg)

**Figure 121:** [Slide 42] Service  Deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_01 -->

* **At the Service deployment level:**

---

<a id="slide-43-service-deployment-level"></a>
### Slide 43: Service  deployment level

* Proprietary + Confidential

<!-- INJECT_START: slide_43_img_02 -->
![Service  deployment level (slide_43_img_02)](media/slide_43_img_02.jpeg)

**Figure 129:** [Slide 43] Service  deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_43_img_02 -->

* Encryption of inter-service communication
* Services communicate with each other using
* remote procedure calls ("RPCs").
* Service
* deployment level
* Google's infrastructure encrypts all
* infrastructure RPC traffic between data
* centers.

<!-- INJECT_START: slide_43_img_01 -->
![Service  deployment level (slide_43_img_01)](media/slide_43_img_01.jpeg)

**Figure 128:** [Slide 43] Service  deployment level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_43_img_01 -->

* **Encryption of inter-service communication:** Google's infrastructure provides
* cryptographic privacy and integrity for remote procedure call ("RPC") data on the
* network. Google's services communicate with each other using RPC calls. The
* infrastructure automatically encrypts all infrastructure RPC traffic which goes
* between data centers. Google has started to deploy hardware cryptographic
* accelerators that will allow it to extend this default encryption to all infrastructure RPC
* traffic inside Google data centers.

---

<a id="slide-44-user-identity-level"></a>
### Slide 44: User identity level

* Proprietary + Confidential

<!-- INJECT_START: slide_44_img_03 -->
![User identity level (slide_44_img_03)](media/slide_44_img_03.jpeg)

**Figure 132:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_03 -->


<!-- INJECT_START: slide_44_img_02 -->
![User identity level (slide_44_img_02)](media/slide_44_img_02.jpeg)

**Figure 131:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_02 -->


<!-- INJECT_START: slide_44_img_04 -->
![User identity level (slide_44_img_04)](media/slide_44_img_04.jpeg)

**Figure 133:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_04 -->


<!-- INJECT_START: slide_44_img_05 -->
![User identity level (slide_44_img_05)](media/slide_44_img_05.jpeg)

**Figure 134:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_05 -->


<!-- INJECT_START: slide_44_img_06 -->
![User identity level (slide_44_img_06)](media/slide_44_img_06.jpeg)

**Figure 135:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_06 -->


<!-- INJECT_START: slide_44_img_07 -->
![User identity level (slide_44_img_07)](media/slide_44_img_07.jpeg)

**Figure 136:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_07 -->


<!-- INJECT_START: slide_44_img_01 -->
![User identity level (slide_44_img_01)](media/slide_44_img_01.jpeg)

**Figure 130:** [Slide 44] User identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_01 -->

* **At the User identity level:**

---

<a id="slide-45-user-identity-level"></a>
### Slide 45: User  identity level

* Proprietary + Confidential

<!-- INJECT_START: slide_45_img_02 -->
![User  identity level (slide_45_img_02)](media/slide_45_img_02.jpeg)

**Figure 138:** [Slide 45] User  identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_45_img_02 -->

* User identity
* Intelligently challenges users for additional
* information based on certain risk factors.
* User
* identity level
* Users can use secondary factors when signing in,
* including Factor (U2F) open standard.

<!-- INJECT_START: slide_45_img_01 -->
![User  identity level (slide_45_img_01)](media/slide_45_img_01.jpeg)

**Figure 137:** [Slide 45] User  identity level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_45_img_01 -->

* **User identity:** Google's central identity service, which usually manifests to end users
* as the Google login page, goes beyond asking for a simple username and password.
* The service also intelligently challenges users for additional information based on risk
* factors such as whether they have logged in from the same device or a similar
* location in the past. Users also have the option of employing secondary factors when
* signing in, including devices based on the Universal 2nd Factor (U2F) open standard.

---

<a id="slide-46-storage-services-level"></a>
### Slide 46: Storage  services level

* Proprietary + Confidential
* Storage
* services level

<!-- INJECT_START: slide_46_img_03 -->
![Storage  services level (slide_46_img_03)](media/slide_46_img_03.jpeg)

**Figure 141:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_03 -->


<!-- INJECT_START: slide_46_img_02 -->
![Storage  services level (slide_46_img_02)](media/slide_46_img_02.jpeg)

**Figure 140:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_02 -->


<!-- INJECT_START: slide_46_img_04 -->
![Storage  services level (slide_46_img_04)](media/slide_46_img_04.jpeg)

**Figure 142:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_04 -->


<!-- INJECT_START: slide_46_img_05 -->
![Storage  services level (slide_46_img_05)](media/slide_46_img_05.jpeg)

**Figure 143:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_05 -->


<!-- INJECT_START: slide_46_img_06 -->
![Storage  services level (slide_46_img_06)](media/slide_46_img_06.jpeg)

**Figure 144:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_06 -->


<!-- INJECT_START: slide_46_img_07 -->
![Storage  services level (slide_46_img_07)](media/slide_46_img_07.jpeg)

**Figure 145:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_07 -->


<!-- INJECT_START: slide_46_img_01 -->
![Storage  services level (slide_46_img_01)](media/slide_46_img_01.jpeg)

**Figure 139:** [Slide 46] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_01 -->

* **At the Storage services level:**

---

<a id="slide-47-storage-services-level"></a>
### Slide 47: Storage  services level

* Proprietary + Confidential

<!-- INJECT_START: slide_47_img_02 -->
![Storage  services level (slide_47_img_02)](media/slide_47_img_02.jpeg)

**Figure 147:** [Slide 47] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_02 -->

* Encryption at rest
* Most Google applications access file storage
* indirectly via storage services and encryption.
* Storage
* services level
* Using centrally managed keys, encryption is
* applied at the layer of these storage services.
* Google also enables hardware encryption support
* in hard drives and SSDs.

<!-- INJECT_START: slide_47_img_01 -->
![Storage  services level (slide_47_img_01)](media/slide_47_img_01.jpeg)

**Figure 146:** [Slide 47] Storage  services level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_01 -->

* **Encryption at rest:** Most applications at Google access physical storage (in other
* words, "file storage") indirectly via storage services, and encryption (using centrally
* managed keys) is applied at the  layer of these storage services. Google also enables
* hardware encryption support in hard drives and SSDs.

---

<a id="slide-48-internet-communication-level"></a>
### Slide 48: Internet  communication level

* Proprietary + Confidential
* Internet
* communication level

<!-- INJECT_START: slide_48_img_03 -->
![Internet  communication level (slide_48_img_03)](media/slide_48_img_03.jpeg)

**Figure 150:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_03 -->


<!-- INJECT_START: slide_48_img_02 -->
![Internet  communication level (slide_48_img_02)](media/slide_48_img_02.jpeg)

**Figure 149:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_02 -->


<!-- INJECT_START: slide_48_img_04 -->
![Internet  communication level (slide_48_img_04)](media/slide_48_img_04.jpeg)

**Figure 151:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_04 -->


<!-- INJECT_START: slide_48_img_05 -->
![Internet  communication level (slide_48_img_05)](media/slide_48_img_05.jpeg)

**Figure 152:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_05 -->


<!-- INJECT_START: slide_48_img_06 -->
![Internet  communication level (slide_48_img_06)](media/slide_48_img_06.jpeg)

**Figure 153:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_06 -->


<!-- INJECT_START: slide_48_img_07 -->
![Internet  communication level (slide_48_img_07)](media/slide_48_img_07.jpeg)

**Figure 154:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_07 -->


<!-- INJECT_START: slide_48_img_01 -->
![Internet  communication level (slide_48_img_01)](media/slide_48_img_01.jpeg)

**Figure 148:** [Slide 48] Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_01 -->

* **At the Internet communication level:**

---

<a id="slide-49-denial-of-service-dos-protection-internet-communication-level"></a>
### Slide 49: Denial of Service ("DoS") protection Internet  communication level

* Proprietary + Confidential
* Google Front End ("GFE")

<!-- INJECT_START: slide_49_img_02 -->
![Denial of Service ("DoS") protection Internet  communication level (slide_49_img_02)](media/slide_49_img_02.jpeg)

**Figure 156:** [Slide 49] Denial of Service ("DoS") protection Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_49_img_02 -->

* Google Front End ensures that all registered
* services use TLS connections incorporating the
* correct certificates and following best practices.
* Denial of Service ("DoS") protection
* Internet
* communication level
* Google has multi-tier, multi-layer DoS protections
* that reduce the risk of any DoS impact on
* a service running behind a GFE.

<!-- INJECT_START: slide_49_img_01 -->
![Denial of Service ("DoS") protection Internet  communication level (slide_49_img_01)](media/slide_49_img_01.jpeg)

**Figure 155:** [Slide 49] Denial of Service ("DoS") protection Internet  communication level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_49_img_01 -->

* **Google Front End ("GFE"):** Google services that want to make themselves available on
* the Internet register themselves with an infrastructure service called the Google Front
* End, which ensures that all TLS connections are ended using a public-private key pair
* and an X.509 certificate from a Certified Authority (CA) as well as following best
* practices such as supporting perfect forward secrecy. The GFE additionally applies
* protections against Denial of Service attacks.
* **Denial of Service ("DoS") protection:** The sheer scale of its infrastructure enables
* Google to simply absorb many DoS attacks. Google also has multi-tier, multi-layer DoS
* protections that further reduce the risk of any DoS impact on a service running behind
* a GFE.

---

<a id="slide-50-operational-security-level"></a>
### Slide 50: Operational  security level

* Proprietary + Confidential
* Operational
* security level

<!-- INJECT_START: slide_50_img_03 -->
![Operational  security level (slide_50_img_03)](media/slide_50_img_03.jpeg)

**Figure 159:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_03 -->


<!-- INJECT_START: slide_50_img_02 -->
![Operational  security level (slide_50_img_02)](media/slide_50_img_02.jpeg)

**Figure 158:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_02 -->


<!-- INJECT_START: slide_50_img_04 -->
![Operational  security level (slide_50_img_04)](media/slide_50_img_04.jpeg)

**Figure 160:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_04 -->


<!-- INJECT_START: slide_50_img_05 -->
![Operational  security level (slide_50_img_05)](media/slide_50_img_05.jpeg)

**Figure 161:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_05 -->


<!-- INJECT_START: slide_50_img_06 -->
![Operational  security level (slide_50_img_06)](media/slide_50_img_06.jpeg)

**Figure 162:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_06 -->


<!-- INJECT_START: slide_50_img_07 -->
![Operational  security level (slide_50_img_07)](media/slide_50_img_07.jpeg)

**Figure 163:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_07 -->


<!-- INJECT_START: slide_50_img_01 -->
![Operational  security level (slide_50_img_01)](media/slide_50_img_01.jpeg)

**Figure 157:** [Slide 50] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_01 -->

* **Finally, at Google's Operational security level:**

---

<a id="slide-51-operational-security-level"></a>
### Slide 51: Operational  security level

* Proprietary + Confidential
* Intrusion detection
* Rules and machine intelligence give operational
* security engineers warnings of possible incidents.

<!-- INJECT_START: slide_51_img_02 -->
![Operational  security level (slide_51_img_02)](media/slide_51_img_02.jpeg)

**Figure 165:** [Slide 51] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_51_img_02 -->

* Reducing insider risk
* Google limits and monitors the activities of
* employees who have access to the infrastructure.
* Operational
* security level
* Employee Universal Second Factor (U2F) use
* All Google employee accounts require use of
* U2F-compatible Security Keys.
* Software development practices
* Google employs central source control and requires
* two-party review of any new code.

<!-- INJECT_START: slide_51_img_01 -->
![Operational  security level (slide_51_img_01)](media/slide_51_img_01.jpeg)

**Figure 164:** [Slide 51] Operational  security level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_51_img_01 -->

* **Intrusion detection:** Rules and machine intelligence give Google's operational security
* teams warnings of possible incidents. Google conducts Red Team exercises to
* measure and improve the effectiveness of its detection and response mechanisms.
* **Reducing insider risk:** Google aggressively limits and actively monitors the activities
* of employees who have been granted administrative access to the infrastructure.
* **Employee U2F use:** To guard against phishing attacks against Google employees,
* employee accounts require use of U2F-compatible Security Keys.
* **Software development practices:** Google employs central source control and requires
* two-party review of new code. Google also provides its developers libraries that
* prevent them from introducing certain classes of security bugs. Google also runs a
* Vulnerability Rewards Program where we pay anyone who is able to discover and
* inform us of bugs in our infrastructure or applications.

---

<a id="slide-52-cloudgooglecomsecuritysecurity-design"></a>
### Slide 52: cloud.google.com/security/security-design

* Proprietary + Confidential

<!-- INJECT_START: slide_52_img_01 -->
![cloud.google.com/security/security-design (slide_52_img_01)](media/slide_52_img_01.jpeg)

**Figure 166:** [Slide 52] cloud.google.com/security/security-design — Visual Illustration & Context Reference
<!-- INJECT_END: slide_52_img_01 -->

* You can learn more about Google's technical-infrastructure security at
* cloud.google.com/security/security-design.

---

<a id="slide-53-introducing-google-cloud"></a>
### Slide 53: Introducing Google Cloud


<!-- INJECT_START: slide_53_img_02 -->
![Introducing Google Cloud (slide_53_img_02)](media/slide_53_img_02.jpeg)

**Figure 168:** [Slide 53] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_53_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_53_img_01 -->
![Introducing Google Cloud (slide_53_img_01)](media/slide_53_img_01.jpeg)

**Figure 167:** [Slide 53] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_53_img_01 -->


---

<a id="slide-54-google-cloud-is-open-source-friendly"></a>
### Slide 54: Google Cloud is open-source friendly

* Proprietary + Confidential

<!-- INJECT_START: slide_54_img_02 -->
![Google Cloud is open-source friendly (slide_54_img_02)](media/slide_54_img_02.jpeg)

**Figure 170:** [Slide 54] Google Cloud is open-source friendly — Visual Illustration & Context Reference
<!-- INJECT_END: slide_54_img_02 -->


<!-- INJECT_START: slide_54_img_01 -->
![Google Cloud is open-source friendly (slide_54_img_01)](media/slide_54_img_01.jpeg)

**Figure 169:** [Slide 54] Google Cloud is open-source friendly — Visual Illustration & Context Reference
<!-- INJECT_END: slide_54_img_01 -->

* Some people are afraid to bring their workloads to the cloud because they're afraid
* they'll get locked into a particular vendor.
* But if, for whatever reason, a customer decides that Google is no longer the best
* provider for their needs, we give customers the ability to run their applications
* elsewhere.
* Google publishes key elements of technology using open source licenses to create
* ecosystems that provide customers with options other than Google.

---

<a id="slide-55-open-source-tensorflow-works-with-google-cloud"></a>
### Slide 55: Open-source TensorFlow works with Google Cloud

* Proprietary + Confidential

<!-- INJECT_START: slide_55_img_02 -->
![Open-source TensorFlow works with Google Cloud (slide_55_img_02)](media/slide_55_img_02.jpeg)

**Figure 172:** [Slide 55] Open-source TensorFlow works with Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_55_img_02 -->

* TensorFlow is an open source
* library for machine learning
* TensorFlow is at the heart of
* a strong open source ecosystem

<!-- INJECT_START: slide_55_img_01 -->
![Open-source TensorFlow works with Google Cloud (slide_55_img_01)](media/slide_55_img_01.jpeg)

**Figure 171:** [Slide 55] Open-source TensorFlow works with Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_55_img_01 -->

* For example, TensorFlow, an open source software library for machine learning
* developed inside Google, is at the heart of a strong open source ecosystem.

---

<a id="slide-56-interoperability-at-multiple-layers-of-the-stack"></a>
### Slide 56: Interoperability at multiple layers of the stack

* Proprietary + Confidential
* Kubernetes
* GKE
* Google Cloud Observability

<!-- INJECT_START: slide_56_img_04 -->
![Interoperability at multiple layers of the stack (slide_56_img_04)](media/slide_56_img_04.jpeg)

**Figure 176:** [Slide 56] Interoperability at multiple layers of the stack — Visual Illustration & Context Reference
<!-- INJECT_END: slide_56_img_04 -->


<!-- INJECT_START: slide_56_img_02 -->
![Interoperability at multiple layers of the stack (slide_56_img_02)](media/slide_56_img_02.jpeg)

**Figure 174:** [Slide 56] Interoperability at multiple layers of the stack — Visual Illustration & Context Reference
<!-- INJECT_END: slide_56_img_02 -->


<!-- INJECT_START: slide_56_img_03 -->
![Interoperability at multiple layers of the stack (slide_56_img_03)](media/slide_56_img_03.jpeg)

**Figure 175:** [Slide 56] Interoperability at multiple layers of the stack — Visual Illustration & Context Reference
<!-- INJECT_END: slide_56_img_03 -->

* Mix and match microservices
* running across different clouds
* Monitor workloads across
* multiple cloud providers

<!-- INJECT_START: slide_56_img_01 -->
![Interoperability at multiple layers of the stack (slide_56_img_01)](media/slide_56_img_01.jpeg)

**Figure 173:** [Slide 56] Interoperability at multiple layers of the stack — Visual Illustration & Context Reference
<!-- INJECT_END: slide_56_img_01 -->

* Google provides interoperability at multiple layers of the stack. Kubernetes and
* Google Kubernetes Engine give customers the ability to mix and match microservices
* running across different clouds. Google Cloud Observability lets customers monitor
* workloads across multiple cloud providers.

---

<a id="slide-57-introducing-google-cloud"></a>
### Slide 57: Introducing Google Cloud


<!-- INJECT_START: slide_57_img_02 -->
![Introducing Google Cloud (slide_57_img_02)](media/slide_57_img_02.jpeg)

**Figure 178:** [Slide 57] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_57_img_02 -->

* 01
* 02
* An overview of cloud computing
* IaaS and PaaS
* 03
* 04
* The Google Cloud network
* Environmental impact
* 05
* 06
* 07
* Security
* Open APIs and open source
* Pricing and billing

<!-- INJECT_START: slide_57_img_01 -->
![Introducing Google Cloud (slide_57_img_01)](media/slide_57_img_01.jpeg)

**Figure 177:** [Slide 57] Introducing Google Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_57_img_01 -->

* Now a word on Google Cloud's pricing structure.

---

<a id="slide-58-google-compute-products-are-billed-per-second"></a>
### Slide 58: Google Compute products are billed per-second


<!-- INJECT_START: slide_58_img_02 -->
![Google Compute products are billed per-second (slide_58_img_02)](media/slide_58_img_02.jpeg)

**Figure 180:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_02 -->


<!-- INJECT_START: slide_58_img_03 -->
![Google Compute products are billed per-second (slide_58_img_03)](media/slide_58_img_03.jpeg)

**Figure 181:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_03 -->


<!-- INJECT_START: slide_58_img_04 -->
![Google Compute products are billed per-second (slide_58_img_04)](media/slide_58_img_04.jpeg)

**Figure 182:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_04 -->


<!-- INJECT_START: slide_58_img_05 -->
![Google Compute products are billed per-second (slide_58_img_05)](media/slide_58_img_05.jpeg)

**Figure 183:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_05 -->


<!-- INJECT_START: slide_58_img_06 -->
![Google Compute products are billed per-second (slide_58_img_06)](media/slide_58_img_06.jpeg)

**Figure 184:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_06 -->


<!-- INJECT_START: slide_58_img_01 -->
![Google Compute products are billed per-second (slide_58_img_01)](media/slide_58_img_01.jpeg)

**Figure 179:** [Slide 58] Google Compute products are billed per-second — Visual Illustration & Context Reference
<!-- INJECT_END: slide_58_img_01 -->

* Google was the first major cloud provider to deliver per-second billing for its
* Infrastructure-as-a-Service compute offering, Compute Engine.
* We'll explore these products and services later in this course, but per-second billing is
* offered for users of Compute Engine, Google Kubernetes Engine (container
* infrastructure as a service), Managed Service for Apache Spark (which is the
* equivalent of the big data system Hadoop, but operating as a service), and App
* Engine flexible environment VMs (a platform as a service).

---

<a id="slide-59-compute-engine-offers-billing-flexibility"></a>
### Slide 59: Compute Engine offers billing flexibility


<!-- INJECT_START: slide_59_img_02 -->
![Compute Engine offers billing flexibility (slide_59_img_02)](media/slide_59_img_02.jpeg)

**Figure 186:** [Slide 59] Compute Engine offers billing flexibility — Visual Illustration & Context Reference
<!-- INJECT_END: slide_59_img_02 -->


<!-- INJECT_START: slide_59_img_03 -->
![Compute Engine offers billing flexibility (slide_59_img_03)](media/slide_59_img_03.jpeg)

**Figure 187:** [Slide 59] Compute Engine offers billing flexibility — Visual Illustration & Context Reference
<!-- INJECT_END: slide_59_img_03 -->


<!-- INJECT_START: slide_59_img_01 -->
![Compute Engine offers billing flexibility (slide_59_img_01)](media/slide_59_img_01.jpeg)

**Figure 185:** [Slide 59] Compute Engine offers billing flexibility — Visual Illustration & Context Reference
<!-- INJECT_END: slide_59_img_01 -->

* Compute Engine offers automatically applied sustained-use discounts, which are
* automatic discounts that you get for running a virtual-machine instance for a
* significant portion of the billing month. Specifically, when you run an instance for
* more than 25% of a month, Compute Engine automatically gives you a discount for
* every incremental minute you use for that instance.
* Custom virtual machine types allow Compute Engine virtual machines to be
* fine-tuned with optimal amounts of vCPU and memory for their applications, so that
* you can tailor your pricing for your workloads.

---

<a id="slide-60-google-cloud-pricing-calculator"></a>
### Slide 60: Google Cloud Pricing Calculator


<!-- INJECT_START: slide_60_img_02 -->
![Google Cloud Pricing Calculator (slide_60_img_02)](media/slide_60_img_02.jpeg)

**Figure 189:** [Slide 60] Google Cloud Pricing Calculator — Visual Illustration & Context Reference
<!-- INJECT_END: slide_60_img_02 -->


<!-- INJECT_START: slide_60_img_01 -->
![Google Cloud Pricing Calculator (slide_60_img_01)](media/slide_60_img_01.jpeg)

**Figure 188:** [Slide 60] Google Cloud Pricing Calculator — Visual Illustration & Context Reference
<!-- INJECT_END: slide_60_img_01 -->

* Our online pricing calculator can help estimate your costs.
* Visit cloud.google.com/products/calculator to try it out.

---

<a id="slide-61-billing-tools-help-to-budget-and-monitor-usage"></a>
### Slide 61: Billing tools help to budget and monitor usage


<!-- INJECT_START: slide_61_img_02 -->
![Billing tools help to budget and monitor usage (slide_61_img_02)](media/slide_61_img_02.jpeg)

**Figure 191:** [Slide 61] Billing tools help to budget and monitor usage — Visual Illustration & Context Reference
<!-- INJECT_END: slide_61_img_02 -->


<!-- INJECT_START: slide_61_img_01 -->
![Billing tools help to budget and monitor usage (slide_61_img_01)](media/slide_61_img_01.jpeg)

**Figure 190:** [Slide 61] Billing tools help to budget and monitor usage — Visual Illustration & Context Reference
<!-- INJECT_END: slide_61_img_01 -->

* You're probably thinking, "How can I make sure I don't accidentally run up a big
* Google Cloud bill?"
* We provide a few tools to help.
* 1.
* You can define budgets at the billing account level or at the project level. A
* budget can be a fixed limit, or it can be tied to another metric - for example, a
* percentage of the previous month's spend.
* 2.
* To be notified when costs approach your budget limit, you can create an alert.
* For example, with a budget limit of $20,000 and an alert set at 90%, you'll
* receive a notification alert when your expenses reach $18,000. Alerts are
* generally set at 50%, 90% and 100%, but can also be customized.
* 3.
* Reports is a visual tool in the Google Cloud console that allows you to monitor
* expenditure based on a project or services.
* 4.
* Finally, Google Cloud also implements quotas, which are designed to prevent
* the over-consumption of resources because of an error or a malicious attack,
* protecting both account owners and the Google Cloud community as a whole.
* It's worth noting that quotas are actually part of Google's Identity and Access
* Management (IAM) tools, but they do help with cost control.

---

<a id="slide-62-quotas-are-allocated-at-project-level"></a>
### Slide 62: Quotas are allocated at project-level


<!-- INJECT_START: slide_62_img_02 -->
![Quotas are allocated at project-level (slide_62_img_02)](media/slide_62_img_02.jpeg)

**Figure 193:** [Slide 62] Quotas are allocated at project-level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_62_img_02 -->


<!-- INJECT_START: slide_62_img_01 -->
![Quotas are allocated at project-level (slide_62_img_01)](media/slide_62_img_01.jpeg)

**Figure 192:** [Slide 62] Quotas are allocated at project-level — Visual Illustration & Context Reference
<!-- INJECT_END: slide_62_img_01 -->

* **There are two types of quotas:** rate quotas and allocation quotas. Both are applied at
* the project level.
* 1.
* Rate quotas reset after a specific time. For example, by default, the GKE
* service implements a quota of 3,000 calls to its API from each Google Cloud
* project every 100 seconds. After that 100 seconds, the limit is reset.
* 2.
* Allocation quotas govern the number of resources you can have in your
* projects. For example, by default, each Google Cloud project has a quota
* allowing it no more than 15 Virtual Private Cloud networks.
* Although projects all start with the same quotas, you can change some of them by
* requesting an increase from Google Cloud Support.

---

<a id="slide-63-module-quiz"></a>
### Slide 63: Module Quiz


<!-- INJECT_START: slide_63_img_02 -->
![Module Quiz (slide_63_img_02)](media/slide_63_img_02.jpeg)

**Figure 195:** [Slide 63] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_63_img_02 -->


<!-- INJECT_START: slide_63_img_01 -->
![Module Quiz (slide_63_img_01)](media/slide_63_img_01.jpeg)

**Figure 194:** [Slide 63] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_63_img_01 -->


---

<a id="slide-64-quiz-question-1"></a>
### Slide 64: Quiz | Question 1

* Proprietary + Confidential
* Question
* What is the primary benefit to a Google Cloud customer of using resources in several
* zones within a region?
* A.
* For improved fault tolerance
* B.
* For better performance
* C.
* For expanding services to customers in new areas
* D.
* For getting discounts on other zones

<!-- INJECT_START: slide_64_img_01 -->
![Quiz | Question 1 (slide_64_img_01)](media/slide_64_img_01.jpeg)

**Figure 196:** [Slide 64] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_64_img_01 -->


---

<a id="slide-65-quiz-question-1"></a>
### Slide 65: Quiz | Question 1

* Proprietary + Confidential
* Answer
* What is the primary benefit to a Google Cloud customer of using resources in several
* zones within a region?

<!-- INJECT_START: slide_65_img_02 -->
![Quiz | Question 1 (slide_65_img_02)](media/slide_65_img_02.jpeg)

**Figure 198:** [Slide 65] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_65_img_02 -->

* A.
* For improved fault tolerance
* B.
* For better performance
* C.
* For expanding services to customers in new areas
* D.
* For getting discounts on other zones

<!-- INJECT_START: slide_65_img_01 -->
![Quiz | Question 1 (slide_65_img_01)](media/slide_65_img_01.jpeg)

**Figure 197:** [Slide 65] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_65_img_01 -->

* Why might a Google Cloud customer use resources in several zones within a region?
* ***A:** For improved fault tolerance
* **Feedback:** Correct. As part of building a fault-tolerant application, you can spread your
* resources across multiple zones in a region.
* **B:** For better performance
* **Feedback:** That is not correct. The primary benefit of spreading your resources across
* multiple zones in a region is protection against failure.
* **C:** For expanding services to customers in new areas
* **Feedback:** That is not correct. The primary benefit of spreading your resources across
* multiple zones in a region is protection against failure.
* **D:** For getting discounts on other zones
* **Feedback:** That is not correct. The primary benefit of spreading your resources across
* multiple zones in a region is protection against failure.

---

<a id="slide-66-quiz-question-2"></a>
### Slide 66: Quiz | Question 2

* Proprietary + Confidential
* Question
* What type of cloud computing service lets you bind your application code to libraries that
* give access to the infrastructure your application needs?
* A.
* Hybrid Cloud
* B.
* Infrastructure as a Service
* C.
* Software as a Service
* D.
* Platform as a Service
* E.
* Virtualized data centers

<!-- INJECT_START: slide_66_img_01 -->
![Quiz | Question 2 (slide_66_img_01)](media/slide_66_img_01.jpeg)

**Figure 199:** [Slide 66] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_66_img_01 -->


---

<a id="slide-67-quiz-question-2"></a>
### Slide 67: Quiz | Question 2

* Proprietary + Confidential
* Answer
* What type of cloud computing service lets you bind your application code to libraries that
* give access to the infrastructure your application needs?
* A.
* Hybrid Cloud
* B.
* Infrastructure as a Service
* C.
* Software as a Service

<!-- INJECT_START: slide_67_img_02 -->
![Quiz | Question 2 (slide_67_img_02)](media/slide_67_img_02.jpeg)

**Figure 201:** [Slide 67] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_67_img_02 -->

* D.
* Platform as a Service
* E.
* Virtualized data centers

<!-- INJECT_START: slide_67_img_01 -->
![Quiz | Question 2 (slide_67_img_01)](media/slide_67_img_01.jpeg)

**Figure 200:** [Slide 67] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_67_img_01 -->

* What type of cloud computing service lets you bind your application code to libraries
* that give access to the infrastructure your application needs?
* **A:** Hybrid cloud
* **Feedback:** Incorrect. This refers to a cloud deployment model (combining private and
* public clouds) rather than a service category. It describes where the cloud is, not how
* you interact with the code.
* **B:** Infrastructure as a Service
* **Feedback:** Incorrect. IaaS provides raw resources like VMs and storage. In IaaS, you
* are responsible for managing the OS and middleware yourself, rather than binding
* code to provided libraries.
* **C:** Software as a Service
* **Feedback:** Incorrect. SaaS provides a finished product managed by the vendor. You
* generally consume the application via a web browser rather than writing or binding
* your own application code to it.
* **D:** Platform as a Service
* **Feedback:** Correct! PaaS is designed for developers. It provides the SDKs, libraries,
* and runtime environments needed to build and deploy applications without managing
* the underlying hardware or OS.
* **E:** Virtualized data centers

---

<a id="slide-68-feedback-incorrect-while-virtualization-is-a-technology-that-powers-cloud-computing-it-is-not-a-cloud-service-model-this-describes-a-physical-infrastructure-setup-often-on-premises"></a>
### Slide 68: Feedback: Incorrect. While virtualization is a technology that powers cloud  computing, it is not a cloud service model. This describes a physical infrastructure  setup, often on-premises.

* **Feedback:** Incorrect. While virtualization is a technology that powers cloud
* computing, it is not a cloud service model. This describes a physical infrastructure
* setup, often on-premises.

---

<a id="slide-69-quiz-question-3"></a>
### Slide 69: Quiz | Question 3

* Proprietary + Confidential
* Question
* Why might a Google Cloud customer use resources in several regions around the world?
* A.
* To improve security
* B.
* To earn discounts
* C.
* To offer localized application versions in different regions
* D.
* To bring their applications closer to users around the world, and for improved fault
* tolerance

<!-- INJECT_START: slide_69_img_01 -->
![Quiz | Question 3 (slide_69_img_01)](media/slide_69_img_01.jpeg)

**Figure 202:** [Slide 69] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_69_img_01 -->


---

<a id="slide-70-quiz-question-3"></a>
### Slide 70: Quiz | Question 3

* Proprietary + Confidential
* Answer
* Why might a Google Cloud customer use resources in several regions around the world?
* A.
* To improve security
* B.
* To earn discounts
* C.
* To offer localized application versions in different regions
* D.
* To bring their applications closer to users around the world, and for improved fault
* tolerance

<!-- INJECT_START: slide_70_img_02 -->
![Quiz | Question 3 (slide_70_img_02)](media/slide_70_img_02.jpeg)

**Figure 204:** [Slide 70] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_70_img_02 -->


<!-- INJECT_START: slide_70_img_01 -->
![Quiz | Question 3 (slide_70_img_01)](media/slide_70_img_01.jpeg)

**Figure 203:** [Slide 70] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_70_img_01 -->

* Why might a Google Cloud customer use resources in several regions around the
* world?
* **A:** To improve security
* **Feedback:** Running an application in several regions does not necessarily improve
* security. Instead, using resources in multiple regions may give better performance for
* global users, and it also can protect against failures of entire regions.
* **B:** To earn discounts
* **Feedback:** Running an application in several regions does not necessarily earn
* discounts. Instead, using resources in multiple regions may give better performance
* for global users, and it also can protect against failures of entire regions.
* **C:** To offer localized application versions in different regions.
* **Feedback:** Google Cloud allows you to develop different localized versions of your
* application even if your application is based in a single region.  Running an application
* in several regions has no impact on the localized versions of your application.
* ***D:** To bring their applications closer to users around the world, and for improved
* fault tolerance
* **Feedback:** That is correct.

---
