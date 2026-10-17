# 03

### Comprehensive Technical Presentation & Study Guide

> **Course / Domain:** Networks in the Cloud · **Academic Term:** Academic Lecture Series
> **Lecturer / Author:** Course Instructor · **Source:** Official Lecture Presentation Slides
> **Documentation Standard:** DTCM-v3 High-Fidelity Architecture (`ptcm-pdf-v1`)

---

## Table of Contents

* [Slide 1: Virtual Machines and  Networks in the Cloud 03](#slide-1-virtual-machines-and-networks-in-the-cloud-03)
* [Slide 2: Virtual Machines and Networks in the Cloud](#slide-2-virtual-machines-and-networks-in-the-cloud)
* [Slide 3: Virtual Private Cloud (VPC) is your cloud within the Cloud](#slide-3-virtual-private-cloud-vpc-is-your-cloud-within-the-cloud)
* [Slide 4: Virtual Private](#slide-4-virtual-private)
* [Slide 5: VPC subnets connect resources in different zones](#slide-5-vpc-subnets-connect-resources-in-different-zones)
* [Slide 6: Virtual Machines and Networks in the Cloud](#slide-6-virtual-machines-and-networks-in-the-cloud)
* [Slide 7: Compute Engine](#slide-7-compute-engine)
* [Slide 8: Virtual machine instances are flexible resources](#slide-8-virtual-machine-instances-are-flexible-resources)
* [Slide 9: Cloud Marketplace](#slide-9-cloud-marketplace)
* [Slide 10: Compute Engine pricing and billing offers discounts](#slide-10-compute-engine-pricing-and-billing-offers-discounts)
* [Slide 11: Compute Engine pricing is "pay for only what you need"](#slide-11-compute-engine-pricing-is-pay-for-only-what-you-need)
* [Slide 12: Virtual Machines and Networks in the Cloud](#slide-12-virtual-machines-and-networks-in-the-cloud)
* [Slide 13: VMs can be auto-scaled to meet demand](#slide-13-vms-can-be-auto-scaled-to-meet-demand)
* [Slide 14: VM machineVM machine type  specifications type specifications](#slide-14-vm-machinevm-machine-type-specifications-type-specifications)
* [Slide 15: Virtual Machines and Networks in the Cloud](#slide-15-virtual-machines-and-networks-in-the-cloud)
* [Slide 16: VPCs do not require a router to be provisioned](#slide-16-vpcs-do-not-require-a-router-to-be-provisioned)
* [Slide 17: VPCs also do not require a firewall to be provisioned](#slide-17-vpcs-also-do-not-require-a-firewall-to-be-provisioned)
* [Slide 18: VPC peering and sharing allow projects to communicate](#slide-18-vpc-peering-and-sharing-allow-projects-to-communicate)
* [Slide 19: Virtual Machines and Networks in the Cloud](#slide-19-virtual-machines-and-networks-in-the-cloud)
* [Slide 20: Load balancing distributes traffic across instances](#slide-20-load-balancing-distributes-traffic-across-instances)
* [Slide 21: Cloud Load](#slide-21-cloud-load)
* [Slide 22: No "pre-warming" is required for  anticipated spikes in traffic Cloud Load](#slide-22-no-pre-warming-is-required-for-anticipated-spikes-in-traffic-cloud-load)
* [Slide 23: There are several load balancing options](#slide-23-there-are-several-load-balancing-options)
* [Slide 24: preserving the original source IP address. This type is well-suited for applications that  require direct server return or need to handle a wider range of IP protocols.](#slide-24-preserving-the-original-source-ip-address-this-type-is-well-suited-for-applications-that-require-direct-server-return-or-need-to-handle-a-wider-range-of-ip-protocols)
* [Slide 25: Virtual Machines and Networks in the Cloud](#slide-25-virtual-machines-and-networks-in-the-cloud)
* [Slide 26: 8.8.8.8](#slide-26-8888)
* [Slide 27: Cloud DNS](#slide-27-cloud-dns)
* [Slide 28: Virtual Machines and Networks in the Cloud](#slide-28-virtual-machines-and-networks-in-the-cloud)
* [Slide 29: Edge caching](#slide-29-edge-caching)
* [Slide 30: Cloud CDN](#slide-30-cloud-cdn)
* [Slide 31: Virtual Machines and Networks in the Cloud](#slide-31-virtual-machines-and-networks-in-the-cloud)
* [Slide 32: Google VPC networks can connect to other networks](#slide-32-google-vpc-networks-can-connect-to-other-networks)
* [Slide 33: Cloud VPN creates dynamic connections](#slide-33-cloud-vpn-creates-dynamic-connections)
* [Slide 34: Direct peering routes traffic through a Google PoP](#slide-34-direct-peering-routes-traffic-through-a-google-pop)
* [Slide 35: Carrier peering allows access to Google Workspace](#slide-35-carrier-peering-allows-access-to-google-workspace)
* [Slide 36: Dedicated Interconnect is a direct connection to Google](#slide-36-dedicated-interconnect-is-a-direct-connection-to-google)
* [Slide 37: Partner Interconnect links your on-prem with your VPC](#slide-37-partner-interconnect-links-your-on-prem-with-your-vpc)
* [Slide 38: Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider](#slide-38-cross-cloud-interconnect-connects-to-a-network-hosted-by-another-cloud-service-provider)
* [Slide 39: Networking options decision tree](#slide-39-networking-options-decision-tree)
* [Slide 40: Slide 40](#slide-40-slide-40)
* [Slide 41: Module Quiz](#slide-41-module-quiz)
* [Slide 42: Quiz | Question 1](#slide-42-quiz-question-1)
* [Slide 43: Quiz | Question 1](#slide-43-quiz-question-1)
* [Slide 44: Quiz | Question 2](#slide-44-quiz-question-2)
* [Slide 45: Quiz | Question 2](#slide-45-quiz-question-2)
* [Slide 46: Quiz | Question 3](#slide-46-quiz-question-3)
* [Slide 47: Quiz | Question 3](#slide-47-quiz-question-3)
* [Slide 48: Quiz | Question 4](#slide-48-quiz-question-4)
* [Slide 49: Quiz | Question 4](#slide-49-quiz-question-4)
* [Slide 50: Quiz | Question 5](#slide-50-quiz-question-5)
* [Slide 51: Quiz | Question 5](#slide-51-quiz-question-5)
* [Slide 52: Lab Intro](#slide-52-lab-intro)

---

## List of Figures

* **Figure 1:** [Slide 1] Virtual Machines and  Networks in the Cloud 03 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 2:** [Slide 1] Virtual Machines and  Networks in the Cloud 03 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 3:** [Slide 2] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 4:** [Slide 2] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 5:** [Slide 3] Virtual Private Cloud (VPC) is your cloud within the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 6:** [Slide 3] Virtual Private Cloud (VPC) is your cloud within the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 7:** [Slide 4] Virtual Private — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 8:** [Slide 4] Virtual Private — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 9:** [Slide 4] Virtual Private — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 10:** [Slide 4] Virtual Private — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 11:** [Slide 4] Virtual Private — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 12:** [Slide 5] VPC subnets connect resources in different zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 13:** [Slide 5] VPC subnets connect resources in different zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 14:** [Slide 5] VPC subnets connect resources in different zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 15:** [Slide 5] VPC subnets connect resources in different zones — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 16:** [Slide 6] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 17:** [Slide 6] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 18:** [Slide 7] Compute Engine — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 19:** [Slide 7] Compute Engine — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 20:** [Slide 7] Compute Engine — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 21:** [Slide 7] Compute Engine — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 22:** [Slide 7] Compute Engine — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 23:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 24:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 25:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 26:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 27:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 28:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 29:** [Slide 8] Virtual machine instances are flexible resources — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 30:** [Slide 9] Cloud Marketplace — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 31:** [Slide 9] Cloud Marketplace — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 32:** [Slide 10] Compute Engine pricing and billing offers discounts — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 33:** [Slide 10] Compute Engine pricing and billing offers discounts — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 34:** [Slide 10] Compute Engine pricing and billing offers discounts — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 35:** [Slide 10] Compute Engine pricing and billing offers discounts — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 36:** [Slide 10] Compute Engine pricing and billing offers discounts — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 37:** [Slide 11] Compute Engine pricing is "pay for only what you need" — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 38:** [Slide 11] Compute Engine pricing is "pay for only what you need" — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 39:** [Slide 11] Compute Engine pricing is "pay for only what you need" — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 40:** [Slide 11] Compute Engine pricing is "pay for only what you need" — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 41:** [Slide 12] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 42:** [Slide 12] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 43:** [Slide 13] VMs can be auto-scaled to meet demand — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 44:** [Slide 13] VMs can be auto-scaled to meet demand — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 45:** [Slide 13] VMs can be auto-scaled to meet demand — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 46:** [Slide 14] VM machineVM machine type  specifications type specifications — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 47:** [Slide 15] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 48:** [Slide 15] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 49:** [Slide 16] VPCs do not require a router to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 50:** [Slide 16] VPCs do not require a router to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 51:** [Slide 16] VPCs do not require a router to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 52:** [Slide 16] VPCs do not require a router to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 53:** [Slide 17] VPCs also do not require a firewall to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 54:** [Slide 17] VPCs also do not require a firewall to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 55:** [Slide 17] VPCs also do not require a firewall to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 56:** [Slide 17] VPCs also do not require a firewall to be provisioned — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 57:** [Slide 18] VPC peering and sharing allow projects to communicate — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 58:** [Slide 18] VPC peering and sharing allow projects to communicate — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 59:** [Slide 18] VPC peering and sharing allow projects to communicate — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 60:** [Slide 18] VPC peering and sharing allow projects to communicate — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 61:** [Slide 18] VPC peering and sharing allow projects to communicate — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 62:** [Slide 19] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 63:** [Slide 19] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 64:** [Slide 20] Load balancing distributes traffic across instances — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 65:** [Slide 20] Load balancing distributes traffic across instances — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 66:** [Slide 20] Load balancing distributes traffic across instances — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 67:** [Slide 21] Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 68:** [Slide 21] Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 69:** [Slide 21] Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 70:** [Slide 21] Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 71:** [Slide 21] Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 72:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 73:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 74:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 75:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 76:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 77:** [Slide 23] There are several load balancing options — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 78:** [Slide 24] preserving the original source IP address. This type is well-suited for applications that  require direct server return or need to handle a wider range of IP protocols. — *System Flowchart & Process Architecture* (`📊 Flowchart`)
* **Figure 79:** [Slide 25] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 80:** [Slide 25] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 81:** [Slide 26] 8.8.8.8 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 82:** [Slide 26] 8.8.8.8 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 83:** [Slide 27] Cloud DNS — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 84:** [Slide 27] Cloud DNS — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 85:** [Slide 27] Cloud DNS — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 86:** [Slide 27] Cloud DNS — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 87:** [Slide 27] Cloud DNS — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 88:** [Slide 28] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 89:** [Slide 28] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 90:** [Slide 29] Edge caching — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 91:** [Slide 29] Edge caching — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 92:** [Slide 30] Cloud CDN — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 93:** [Slide 30] Cloud CDN — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 94:** [Slide 30] Cloud CDN — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 95:** [Slide 30] Cloud CDN — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 96:** [Slide 31] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 97:** [Slide 31] Virtual Machines and Networks in the Cloud — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 98:** [Slide 32] Google VPC networks can connect to other networks — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 99:** [Slide 32] Google VPC networks can connect to other networks — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 100:** [Slide 32] Google VPC networks can connect to other networks — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 101:** [Slide 33] Cloud VPN creates dynamic connections — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 102:** [Slide 33] Cloud VPN creates dynamic connections — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 103:** [Slide 33] Cloud VPN creates dynamic connections — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 104:** [Slide 33] Cloud VPN creates dynamic connections — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 105:** [Slide 34] Direct peering routes traffic through a Google PoP — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 106:** [Slide 34] Direct peering routes traffic through a Google PoP — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 107:** [Slide 34] Direct peering routes traffic through a Google PoP — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 108:** [Slide 35] Carrier peering allows access to Google Workspace — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 109:** [Slide 35] Carrier peering allows access to Google Workspace — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 110:** [Slide 35] Carrier peering allows access to Google Workspace — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 111:** [Slide 36] Dedicated Interconnect is a direct connection to Google — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 112:** [Slide 36] Dedicated Interconnect is a direct connection to Google — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 113:** [Slide 36] Dedicated Interconnect is a direct connection to Google — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 114:** [Slide 37] Partner Interconnect links your on-prem with your VPC — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 115:** [Slide 37] Partner Interconnect links your on-prem with your VPC — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 116:** [Slide 37] Partner Interconnect links your on-prem with your VPC — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 117:** [Slide 37] Partner Interconnect links your on-prem with your VPC — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 118:** [Slide 38] Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 119:** [Slide 38] Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 120:** [Slide 39] Networking options decision tree — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 121:** [Slide 39] Networking options decision tree — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 122:** [Slide 39] Networking options decision tree — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 123:** [Slide 41] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 124:** [Slide 41] Module Quiz — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 125:** [Slide 42] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 126:** [Slide 43] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 127:** [Slide 43] Quiz | Question 1 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 128:** [Slide 44] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 129:** [Slide 45] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 130:** [Slide 45] Quiz | Question 2 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 131:** [Slide 46] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 132:** [Slide 47] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 133:** [Slide 47] Quiz | Question 3 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 134:** [Slide 48] Quiz | Question 4 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 135:** [Slide 49] Quiz | Question 4 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 136:** [Slide 49] Quiz | Question 4 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 137:** [Slide 50] Quiz | Question 5 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 138:** [Slide 51] Quiz | Question 5 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 139:** [Slide 51] Quiz | Question 5 — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 140:** [Slide 52] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)
* **Figure 141:** [Slide 52] Lab Intro — *Visual Illustration & Context Reference* (`🖼️ Visual`)

---

<a id="slide-1-virtual-machines-and-networks-in-the-cloud-03"></a>
### Slide 1: Virtual Machines and  Networks in the Cloud 03


<!-- INJECT_START: slide_01_img_02 -->
![Virtual Machines and  Networks in the Cloud 03 (slide_01_img_02)](media/slide_01_img_02.jpeg)

**Figure 2:** [Slide 1] Virtual Machines and  Networks in the Cloud 03 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_02 -->

* Proprietary + Confidential
* Virtual Machines and
* Networks in the Cloud
* 03

<!-- INJECT_START: slide_01_img_01 -->
![Virtual Machines and  Networks in the Cloud 03 (slide_01_img_01)](media/slide_01_img_01.jpeg)

**Figure 1:** [Slide 1] Virtual Machines and  Networks in the Cloud 03 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_01_img_01 -->

* In this module, we're going to explore how Google Compute Engine works, with a
* focus on virtual networking.
* Let's begin.

---

<a id="slide-2-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 2: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_02_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_02_img_02)](media/slide_02_img_02.jpeg)

**Figure 4:** [Slide 2] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_02_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_02_img_01)](media/slide_02_img_01.jpeg)

**Figure 3:** [Slide 2] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_02_img_01 -->

* Many users start with Google Cloud by defining their own virtual private cloud inside
* their first Google Cloud project or by starting with the default virtual private cloud.
* So, what is a virtual private cloud?

---

<a id="slide-3-virtual-private-cloud-vpc-is-your-cloud-within-the-cloud"></a>
### Slide 3: Virtual Private Cloud (VPC) is your cloud within the Cloud


<!-- INJECT_START: slide_03_img_02 -->
![Virtual Private Cloud (VPC) is your cloud within the Cloud (slide_03_img_02)](media/slide_03_img_02.jpeg)

**Figure 6:** [Slide 3] Virtual Private Cloud (VPC) is your cloud within the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_02 -->


<!-- INJECT_START: slide_03_img_01 -->
![Virtual Private Cloud (VPC) is your cloud within the Cloud (slide_03_img_01)](media/slide_03_img_01.jpeg)

**Figure 5:** [Slide 3] Virtual Private Cloud (VPC) is your cloud within the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_03_img_01 -->

  * A virtual private cloud, or VPC, is a secure, individual, private cloud-computing model
  * hosted within a public cloud  like Google Cloud!
* On a VPC, customers can run code, store data, host websites, and do anything else
* they could do in an ordinary private cloud, but this private cloud is hosted remotely by
* a public cloud provider. This means that VPCs combine the scalability and
* convenience of public cloud computing with the data isolation of private cloud
* computing.

---

<a id="slide-4-virtual-private"></a>
### Slide 4: Virtual Private


<!-- INJECT_START: slide_04_img_04 -->
![Virtual Private (slide_04_img_04)](media/slide_04_img_04.jpeg)

**Figure 10:** [Slide 4] Virtual Private — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_04 -->


<!-- INJECT_START: slide_04_img_02 -->
![Virtual Private (slide_04_img_02)](media/slide_04_img_02.jpeg)

**Figure 8:** [Slide 4] Virtual Private — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_02 -->


<!-- INJECT_START: slide_04_img_03 -->
![Virtual Private (slide_04_img_03)](media/slide_04_img_03.jpeg)

**Figure 9:** [Slide 4] Virtual Private — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_03 -->


<!-- INJECT_START: slide_04_img_05 -->
![Virtual Private (slide_04_img_05)](media/slide_04_img_05.jpeg)

**Figure 11:** [Slide 4] Virtual Private — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_05 -->


<!-- INJECT_START: slide_04_img_01 -->
![Virtual Private (slide_04_img_01)](media/slide_04_img_01.jpeg)

**Figure 7:** [Slide 4] Virtual Private — Visual Illustration & Context Reference
<!-- INJECT_END: slide_04_img_01 -->

* Virtual Private Cloud (VPC) networks connect Google Cloud resources to each other
* and to the internet. This includes segmenting networks, using firewall rules to restrict
* access to instances, and creating static routes to forward traffic to specific
* destinations.
* Here's something that tends to surprise a lot of new Google Cloud users: Google
* Cloud VPC networks are global. They can also have subnets, which is a segmented
* piece of the larger network, in any Google Cloud region worldwide. Subnets can span
* the zones that make up a region. This architecture makes it easy to define network
* layouts with global scope. Resources can even be in different zones on the same
* subnet.

---

<a id="slide-5-vpc-subnets-connect-resources-in-different-zones"></a>
### Slide 5: VPC subnets connect resources in different zones

* Proprietary + Confidential
* **Region:** asia-east1
* asia-east1-a
* asia-east1-b
* asia-east1-c

<!-- INJECT_START: slide_05_img_03 -->
![VPC subnets connect resources in different zones (slide_05_img_03)](media/slide_05_img_03.jpeg)

**Figure 14:** [Slide 5] VPC subnets connect resources in different zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_03 -->

* subnet 1

<!-- INJECT_START: slide_05_img_04 -->
![VPC subnets connect resources in different zones (slide_05_img_04)](media/slide_05_img_04.jpeg)

**Figure 15:** [Slide 5] VPC subnets connect resources in different zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_04 -->

* 10.0.0.0/24
* 10.0.0.2
* 10.0.0.3
* 10.0.0.4
* **Region:** us-east1
* us-east1-b
* us-east1-c
* us-east1-d

<!-- INJECT_START: slide_05_img_02 -->
![VPC subnets connect resources in different zones (slide_05_img_02)](media/slide_05_img_02.jpeg)

**Figure 13:** [Slide 5] VPC subnets connect resources in different zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_02 -->

* VPC
* subnet 2
* 10.0.1.0/24
* 10.0.1.2
* 10.0.1.3
* 10.0.1.4
* vpc1

<!-- INJECT_START: slide_05_img_01 -->
![VPC subnets connect resources in different zones (slide_05_img_01)](media/slide_05_img_01.jpeg)

**Figure 12:** [Slide 5] VPC subnets connect resources in different zones — Visual Illustration & Context Reference
<!-- INJECT_END: slide_05_img_01 -->

* The size of a subnet can be increased by expanding the range of IP addresses
* allocated to it. And doing so won't affect already configured virtual machines.
* For example, let's take a VPC network named vpc1 that has two subnets defined in
* the asia-east1 and us-east1 regions. If the VPC has three Compute Engine VMs
* attached to it, it means they're neighbors on the same subnet even though they are in
* different zones! This capability can be used to build solutions that are resilient to
* disruptions, yet retain a simple network layout.

---

<a id="slide-6-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 6: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_06_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_06_img_02)](media/slide_06_img_02.jpeg)

**Figure 17:** [Slide 6] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_06_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_06_img_01)](media/slide_06_img_01.jpeg)

**Figure 16:** [Slide 6] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_06_img_01 -->

* Earlier in the course, we explored Infrastructure as a Service, or IaaS. Now let's
* **explore Google Cloud's IaaS solution:** Google Compute Engine.

---

<a id="slide-7-compute-engine"></a>
### Slide 7: Compute Engine


<!-- INJECT_START: slide_07_img_04 -->
![Compute Engine (slide_07_img_04)](media/slide_07_img_04.jpeg)

**Figure 21:** [Slide 7] Compute Engine — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_04 -->


<!-- INJECT_START: slide_07_img_05 -->
![Compute Engine (slide_07_img_05)](media/slide_07_img_05.jpeg)

**Figure 22:** [Slide 7] Compute Engine — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_05 -->


<!-- INJECT_START: slide_07_img_02 -->
![Compute Engine (slide_07_img_02)](media/slide_07_img_02.jpeg)

**Figure 19:** [Slide 7] Compute Engine — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_02 -->


<!-- INJECT_START: slide_07_img_03 -->
![Compute Engine (slide_07_img_03)](media/slide_07_img_03.jpeg)

**Figure 20:** [Slide 7] Compute Engine — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_03 -->


<!-- INJECT_START: slide_07_img_01 -->
![Compute Engine (slide_07_img_01)](media/slide_07_img_01.jpeg)

**Figure 18:** [Slide 7] Compute Engine — Visual Illustration & Context Reference
<!-- INJECT_END: slide_07_img_01 -->

* With Compute Engine, users can create and run virtual machines on Google
* infrastructure. There are no upfront investments, and thousands of virtual CPUs can
* run on a system that is designed to be fast and offer consistent performance.
* Each virtual machine contains the power and functionality of a full-fledged operating
* system. This means a virtual machine can be configured much like a physical server;
* by specifying the amount of CPU power and memory needed, the amount and type of
* storage needed, and the operating system.

---

<a id="slide-8-virtual-machine-instances-are-flexible-resources"></a>
### Slide 8: Virtual machine instances are flexible resources


<!-- INJECT_START: slide_08_img_06 -->
![Virtual machine instances are flexible resources (slide_08_img_06)](media/slide_08_img_06.jpeg)

**Figure 28:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_06 -->


<!-- INJECT_START: slide_08_img_05 -->
![Virtual machine instances are flexible resources (slide_08_img_05)](media/slide_08_img_05.jpeg)

**Figure 27:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_05 -->


<!-- INJECT_START: slide_08_img_02 -->
![Virtual machine instances are flexible resources (slide_08_img_02)](media/slide_08_img_02.jpeg)

**Figure 24:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_02 -->


<!-- INJECT_START: slide_08_img_03 -->
![Virtual machine instances are flexible resources (slide_08_img_03)](media/slide_08_img_03.jpeg)

**Figure 25:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_03 -->


<!-- INJECT_START: slide_08_img_04 -->
![Virtual machine instances are flexible resources (slide_08_img_04)](media/slide_08_img_04.jpeg)

**Figure 26:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_04 -->


<!-- INJECT_START: slide_08_img_07 -->
![Virtual machine instances are flexible resources (slide_08_img_07)](media/slide_08_img_07.jpeg)

**Figure 29:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_07 -->

* VM can be created using
* the Google Cloud console, the
* Google Cloud CLI, or the
* Compute Engine API

<!-- INJECT_START: slide_08_img_01 -->
![Virtual machine instances are flexible resources (slide_08_img_01)](media/slide_08_img_01.jpeg)

**Figure 23:** [Slide 8] Virtual machine instances are flexible resources — Visual Illustration & Context Reference
<!-- INJECT_END: slide_08_img_01 -->

* You can create a virtual machine instance or create a group of managed instances by
* using the Google Cloud console, which is a web-based tool to manage Google Cloud
* projects and resources, the Google Cloud CLI, or the Compute Engine API.
* The instance can run Linux and Windows Server images provided by Google, or any
* customized versions of these images. You can also build and run images of other
* operating systems and flexibly reconfigure virtual machines.

---

<a id="slide-9-cloud-marketplace"></a>
### Slide 9: Cloud Marketplace


<!-- INJECT_START: slide_09_img_02 -->
![Cloud Marketplace (slide_09_img_02)](media/slide_09_img_02.jpeg)

**Figure 31:** [Slide 9] Cloud Marketplace — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_02 -->


<!-- INJECT_START: slide_09_img_01 -->
![Cloud Marketplace (slide_09_img_01)](media/slide_09_img_01.jpeg)

**Figure 30:** [Slide 9] Cloud Marketplace — Visual Illustration & Context Reference
<!-- INJECT_END: slide_09_img_01 -->

* A quick way to get started with Google Cloud is through the Cloud Marketplace, which
* offers solutions from both Google and third-party vendors. With these solutions,
* there's no need to manually configure the software, virtual machine instances,
* storage, or network settings, although many of them can be modified before launch if
* that's required.
* Most software packages in Cloud Marketplace are available at no additional charge
* beyond the normal usage fees for Google Cloud resources. Some Cloud Marketplace
* images charge usage fees, particularly those published by third parties, with
* commercially licensed software, but they all show estimates of their monthly charges
* before they're launched.

---

<a id="slide-10-compute-engine-pricing-and-billing-offers-discounts"></a>
### Slide 10: Compute Engine pricing and billing offers discounts


<!-- INJECT_START: slide_10_img_05 -->
![Compute Engine pricing and billing offers discounts (slide_10_img_05)](media/slide_10_img_05.jpeg)

**Figure 36:** [Slide 10] Compute Engine pricing and billing offers discounts — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_05 -->


<!-- INJECT_START: slide_10_img_02 -->
![Compute Engine pricing and billing offers discounts (slide_10_img_02)](media/slide_10_img_02.jpeg)

**Figure 33:** [Slide 10] Compute Engine pricing and billing offers discounts — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_02 -->


<!-- INJECT_START: slide_10_img_03 -->
![Compute Engine pricing and billing offers discounts (slide_10_img_03)](media/slide_10_img_03.jpeg)

**Figure 34:** [Slide 10] Compute Engine pricing and billing offers discounts — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_03 -->


<!-- INJECT_START: slide_10_img_04 -->
![Compute Engine pricing and billing offers discounts (slide_10_img_04)](media/slide_10_img_04.jpeg)

**Figure 35:** [Slide 10] Compute Engine pricing and billing offers discounts — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_04 -->


<!-- INJECT_START: slide_10_img_01 -->
![Compute Engine pricing and billing offers discounts (slide_10_img_01)](media/slide_10_img_01.jpeg)

**Figure 32:** [Slide 10] Compute Engine pricing and billing offers discounts — Visual Illustration & Context Reference
<!-- INJECT_END: slide_10_img_01 -->

* At this point, you might be wondering about pricing and billing related to Compute
* Engine.
* For the use of virtual machines, Compute Engine bills by the second with a
* one-minute minimum, and sustained-use discounts start to apply automatically to
* virtual machines the longer they run. So, for each VM that runs for more than 25% of a
* month, Compute Engine automatically applies a discount for every additional minute.
* Compute Engine also offers committed-use discounts. This means that for stable
* and predictable workloads, a specific amount of vCPUs and memory can be
* purchased for up to a 57% discount off of normal prices in return for committing to a
* usage term of one year or three years.
  * Then there are Spot VMs. These are perfect for workloads that don't require
  * immediate human oversightlike a batch job analyzing a large dataset. By opting for
  * Spot VMs, you can save up to 90% compared to standard pricing. Unlike the older
  * 'Preemptible' model, Spot VMs have no maximum runtime; they can run as long as the
  * capacity is available.
* The primary trade-off is that Google Cloud reserves the right to terminate the instance
* if those resources are needed elsewhere. While the savings are significant, you must
* ensure your workload is designed to be stopped and restarted without losing
* progress.

---

<a id="slide-11-compute-engine-pricing-is-pay-for-only-what-you-need"></a>
### Slide 11: Compute Engine pricing is "pay for only what you need"


<!-- INJECT_START: slide_11_img_04 -->
![Compute Engine pricing is "pay for only what you need" (slide_11_img_04)](media/slide_11_img_04.jpeg)

**Figure 40:** [Slide 11] Compute Engine pricing is "pay for only what you need" — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_04 -->


<!-- INJECT_START: slide_11_img_02 -->
![Compute Engine pricing is "pay for only what you need" (slide_11_img_02)](media/slide_11_img_02.jpeg)

**Figure 38:** [Slide 11] Compute Engine pricing is "pay for only what you need" — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_02 -->


<!-- INJECT_START: slide_11_img_03 -->
![Compute Engine pricing is "pay for only what you need" (slide_11_img_03)](media/slide_11_img_03.jpeg)

**Figure 39:** [Slide 11] Compute Engine pricing is "pay for only what you need" — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_03 -->


<!-- INJECT_START: slide_11_img_01 -->
![Compute Engine pricing is "pay for only what you need" (slide_11_img_01)](media/slide_11_img_01.jpeg)

**Figure 37:** [Slide 11] Compute Engine pricing is "pay for only what you need" — Visual Illustration & Context Reference
<!-- INJECT_END: slide_11_img_01 -->

* In terms of storage, Compute Engine doesn't require a particular option or machine
* type to get high throughput between processing and persistent disks. That's the
* default, and it comes to you at no extra cost.
* Compute Engine offers several types of storage options for your instances. Each of
* the following storage options has unique price and performance characteristics:
* ●
* **Zonal persistent disk:** Efficient, reliable block storage.
* ●
* **Regional persistent disk:** Regional block storage replicated in two zones.
* ●
* **Local SSD:** High performance, transient, local block storage.
* ●
* **Cloud Storage buckets:** Affordable object storage.
* ●
* **Filestore:** High performance file storage for Google Cloud users.
* If you are not sure which option to use, the most common solution is to add a
* persistent disk to your instance.
* And finally, you'll only pay for what you need with custom machine types. Compute
* Engine lets you choose the machine properties of your instances, like the number of
* virtual CPUs and the amount of memory, by using a set of predefined machine types
* or by creating your own custom machine types.
* For more information, see Storage options at
* https://cloud.google.com/compute/docs/disks

---

<a id="slide-12-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 12: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_12_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_12_img_02)](media/slide_12_img_02.jpeg)

**Figure 42:** [Slide 12] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_12_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_12_img_01)](media/slide_12_img_01.jpeg)

**Figure 41:** [Slide 12] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_12_img_01 -->


---

<a id="slide-13-vms-can-be-auto-scaled-to-meet-demand"></a>
### Slide 13: VMs can be auto-scaled to meet demand

* Proprietary + Confidential

<!-- INJECT_START: slide_13_img_02 -->
![VMs can be auto-scaled to meet demand (slide_13_img_02)](media/slide_13_img_02.jpeg)

**Figure 44:** [Slide 13] VMs can be auto-scaled to meet demand — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_02 -->


<!-- INJECT_START: slide_13_img_03 -->
![VMs can be auto-scaled to meet demand (slide_13_img_03)](media/slide_13_img_03.jpeg)

**Figure 45:** [Slide 13] VMs can be auto-scaled to meet demand — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_03 -->


<!-- INJECT_START: slide_13_img_01 -->
![VMs can be auto-scaled to meet demand (slide_13_img_01)](media/slide_13_img_01.jpeg)

**Figure 43:** [Slide 13] VMs can be auto-scaled to meet demand — Visual Illustration & Context Reference
<!-- INJECT_END: slide_13_img_01 -->

* As we've just seen, with Compute Engine, you can choose the most appropriate
* machine properties for your instances, like the number of virtual CPUs and the
* amount of memory, by using a set of predefined machine types, or by creating custom
* machine types.
* To do this, Compute Engine has a feature called Autoscaling, where VMs can be
* added to or subtracted from an application based on load metrics. The other part of
* making that work is balancing the incoming traffic among the VMs. Google's Virtual
* Private Cloud (VPC) supports several different kinds of load balancing, which we'll
* explore shortly.
* With Compute Engine, you can in fact configure very large VMs, which are great for
* workloads such as in-memory databases and CPU-intensive analytics, but most
* Google Cloud customers start off with scaling out, not up. The maximum number of
* CPUs per VM is tied to its "machine family" and is also constrained by the quota
* available to the user, which is zone-dependent.

---

<a id="slide-14-vm-machinevm-machine-type-specifications-type-specifications"></a>
### Slide 14: VM machineVM machine type  specifications type specifications

* Proprietary + Confidential
* VM machineVM machine type
* specifications type specifications
* Specs for currently available VM machine types:
* cloud.google.com/compute/docs/machine-types

<!-- INJECT_START: slide_14_img_01 -->
![VM machineVM machine type  specifications type specifications (slide_14_img_01)](media/slide_14_img_01.jpeg)

**Figure 46:** [Slide 14] VM machineVM machine type  specifications type specifications — Visual Illustration & Context Reference
<!-- INJECT_END: slide_14_img_01 -->

* Specs for currently available VM machine types can be found at
* https://cloud.google.com/compute/docs/machine-types

---

<a id="slide-15-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 15: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_15_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_15_img_02)](media/slide_15_img_02.jpeg)

**Figure 48:** [Slide 15] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_15_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_15_img_01)](media/slide_15_img_01.jpeg)

**Figure 47:** [Slide 15] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_15_img_01 -->

* Now let's explore some of the most important Virtual Private Cloud compatibility
* features.

---

<a id="slide-16-vpcs-do-not-require-a-router-to-be-provisioned"></a>
### Slide 16: VPCs do not require a router to be provisioned


<!-- INJECT_START: slide_16_img_02 -->
![VPCs do not require a router to be provisioned (slide_16_img_02)](media/slide_16_img_02.jpeg)

**Figure 50:** [Slide 16] VPCs do not require a router to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_02 -->


<!-- INJECT_START: slide_16_img_03 -->
![VPCs do not require a router to be provisioned (slide_16_img_03)](media/slide_16_img_03.jpeg)

**Figure 51:** [Slide 16] VPCs do not require a router to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_03 -->


<!-- INJECT_START: slide_16_img_04 -->
![VPCs do not require a router to be provisioned (slide_16_img_04)](media/slide_16_img_04.jpeg)

**Figure 52:** [Slide 16] VPCs do not require a router to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_04 -->


<!-- INJECT_START: slide_16_img_01 -->
![VPCs do not require a router to be provisioned (slide_16_img_01)](media/slide_16_img_01.jpeg)

**Figure 49:** [Slide 16] VPCs do not require a router to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_16_img_01 -->

* Much like physical networks, VPCs have routing tables. VPC routing tables are built-in
* so you don't have to provision or manage a router. They are used to forward traffic
* from one instance to another within the same network, across subnetworks, or even
* between Google Cloud zones, without requiring an external IP address.

---

<a id="slide-17-vpcs-also-do-not-require-a-firewall-to-be-provisioned"></a>
### Slide 17: VPCs also do not require a firewall to be provisioned


<!-- INJECT_START: slide_17_img_02 -->
![VPCs also do not require a firewall to be provisioned (slide_17_img_02)](media/slide_17_img_02.jpeg)

**Figure 54:** [Slide 17] VPCs also do not require a firewall to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_02 -->


<!-- INJECT_START: slide_17_img_03 -->
![VPCs also do not require a firewall to be provisioned (slide_17_img_03)](media/slide_17_img_03.jpeg)

**Figure 55:** [Slide 17] VPCs also do not require a firewall to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_03 -->


<!-- INJECT_START: slide_17_img_04 -->
![VPCs also do not require a firewall to be provisioned (slide_17_img_04)](media/slide_17_img_04.jpeg)

**Figure 56:** [Slide 17] VPCs also do not require a firewall to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_04 -->


<!-- INJECT_START: slide_17_img_01 -->
![VPCs also do not require a firewall to be provisioned (slide_17_img_01)](media/slide_17_img_01.jpeg)

**Figure 53:** [Slide 17] VPCs also do not require a firewall to be provisioned — Visual Illustration & Context Reference
<!-- INJECT_END: slide_17_img_01 -->

* Another thing you don't have to provision or manage for Google Cloud is a firewall.
* VPCs provide a global distributed firewall, which can be controlled to restrict access
* to instances through both incoming and outgoing traffic.
* Firewall rules can be defined through network tags on Compute Engine instances,
* which is really convenient.
* For example, you can tag all your web servers with, say, "WEB," and write a firewall rule
* saying that traffic on ports 80 or 443 is allowed into all VMs with the "WEB" tag, no
* matter what their IP address happens to be.

---

<a id="slide-18-vpc-peering-and-sharing-allow-projects-to-communicate"></a>
### Slide 18: VPC peering and sharing allow projects to communicate

* Proprietary + Confidential

<!-- INJECT_START: slide_18_img_02 -->
![VPC peering and sharing allow projects to communicate (slide_18_img_02)](media/slide_18_img_02.jpeg)

**Figure 58:** [Slide 18] VPC peering and sharing allow projects to communicate — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_02 -->


<!-- INJECT_START: slide_18_img_03 -->
![VPC peering and sharing allow projects to communicate (slide_18_img_03)](media/slide_18_img_03.jpeg)

**Figure 59:** [Slide 18] VPC peering and sharing allow projects to communicate — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_03 -->


<!-- INJECT_START: slide_18_img_04 -->
![VPC peering and sharing allow projects to communicate (slide_18_img_04)](media/slide_18_img_04.jpeg)

**Figure 60:** [Slide 18] VPC peering and sharing allow projects to communicate — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_04 -->


<!-- INJECT_START: slide_18_img_05 -->
![VPC peering and sharing allow projects to communicate (slide_18_img_05)](media/slide_18_img_05.jpeg)

**Figure 61:** [Slide 18] VPC peering and sharing allow projects to communicate — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_05 -->

* VPC peering
* Shared VPC

<!-- INJECT_START: slide_18_img_01 -->
![VPC peering and sharing allow projects to communicate (slide_18_img_01)](media/slide_18_img_01.jpeg)

**Figure 57:** [Slide 18] VPC peering and sharing allow projects to communicate — Visual Illustration & Context Reference
<!-- INJECT_END: slide_18_img_01 -->

* You'll remember that VPCs belong to Google Cloud projects, but what if your company
* has several Google Cloud projects and the VPCs need to talk to each other?
* With VPC Peering, a relationship between two VPCs can be established to exchange
* traffic.
* Alternatively, to use the full power of identity access management (IAM) to control
* who and what in one project can interact with a VPC in another, then you can
* configure a Shared VPC.

---

<a id="slide-19-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 19: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_19_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_19_img_02)](media/slide_19_img_02.jpeg)

**Figure 63:** [Slide 19] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_19_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_19_img_01)](media/slide_19_img_01.jpeg)

**Figure 62:** [Slide 19] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_19_img_01 -->

* Previously, we explored how virtual machines can autoscale to respond to changing
* loads. But how do your customers get to your application when it might be provided
* by four VMs one moment, and by forty VMs at another? That's done through Cloud
* Load Balancing.

---

<a id="slide-20-load-balancing-distributes-traffic-across-instances"></a>
### Slide 20: Load balancing distributes traffic across instances

* Proprietary + Confidential

<!-- INJECT_START: slide_20_img_02 -->
![Load balancing distributes traffic across instances (slide_20_img_02)](media/slide_20_img_02.jpeg)

**Figure 65:** [Slide 20] Load balancing distributes traffic across instances — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_02 -->


<!-- INJECT_START: slide_20_img_03 -->
![Load balancing distributes traffic across instances (slide_20_img_03)](media/slide_20_img_03.jpeg)

**Figure 66:** [Slide 20] Load balancing distributes traffic across instances — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_03 -->


<!-- INJECT_START: slide_20_img_01 -->
![Load balancing distributes traffic across instances (slide_20_img_01)](media/slide_20_img_01.jpeg)

**Figure 64:** [Slide 20] Load balancing distributes traffic across instances — Visual Illustration & Context Reference
<!-- INJECT_END: slide_20_img_01 -->

* The job of a load balancer is to distribute user traffic across multiple instances of an
* application. By spreading the load, load balancing reduces the risk that applications
* experience performance issues.

---

<a id="slide-21-cloud-load"></a>
### Slide 21: Cloud Load


<!-- INJECT_START: slide_21_img_04 -->
![Cloud Load (slide_21_img_04)](media/slide_21_img_04.jpeg)

**Figure 70:** [Slide 21] Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_04 -->


<!-- INJECT_START: slide_21_img_02 -->
![Cloud Load (slide_21_img_02)](media/slide_21_img_02.jpeg)

**Figure 68:** [Slide 21] Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_02 -->


<!-- INJECT_START: slide_21_img_03 -->
![Cloud Load (slide_21_img_03)](media/slide_21_img_03.jpeg)

**Figure 69:** [Slide 21] Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_03 -->


<!-- INJECT_START: slide_21_img_05 -->
![Cloud Load (slide_21_img_05)](media/slide_21_img_05.jpeg)

**Figure 71:** [Slide 21] Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_05 -->


<!-- INJECT_START: slide_21_img_01 -->
![Cloud Load (slide_21_img_01)](media/slide_21_img_01.jpeg)

**Figure 67:** [Slide 21] Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_21_img_01 -->

* Cloud Load Balancing is a fully distributed, software-defined, managed service for all
* your traffic. And because the load balancers don't run in VMs that you have to
* manage, you don't have to worry about scaling or managing them. You can put Cloud
* Load Balancing in front of all of your traffic: HTTP(S), other TCP and SSL traffic, and
* UDP traffic too.

---

<a id="slide-22-no-pre-warming-is-required-for-anticipated-spikes-in-traffic-cloud-load"></a>
### Slide 22: No "pre-warming" is required for  anticipated spikes in traffic Cloud Load


<!-- INJECT_START: slide_22_img_04 -->
![No "pre-warming" is required for  anticipated spikes in traffic Cloud Load (slide_22_img_04)](media/slide_22_img_04.jpeg)

**Figure 75:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_04 -->


<!-- INJECT_START: slide_22_img_05 -->
![No "pre-warming" is required for  anticipated spikes in traffic Cloud Load (slide_22_img_05)](media/slide_22_img_05.jpeg)

**Figure 76:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_05 -->


<!-- INJECT_START: slide_22_img_02 -->
![No "pre-warming" is required for  anticipated spikes in traffic Cloud Load (slide_22_img_02)](media/slide_22_img_02.jpeg)

**Figure 73:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_02 -->


<!-- INJECT_START: slide_22_img_03 -->
![No "pre-warming" is required for  anticipated spikes in traffic Cloud Load (slide_22_img_03)](media/slide_22_img_03.jpeg)

**Figure 74:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_03 -->


<!-- INJECT_START: slide_22_img_01 -->
![No "pre-warming" is required for  anticipated spikes in traffic Cloud Load (slide_22_img_01)](media/slide_22_img_01.jpeg)

**Figure 72:** [Slide 22] No "pre-warming" is required for  anticipated spikes in traffic Cloud Load — Visual Illustration & Context Reference
<!-- INJECT_END: slide_22_img_01 -->

* Cloud Load Balancing provides cross-region load balancing, including automatic
* multi-region failover, which gently moves traffic in fractions if backends become
* unhealthy. Cloud Load Balancing reacts quickly to changes in users, traffic, network,
* backend health, and other related conditions.
* And what if you anticipate a huge spike in demand? Say, your online game is already a
* hit; do you need to file a support ticket to warn Google of the incoming load? No. No
* so-called "pre-warming" is required.

---

<a id="slide-23-there-are-several-load-balancing-options"></a>
### Slide 23: There are several load balancing options

* Proprietary + Confidential
* Application Load Balancer (HTTP / HTTPS)
* Network Load Balancer (TCP / UDP / other IP protocols)
* External
* Internal
* Proxy
* Passthrough
* Global
* Regional
* Regional
* Cross-region
* External
* Internal
* External
* Internal
* Global
* external
* Application
* Regional
* Regional
* Cross-region
* Global
* Regional
* Regional
* Cross-region
* Regional
* Regional
* external
* Application
* internal
* Application
* internal
* Application
* Load
* Balancer
* Load
* Balancer
* Load
* Balancer
* Load
* Balancer
* Regional
* Regional
* Global
* external proxy
* Network Load
* Regional
* external proxy
* Network Load
* Regional
* internal proxy
* Cross-region
* internal proxy
* Network Load
* external
* passthrough
* Network Load
* internal
* passthrough
* Network Load
* Network
* Load Balancer
* Balancer
* Balancer
* Balancer
* Balancer
* Balancer

<!-- INJECT_START: slide_23_img_01 -->
![There are several load balancing options (slide_23_img_01)](media/slide_23_img_01.jpeg)

**Figure 77:** [Slide 23] There are several load balancing options — Visual Illustration & Context Reference
<!-- INJECT_END: slide_23_img_01 -->

* Google Cloud offers a range of load balancing solutions that can be classified based
* on the OSI model layer they operate at and their specific functionalities.
* Application Load Balancers
* These load balancers operate at the application layer (layer 7) and are designed to
* handle HTTP and HTTPS traffic, making them ideal for web applications and services
* that require advanced features like content-based routing and SSL/TLS termination.
* Application Load Balancers operate as reverse proxies, distributing incoming traffic
* across multiple backend instances based on rules you define. They are highly flexible
* and can be configured for both internet-facing (external) and internal applications.
* Network Load Balancers
* Network Load Balancers operate at the transport layer (layer 4) and efficiently handle
* TCP, UDP, and other IP protocols. They can be further classified into two types:
* **Proxy Load Balancers:** These also function as reverse proxies, terminating client
* connections and establishing new ones to backend services. They offer advanced
* traffic management capabilities and support backends located both on-premises and
* in various cloud environments.
* **Passthrough Load Balancers:** Unlike proxy load balancers, these do not modify or
* terminate connections. Instead, they directly forward traffic to the backend while

---

<a id="slide-24-preserving-the-original-source-ip-address-this-type-is-well-suited-for-applications-that-require-direct-server-return-or-need-to-handle-a-wider-range-of-ip-protocols"></a>
### Slide 24: preserving the original source IP address. This type is well-suited for applications that  require direct server return or need to handle a wider range of IP protocols.


<!-- INJECT_START: slide_24_fig_01 -->
![preserving the original source IP address. This type is well-suited for applications that  require direct server return or need to handle a wider range of IP protocols. (slide_24_fig_01)](media/slide_24_fig_01.png)

**Figure 78:** [Slide 24] preserving the original source IP address. This type is well-suited for applications that  require direct server return or need to handle a wider range of IP protocols. — System Flowchart & Process Architecture
<!-- INJECT_END: slide_24_fig_01 -->


---

<a id="slide-25-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 25: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_25_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_25_img_02)](media/slide_25_img_02.jpeg)

**Figure 80:** [Slide 25] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_25_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_25_img_01)](media/slide_25_img_01.jpeg)

**Figure 79:** [Slide 25] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_25_img_01 -->


---

<a id="slide-26-8888"></a>
### Slide 26: 8.8.8.8


<!-- INJECT_START: slide_26_img_02 -->
![8.8.8.8 (slide_26_img_02)](media/slide_26_img_02.jpeg)

**Figure 82:** [Slide 26] 8.8.8.8 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_02 -->


<!-- INJECT_START: slide_26_img_01 -->
![8.8.8.8 (slide_26_img_01)](media/slide_26_img_01.jpeg)

**Figure 81:** [Slide 26] 8.8.8.8 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_26_img_01 -->

* One of the most famous free Google services is 8.8.8.8, which provides a public
* Domain Name Service to the world. DNS is what translates Internet hostnames to
* addresses, and as you might imagine, Google has a highly developed DNS
* infrastructure. It makes 8.8.8.8 available so that everybody can take advantage of it.

---

<a id="slide-27-cloud-dns"></a>
### Slide 27: Cloud DNS


<!-- INJECT_START: slide_27_img_04 -->
![Cloud DNS (slide_27_img_04)](media/slide_27_img_04.jpeg)

**Figure 86:** [Slide 27] Cloud DNS — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_04 -->


<!-- INJECT_START: slide_27_img_02 -->
![Cloud DNS (slide_27_img_02)](media/slide_27_img_02.jpeg)

**Figure 84:** [Slide 27] Cloud DNS — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_02 -->


<!-- INJECT_START: slide_27_img_03 -->
![Cloud DNS (slide_27_img_03)](media/slide_27_img_03.jpeg)

**Figure 85:** [Slide 27] Cloud DNS — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_03 -->


<!-- INJECT_START: slide_27_img_05 -->
![Cloud DNS (slide_27_img_05)](media/slide_27_img_05.jpeg)

**Figure 87:** [Slide 27] Cloud DNS — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_05 -->


<!-- INJECT_START: slide_27_img_01 -->
![Cloud DNS (slide_27_img_01)](media/slide_27_img_01.jpeg)

**Figure 83:** [Slide 27] Cloud DNS — Visual Illustration & Context Reference
<!-- INJECT_END: slide_27_img_01 -->

* But what about the Internet hostnames and addresses of applications built in Google
* Cloud?
* Google Cloud offers Cloud DNS to help the world find them. It's a managed DNS
* service that runs on the same infrastructure as Google. It has low latency and high
* availability, and it's a cost-effective way to make your applications and services
* available to your users. The DNS information you publish is served from redundant
* locations around the world.
* Cloud DNS is also programmable. You can publish and manage millions of DNS zones
* and records using the Google Cloud console, the command-line interface, or the API.

---

<a id="slide-28-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 28: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_28_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_28_img_02)](media/slide_28_img_02.jpeg)

**Figure 89:** [Slide 28] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_28_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_28_img_01)](media/slide_28_img_01.jpeg)

**Figure 88:** [Slide 28] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_28_img_01 -->


---

<a id="slide-29-edge-caching"></a>
### Slide 29: Edge caching


<!-- INJECT_START: slide_29_img_02 -->
![Edge caching (slide_29_img_02)](media/slide_29_img_02.jpeg)

**Figure 91:** [Slide 29] Edge caching — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_02 -->


<!-- INJECT_START: slide_29_img_01 -->
![Edge caching (slide_29_img_01)](media/slide_29_img_01.jpeg)

**Figure 90:** [Slide 29] Edge caching — Visual Illustration & Context Reference
<!-- INJECT_END: slide_29_img_01 -->

* Google has a global system of edge caches. Edge caching refers to the use of
* caching servers to store content closer to end users.

---

<a id="slide-30-cloud-cdn"></a>
### Slide 30: Cloud CDN

* Proprietary + Confidential

<!-- INJECT_START: slide_30_img_02 -->
![Cloud CDN (slide_30_img_02)](media/slide_30_img_02.jpeg)

**Figure 93:** [Slide 30] Cloud CDN — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_02 -->


<!-- INJECT_START: slide_30_img_03 -->
![Cloud CDN (slide_30_img_03)](media/slide_30_img_03.jpeg)

**Figure 94:** [Slide 30] Cloud CDN — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_03 -->

* Lower network latency

<!-- INJECT_START: slide_30_img_04 -->
![Cloud CDN (slide_30_img_04)](media/slide_30_img_04.jpeg)

**Figure 95:** [Slide 30] Cloud CDN — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_04 -->

* Origins of content will experience reduced load
* Save money
* Enabled with a single checkbox

<!-- INJECT_START: slide_30_img_01 -->
![Cloud CDN (slide_30_img_01)](media/slide_30_img_01.jpeg)

**Figure 92:** [Slide 30] Cloud CDN — Visual Illustration & Context Reference
<!-- INJECT_END: slide_30_img_01 -->

* You can use this system to accelerate content delivery in your application using Cloud
* **CDN:** content delivery network. This means your customers will experience lower
* network latency, the origins of your content will experience reduced load, and you can
* even save money. Once an Application Load Balancer is set up, Cloud CDN can be
* enabled with a single checkbox.
* There are many other CDNs available out there, of course. If you are already using
* one, chances are, it's a part of Google Cloud's CDN Interconnect partner program, and
* you can continue to use it.

---

<a id="slide-31-virtual-machines-and-networks-in-the-cloud"></a>
### Slide 31: Virtual Machines and Networks in the Cloud


<!-- INJECT_START: slide_31_img_02 -->
![Virtual Machines and Networks in the Cloud (slide_31_img_02)](media/slide_31_img_02.jpeg)

**Figure 97:** [Slide 31] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_02 -->

* 01
* 02
* Virtual private cloud networking
* Compute Engine
* 03
* 04
* Scaling virtual machines
* Important VPC compatibilities
* 05
* 06
* 07
* 08
* Cloud Load Balancing
* Cloud DNS
* Cloud CDN
* Connecting Networks to Google VPC

<!-- INJECT_START: slide_31_img_01 -->
![Virtual Machines and Networks in the Cloud (slide_31_img_01)](media/slide_31_img_01.jpeg)

**Figure 96:** [Slide 31] Virtual Machines and Networks in the Cloud — Visual Illustration & Context Reference
<!-- INJECT_END: slide_31_img_01 -->


---

<a id="slide-32-google-vpc-networks-can-connect-to-other-networks"></a>
### Slide 32: Google VPC networks can connect to other networks


<!-- INJECT_START: slide_32_img_02 -->
![Google VPC networks can connect to other networks (slide_32_img_02)](media/slide_32_img_02.jpeg)

**Figure 99:** [Slide 32] Google VPC networks can connect to other networks — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_02 -->

* Proprietary + Confidential

<!-- INJECT_START: slide_32_img_04 -->
![Google VPC networks can connect to other networks (slide_32_img_04)](media/slide_32_img_04.jpeg)

**Figure 100:** [Slide 32] Google VPC networks can connect to other networks — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_04 -->

* Cross-Cloud
* Interconnect

<!-- INJECT_START: slide_32_img_01 -->
![Google VPC networks can connect to other networks (slide_32_img_01)](media/slide_32_img_01.jpeg)

**Figure 98:** [Slide 32] Google VPC networks can connect to other networks — Visual Illustration & Context Reference
<!-- INJECT_END: slide_32_img_01 -->

* Many Google Cloud customers want to connect their Google Virtual Private Cloud
* networks to other networks in their system, such as on-premises networks or
* networks in other clouds. There are a number of effective ways to accomplish this.

---

<a id="slide-33-cloud-vpn-creates-dynamic-connections"></a>
### Slide 33: Cloud VPN creates dynamic connections

* Proprietary + Confidential

<!-- INJECT_START: slide_33_img_02 -->
![Cloud VPN creates dynamic connections (slide_33_img_02)](media/slide_33_img_02.jpeg)

**Figure 102:** [Slide 33] Cloud VPN creates dynamic connections — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_02 -->


<!-- INJECT_START: slide_33_img_03 -->
![Cloud VPN creates dynamic connections (slide_33_img_03)](media/slide_33_img_03.jpeg)

**Figure 103:** [Slide 33] Cloud VPN creates dynamic connections — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_03 -->

* Creates a VPN "tunnel" connection

<!-- INJECT_START: slide_33_img_04 -->
![Cloud VPN creates dynamic connections (slide_33_img_04)](media/slide_33_img_04.jpeg)

**Figure 104:** [Slide 33] Cloud VPN creates dynamic connections — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_04 -->

* Uses Cloud Router to make the connection
* dynamic
* Lets other networks and Google VPC exchange
* route information over the VPN using the Border
* Gateway Protocol
* Cloud VPN
* Not always the best option because of security
* concerns or bandwidth reliability

<!-- INJECT_START: slide_33_img_01 -->
![Cloud VPN creates dynamic connections (slide_33_img_01)](media/slide_33_img_01.jpeg)

**Figure 101:** [Slide 33] Cloud VPN creates dynamic connections — Visual Illustration & Context Reference
<!-- INJECT_END: slide_33_img_01 -->

* One option is to start with a Virtual Private Network connection over the Internet and
* use Cloud VPN to create a "tunnel" connection. To make the connection dynamic, a
* Google Cloud feature called Cloud Router can be used. Cloud Router lets other
* networks and Google VPC exchange route information over the VPN using the Border
* Gateway Protocol. Using this method, if you add a new subnet to your Google VPC,
* your on-premises network will automatically get routes to it.

---

<a id="slide-34-direct-peering-routes-traffic-through-a-google-pop"></a>
### Slide 34: Direct peering routes traffic through a Google PoP

* Proprietary + Confidential

<!-- INJECT_START: slide_34_img_03 -->
![Direct peering routes traffic through a Google PoP (slide_34_img_03)](media/slide_34_img_03.jpeg)

**Figure 107:** [Slide 34] Direct peering routes traffic through a Google PoP — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_03 -->


<!-- INJECT_START: slide_34_img_02 -->
![Direct peering routes traffic through a Google PoP (slide_34_img_02)](media/slide_34_img_02.jpeg)

**Figure 106:** [Slide 34] Direct peering routes traffic through a Google PoP — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_02 -->

* Puts a router in the same public datacenter as a
* Google point of presence (PoP)
* Uses a router to exchange traffic between
* networks
* Connects to more than 200 Google points of
* presence around the world
* Direct Peering

<!-- INJECT_START: slide_34_img_01 -->
![Direct peering routes traffic through a Google PoP (slide_34_img_01)](media/slide_34_img_01.jpeg)

**Figure 105:** [Slide 34] Direct peering routes traffic through a Google PoP — Visual Illustration & Context Reference
<!-- INJECT_END: slide_34_img_01 -->

* But using the Internet to connect networks isn't always the best option for everyone,
* either because of security concerns or because of bandwidth reliability.
* A second option is to consider "peering" with Google using Direct Peering. Peering
* means putting a router in the same public datacenter as a Google point of presence
* and using it to exchange traffic between networks. Google has more than 200 points
* of presence (PoPs) around the world.

---

<a id="slide-35-carrier-peering-allows-access-to-google-workspace"></a>
### Slide 35: Carrier peering allows access to Google Workspace

* Proprietary + Confidential

<!-- INJECT_START: slide_35_img_02 -->
![Carrier peering allows access to Google Workspace (slide_35_img_02)](media/slide_35_img_02.jpeg)

**Figure 109:** [Slide 35] Carrier peering allows access to Google Workspace — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_02 -->


<!-- INJECT_START: slide_35_img_03 -->
![Carrier peering allows access to Google Workspace (slide_35_img_03)](media/slide_35_img_03.jpeg)

**Figure 110:** [Slide 35] Carrier peering allows access to Google Workspace — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_03 -->

* Gives direct access from an on-premises
* network through a service provider's network
* Not covered by a Google Service Level
* Agreement
* Carrier Peering

<!-- INJECT_START: slide_35_img_01 -->
![Carrier peering allows access to Google Workspace (slide_35_img_01)](media/slide_35_img_01.jpeg)

**Figure 108:** [Slide 35] Carrier peering allows access to Google Workspace — Visual Illustration & Context Reference
<!-- INJECT_END: slide_35_img_01 -->

* Customers who aren't already in a point of presence can contract with a partner in the
* Carrier Peering program to get connected. Carrier peering gives you direct access from
* your on-premises network through a service provider's network to Google Workspace and
* to Google Cloud products that can be exposed through one or more public IP addresses.
* One downside of peering, though, is that it isn't covered by a Google Service Level
* Agreement.

---

<a id="slide-36-dedicated-interconnect-is-a-direct-connection-to-google"></a>
### Slide 36: Dedicated Interconnect is a direct connection to Google

* Proprietary + Confidential

<!-- INJECT_START: slide_36_img_02 -->
![Dedicated Interconnect is a direct connection to Google (slide_36_img_02)](media/slide_36_img_02.jpeg)

**Figure 112:** [Slide 36] Dedicated Interconnect is a direct connection to Google — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_02 -->

* Good solution for getting the highest uptimes for
* interconnection

<!-- INJECT_START: slide_36_img_03 -->
![Dedicated Interconnect is a direct connection to Google (slide_36_img_03)](media/slide_36_img_03.jpeg)

**Figure 113:** [Slide 36] Dedicated Interconnect is a direct connection to Google — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_03 -->

* Allows for one or more direct, private
* connections to Google
* Can be covered by up to a 99.99% SLA
* if connections have topologies that meet
* Google's specifications
* Dedicated
* Interconnect
* Connections can be backed up by a VPN for
* even greater reliability

<!-- INJECT_START: slide_36_img_01 -->
![Dedicated Interconnect is a direct connection to Google (slide_36_img_01)](media/slide_36_img_01.jpeg)

**Figure 111:** [Slide 36] Dedicated Interconnect is a direct connection to Google — Visual Illustration & Context Reference
<!-- INJECT_END: slide_36_img_01 -->

* If getting the highest uptimes for interconnection is important, then using Dedicated
* Interconnect would be a good solution. This option allows for one or more direct,
* private connections to Google. If these connections have topologies that meet
* Google's specifications, they can be covered by up to a 99.99% SLA. Also, these
* connections can be backed up by a VPN for even greater reliability.

---

<a id="slide-37-partner-interconnect-links-your-on-prem-with-your-vpc"></a>
### Slide 37: Partner Interconnect links your on-prem with your VPC

* Proprietary + Confidential

<!-- INJECT_START: slide_37_img_02 -->
![Partner Interconnect links your on-prem with your VPC (slide_37_img_02)](media/slide_37_img_02.jpeg)

**Figure 115:** [Slide 37] Partner Interconnect links your on-prem with your VPC — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_02 -->


<!-- INJECT_START: slide_37_img_03 -->
![Partner Interconnect links your on-prem with your VPC (slide_37_img_03)](media/slide_37_img_03.jpeg)

**Figure 116:** [Slide 37] Partner Interconnect links your on-prem with your VPC — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_03 -->

* Provides connectivity between an on-premises
* network and a VPC network through
* a supported service provider

<!-- INJECT_START: slide_37_img_04 -->
![Partner Interconnect links your on-prem with your VPC (slide_37_img_04)](media/slide_37_img_04.jpeg)

**Figure 117:** [Slide 37] Partner Interconnect links your on-prem with your VPC — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_04 -->

* Can be configured to support mission-critical
* services or applications that can tolerate some
* downtime
* Partner
* Interconnect
* Can be covered by up to a 99.99% SLA if
* connections have topologies that meet Google's
* specifications

<!-- INJECT_START: slide_37_img_01 -->
![Partner Interconnect links your on-prem with your VPC (slide_37_img_01)](media/slide_37_img_01.jpeg)

**Figure 114:** [Slide 37] Partner Interconnect links your on-prem with your VPC — Visual Illustration & Context Reference
<!-- INJECT_END: slide_37_img_01 -->

* Another option we'll explore is Partner Interconnect, which provides connectivity
* between an on-premises network and a VPC network through a supported service
* provider. A Partner Interconnect connection is useful if a data center is in a physical
* location that can't reach a Dedicated Interconnect colocation facility, or if the data
* needs doesn't warrant an entire 10 Gbps connection.
* Depending on availability needs, Partner Interconnect can be configured to support
* mission-critical services or applications that can tolerate some downtime. As with
* Dedicated Interconnect, if these connections have topologies that meet Google's
* specifications, they can be covered by up to a 99.99% SLA, but note that Google is not
* responsible for any aspects of Partner Interconnect provided by the third party service
* provider nor any issues outside of Google's network.

---

<a id="slide-38-cross-cloud-interconnect-connects-to-a-network-hosted-by-another-cloud-service-provider"></a>
### Slide 38: Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider

* Proprietary + Confidential
* Cross-Cloud Interconnect connects to a network hosted
* by another cloud service provider

<!-- INJECT_START: slide_38_img_03 -->
![Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider (slide_38_img_03)](media/slide_38_img_03.jpeg)

**Figure 119:** [Slide 38] Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_03 -->

* Establish high-bandwidth dedicated connectivity
* between Google Cloud and another cloud
* service provider
* Supports the adoption of an integrated
* multicloud strategy
* **Two connection sizes:** 10 Gbps or 100 Gbps
* Cross-Cloud
* Interconnect

<!-- INJECT_START: slide_38_img_01 -->
![Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider (slide_38_img_01)](media/slide_38_img_01.jpeg)

**Figure 118:** [Slide 38] Cross-Cloud Interconnect connects to a network hosted  by another cloud service provider — Visual Illustration & Context Reference
<!-- INJECT_END: slide_38_img_01 -->

* And the final option is Cross-Cloud Interconnect. Cross-Cloud Interconnect helps you
* establish high-bandwidth dedicated connectivity between Google Cloud and another
* cloud service provider. Google provisions a dedicated physical connection between
* the Google network and that of another cloud service provider. You can use this
* connection to peer your Google Virtual Private Cloud (VPC) network with your network
* that's hosted by a supported cloud service provider.
* Cross-Cloud Interconnect provides a number of benefits, for example:
* ●
* Supports your adoption of an integrated multicloud strategy.
* ●
* Provides reduced complexity
* ●
* Site-to-site data transfer
* ●
* Encryption
* ●
* Supports various cloud service providers
* Cross-Cloud Interconnect connections are available in two sizes: 10 Gbps or 100
* Gbps.

---

<a id="slide-39-networking-options-decision-tree"></a>
### Slide 39: Networking options decision tree

* Proprietary + Confidential
* Use Dedicated
* Use Cloud VPN
* Interconnect

<!-- INJECT_START: slide_39_img_02 -->
![Networking options decision tree (slide_39_img_02)](media/slide_39_img_02.jpeg)

**Figure 121:** [Slide 39] Networking options decision tree — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_02 -->

* Bandwidth and
* performance of
* current connection ok?
* Manage equipment in
* Use Partner
* Interconnect
* Google PoP?
* Need
* private-to-private
* address connectivity?
* 1
* 2
* 3

<!-- INJECT_START: slide_39_img_03 -->
![Networking options decision tree (slide_39_img_03)](media/slide_39_img_03.jpeg)

**Figure 122:** [Slide 39] Networking options decision tree — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_03 -->

* Bandwidth and
* performance of
* current connection ok?
* Manage equipment in
* Use Carrier Peering
* Google PoP?
* Use public IP address
* Use Direct Peering

<!-- INJECT_START: slide_39_img_01 -->
![Networking options decision tree (slide_39_img_01)](media/slide_39_img_01.jpeg)

**Figure 120:** [Slide 39] Networking options decision tree — Visual Illustration & Context Reference
<!-- INJECT_END: slide_39_img_01 -->

* Choosing a networking option depends on your applications and business
* requirements. You can assess those requirements by answering three simple
* **questions:**
* 1.
* Do any of your on-premises servers or user computers with private addressing
* need to connect to Google Cloud resources with private addressing?
* 2.
* Do the bandwidth and performance of your current connection to Google
* services currently meet your business requirements?
* 3.
* Do you already have, or are you willing to install and manage, access and
* routing equipment in one of Google's point of presence (POP) locations?
* ●
* If you need private-to-private connectivity and your internet connection meets
* your business requirements, then building a Cloud VPN is your best bet.
* ●
* If you don't need private access and your Internet connection is meeting your
* business requirements, then you can simply use public IP addresses to
* connect to Google services.
* ●
* If you don't need private address connectivity and your current connection to
* Google Cloud isn't performing well, then peering may be your best connectivity
* option. Direct Peering is a good option if you already have a footprint in one of
* Google's POPs, or you're willing to lease co-location space and install and
* support routing equipment.
* ●
* If installing equipment isn't an option or you would prefer to work with a
* service provider partner as an intermediary to peer with Google, then Carrier
* Peering is the way to go.

---

<a id="slide-40-slide-40"></a>
### Slide 40: Slide 40

  * ●
  * If you need private, high-performance connectivity to Google Cloud, but
  * installing equipment isn't an optionor you would prefer to work with a service
  * provider partner as an intermediary, then Partner Interconnect would be the
  * recommended option.
  * ●
  * Last but not least, there's Dedicated Interconnect, which provides you with a
  * private circuit direct to Google. This is a good option if you already have a
  * footprint (or are willing to lease co-lo space and install and support routing
  * equipment) in a Google POP.

---

<a id="slide-41-module-quiz"></a>
### Slide 41: Module Quiz


<!-- INJECT_START: slide_41_img_02 -->
![Module Quiz (slide_41_img_02)](media/slide_41_img_02.jpeg)

**Figure 124:** [Slide 41] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_41_img_02 -->


<!-- INJECT_START: slide_41_img_01 -->
![Module Quiz (slide_41_img_01)](media/slide_41_img_01.jpeg)

**Figure 123:** [Slide 41] Module Quiz — Visual Illustration & Context Reference
<!-- INJECT_END: slide_41_img_01 -->


---

<a id="slide-42-quiz-question-1"></a>
### Slide 42: Quiz | Question 1

* Proprietary + Confidential
* Question
* In Google Cloud VPCs, what scope do subnets have?
* A.
* Zonal
* B.
* Regional
* C.
* Global
* D.
* Multi-regional

<!-- INJECT_START: slide_42_img_01 -->
![Quiz | Question 1 (slide_42_img_01)](media/slide_42_img_01.jpeg)

**Figure 125:** [Slide 42] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_42_img_01 -->


---

<a id="slide-43-quiz-question-1"></a>
### Slide 43: Quiz | Question 1

* Proprietary + Confidential
* Answer
* In Google Cloud VPCs, what scope do subnets have?
* A.
* Zonal

<!-- INJECT_START: slide_43_img_02 -->
![Quiz | Question 1 (slide_43_img_02)](media/slide_43_img_02.jpeg)

**Figure 127:** [Slide 43] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_43_img_02 -->

* B.
* Regional
* C.
* Global
* D.
* Multi-regional

<!-- INJECT_START: slide_43_img_01 -->
![Quiz | Question 1 (slide_43_img_01)](media/slide_43_img_01.jpeg)

**Figure 126:** [Slide 43] Quiz | Question 1 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_43_img_01 -->

* In Google Cloud VPCs, what scope do subnets have?
* **A:** Zonal
* **Feedback:** Sorry, that's not correct. VPC subnets can span the zones that make up a
* region. This is beneficial because your solutions can incorporate fault tolerance
* without complicating your network topology.
* **B:** Regional
* **Feedback:** That's correct. VPC subnets can span the zones that make up a region.
* This is beneficial because your solutions can incorporate fault tolerance without
* complicating your network topology.
* **C:** Global
* **Feedback:** Sorry, that's not correct. VPC subnets can span the zones that make up a
* region. This is beneficial because your solutions can incorporate fault tolerance
* without complicating your network topology.
* **D:** Multi-regional
* **Feedback:** Sorry, that's not correct. VPC subnets can span the zones that make up a
* region. This is beneficial because your solutions can incorporate fault tolerance
* without complicating your network topology.

---

<a id="slide-44-quiz-question-2"></a>
### Slide 44: Quiz | Question 2

* Proprietary + Confidential
* Question
* What is the main reason customers choose Spot VMs?
* A.
* To improve performance
* B.
* To reduce cost
* C.
* To use custom machine types
* D.
* To reduce cost on premium operating systems

<!-- INJECT_START: slide_44_img_01 -->
![Quiz | Question 2 (slide_44_img_01)](media/slide_44_img_01.jpeg)

**Figure 128:** [Slide 44] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_44_img_01 -->


---

<a id="slide-45-quiz-question-2"></a>
### Slide 45: Quiz | Question 2

* Proprietary + Confidential
* Answer
* What is the main reason customers choose Spot VMs?
* A.
* To improve performance

<!-- INJECT_START: slide_45_img_02 -->
![Quiz | Question 2 (slide_45_img_02)](media/slide_45_img_02.jpeg)

**Figure 130:** [Slide 45] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_45_img_02 -->

* B.
* To reduce cost
* C.
* To use custom machine types
* D.
* To reduce cost on premium operating systems

<!-- INJECT_START: slide_45_img_01 -->
![Quiz | Question 2 (slide_45_img_01)](media/slide_45_img_01.jpeg)

**Figure 129:** [Slide 45] Quiz | Question 2 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_45_img_01 -->

* What is the main reason customers choose Spot VMs?
* **A:** To improve performance.
* **Feedback:** Sorry, that's not correct. Spot VMs have the same performance as
* ordinary VMs of the same machine type.
* **B:** To reduce cost.
* **Feedback:** That's correct! The per-hour price of Spot VMs incorporates a substantial
* discount.
* **C:** To use custom machine types
* **Feedback:** Sorry, that's not correct. Spot VMs and regular VMs can have custom
* configurations.
* **D:** To reduce cost on premium operating systems.
* **Feedback:** Sorry, that's not correct. Spot instances don't reduce the cost of premium
* operating systems and don't change the way that you're billed for the use of those
* operating systems. If Compute Engine stops a spot instance that runs a premium
* operating system, you are billed for that operating system as if you stopped the
* instance yourself.

---

<a id="slide-46-quiz-question-3"></a>
### Slide 46: Quiz | Question 3

* Proprietary + Confidential
* Question
* For which of these interconnect options is a Service Level Agreement available?
* A.
* Dedicated Interconnect
* B.
* Standard Network Tier
* C.
* Direct Peering
* D.
* Carrier Peering

<!-- INJECT_START: slide_46_img_01 -->
![Quiz | Question 3 (slide_46_img_01)](media/slide_46_img_01.jpeg)

**Figure 131:** [Slide 46] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_46_img_01 -->


---

<a id="slide-47-quiz-question-3"></a>
### Slide 47: Quiz | Question 3

* Proprietary + Confidential
* Answer
* For which of these interconnect options is a Service Level Agreement available?

<!-- INJECT_START: slide_47_img_02 -->
![Quiz | Question 3 (slide_47_img_02)](media/slide_47_img_02.jpeg)

**Figure 133:** [Slide 47] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_02 -->

* A.
* Dedicated Interconnect
* B.
* Standard Network Tier
* C.
* Direct Peering
* D.
* Carrier Peering

<!-- INJECT_START: slide_47_img_01 -->
![Quiz | Question 3 (slide_47_img_01)](media/slide_47_img_01.jpeg)

**Figure 132:** [Slide 47] Quiz | Question 3 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_47_img_01 -->

* For which of these interconnect options is a Service Level Agreement available?
* **A:** Dedicated Interconnect
* **Feedback:** Correct! Dedicated Interconnect is correct because Google provides an
* SLA for this managed service, guaranteeing performance.
* **B:** Standard Network Tier
* **Feedback:** Incorrect. Standard Network Tier is a pricing option, not an interconnect
* service, so no SLA applies directly to it. Review the lecture "Connecting networks to
* Google VPC."
* **C:** Direct Peering
* **Feedback:** Incorrect. Direct Peering is an unmanaged connection to Google's network,
* and as such, does not come with an SLA. Review the lecture "Connecting networks to
* Google VPC."
* **D:** Carrier Peering
* **Feedback:** Incorrect. Carrier Peering is an unmanaged connection to Google's
* network, and as such, does not come with an SLA. Review the lecture "Connecting
* networks to Google VPC."

---

<a id="slide-48-quiz-question-4"></a>
### Slide 48: Quiz | Question 4

* Proprietary + Confidential
* Question
* How does global Cloud Load Balancing allow you to balance HTTP-based traffic?
* A.
* Across multiple virtual machine instances in a single Compute Engine region.
* B.
* Across multiple Google Cloud services.
* C.
* Across multiple physical machines in a single data center.
* D.
* Across multiple Compute Engine regions.

<!-- INJECT_START: slide_48_img_01 -->
![Quiz | Question 4 (slide_48_img_01)](media/slide_48_img_01.jpeg)

**Figure 134:** [Slide 48] Quiz | Question 4 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_48_img_01 -->


---

<a id="slide-49-quiz-question-4"></a>
### Slide 49: Quiz | Question 4

* Proprietary + Confidential
* Answer
* How does global Cloud Load Balancing allow you to balance HTTP-based traffic?
* A.
* Across multiple virtual machine instances in a single Compute Engine region.
* B.
* Across multiple Google Cloud services.
* C.
* Across multiple physical machines in a single data center.

<!-- INJECT_START: slide_49_img_02 -->
![Quiz | Question 4 (slide_49_img_02)](media/slide_49_img_02.jpeg)

**Figure 136:** [Slide 49] Quiz | Question 4 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_49_img_02 -->

* D.
* Across multiple Compute Engine regions.

<!-- INJECT_START: slide_49_img_01 -->
![Quiz | Question 4 (slide_49_img_01)](media/slide_49_img_01.jpeg)

**Figure 135:** [Slide 49] Quiz | Question 4 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_49_img_01 -->

* For which of these interconnect options is a Service Level Agreement available?
* **A:** Across multiple virtual machine instances in a single Compute Engine region.
* **Feedback:** Incorrect. This answer is only partially correct, as load balancers also
* operate globally. Review the lecture "Cloud Load Balancing."
* **B:** Across multiple Google Cloud services.
* **Feedback:** Incorrect. This answer is too general. Load balancers are for specific
* backends, not all services. Review the lecture "Cloud Load Balancing."
* **C:** Across multiple physical machines in a single data center.
* **Feedback:** Sorry, that's not correct, as this is how on-premise load balancing works,
* not a managed cloud service. Review the lecture "Cloud Load Balancing."
* **D:** Across multiple Compute Engine regions.
* **Feedback:** Correct! With global Cloud Load Balancing, your application presents a
* single front-end to the world.

---

<a id="slide-50-quiz-question-5"></a>
### Slide 50: Quiz | Question 5

* Proprietary + Confidential
* Question
* Which of the following describes a Virtual Private Cloud (VPC)?
* A.
* A fully distributed, software-defined, managed service for traffic distribution.
* B.
* A service that routes traffic through a Google Point of Presence (PoP).
* C.
* A secure, individual, private cloud-computing network hosted within a public cloud.
* D.
* An option that allows one or more direct, private connections to Google.

<!-- INJECT_START: slide_50_img_01 -->
![Quiz | Question 5 (slide_50_img_01)](media/slide_50_img_01.jpeg)

**Figure 137:** [Slide 50] Quiz | Question 5 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_50_img_01 -->


---

<a id="slide-51-quiz-question-5"></a>
### Slide 51: Quiz | Question 5

* Proprietary + Confidential
* Answer
* Which of the following describes a Virtual Private Cloud (VPC)?
* A.
* A fully distributed, software-defined, managed service for traffic distribution.
* B.
* A service that routes traffic through a Google Point of Presence (PoP).

<!-- INJECT_START: slide_51_img_02 -->
![Quiz | Question 5 (slide_51_img_02)](media/slide_51_img_02.jpeg)

**Figure 139:** [Slide 51] Quiz | Question 5 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_51_img_02 -->

* C.
* A secure, individual, private cloud-computing network hosted within a public cloud.
* D.
* An option that allows one or more direct, private connections to Google.

<!-- INJECT_START: slide_51_img_01 -->
![Quiz | Question 5 (slide_51_img_01)](media/slide_51_img_01.jpeg)

**Figure 138:** [Slide 51] Quiz | Question 5 — Visual Illustration & Context Reference
<!-- INJECT_END: slide_51_img_01 -->

* Which of the following describes a Virtual Private Cloud (VPC)?
* **A:** A fully distributed, software-defined, managed service for traffic distribution.
* **Feedback:** Sorry, that's not correct. This describes a load balancer or a similar
* network service, not a VPC. Review the "Virtual Private Cloud" section of the slide
* deck.
* **B:** A service that routes traffic through a Google Point of Presence (PoP).
* **Feedback:** Sorry, that's not correct. This is a characteristic of some Google networking
* services, but not the primary definition of a VPC. Review the "Connecting Networks to
* Google VPC" section of the slide deck.
* **C:** A secure, individual, private cloud-computing network hosted within a public
* cloud.
* **Feedback:** Correct!
* **D:** An option that allows one or more direct, private connections to Google.
* **Feedback:** Sorry, that's not correct. This describes an interconnect option like
* Dedicated Interconnect, not a VPC. Review the "Connecting Networks to Google
* VPC" section of the slide deck.

---

<a id="slide-52-lab-intro"></a>
### Slide 52: Lab Intro

* Proprietary + Confidential

<!-- INJECT_START: slide_52_img_02 -->
![Lab Intro (slide_52_img_02)](media/slide_52_img_02.jpeg)

**Figure 141:** [Slide 52] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_52_img_02 -->

* Get Started with Virtual Private Cloud
* Networking and Compute Engine
* In this lab, you create an auto mode VPC
* network with firewall rules and two VM
* instances. Then, you explore the connectivity
* for the VM instances.

<!-- INJECT_START: slide_52_img_01 -->
![Lab Intro (slide_52_img_01)](media/slide_52_img_01.jpeg)

**Figure 140:** [Slide 52] Lab Intro — Visual Illustration & Context Reference
<!-- INJECT_END: slide_52_img_01 -->


---
