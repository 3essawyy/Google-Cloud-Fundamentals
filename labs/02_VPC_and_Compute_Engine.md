# Lab 2: Get Started with Virtual Private Cloud Networking and Compute Engine

> **Progression Rank:** 2 of 4 (Easy / Medium)
> **Estimated Time:** 40 Minutes · **Target Track:** Module 3: Virtual Machines and Networks in the Cloud
> **Role Trajectory:** Google Cloud Associate Cloud Engineer (ACE)

---

## ⚡ Cloud Shell Quick-Reference Script
*Consolidated CLI commands ready for pasting into Google Cloud Shell:*

```bash
#!/usr/bin/env bash
# Lab 2: Get Started with Virtual Private Cloud Networking and Compute Engine - Quick Execution Script
set -euo pipefail

# Step Command block 1
ping -c 3 <Enter mynet-r2-vm's internal IP here>

# Step Command block 2
ping -c 3 <Enter mynet-r2-vm's external IP here>

# Step Command block 3
ping -c 3 <Enter mynet-r2-vm's internal IP here>

# Step Command block 4
ping -c 3 <Enter mynet-r2-vm's external IP here>

# Step Command block 5
ping -c 3 <Enter mynet-r2-vm's internal IP here>

# Step Command block 6
exit

```

---

## 📖 Lab Instructions & Walkthrough


## Overview

Google Cloud Virtual Private Cloud (VPC) provides networking functionality to Compute Engine virtual machine (VM) instances, Kubernetes Engine containers, and App Engine flexible environment. In other words, without a VPC network you cannot create VM instances, containers, or App Engine applications. Therefore, each Google Cloud project has adefaultnetwork to get you started.

You can think of a VPC network as similar to a physical network, except that it is virtualized within Google Cloud. A VPC network is a global resource that consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network (WAN). VPC networks are logically isolated from each other in Google Cloud.

In this lab, you create an auto mode VPC network with firewall rules and two VM instances. Then, you explore the connectivity for the VM instances.

### Objectives

In this lab, you  learn how to perform the following tasks:

* Explore the default VPC network
* Create an auto mode network with firewall rules
* Create VM instances using Compute Engine
* Explore the connectivity for VM instances

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

## Task 1. Explore the default network

Each Google Cloud project has adefaultnetwork with subnets, routes, and firewall rules.

### View the subnets

Thedefaultnetwork has a subnet ineach Google Cloud region.

1. In the Cloud console, in theNavigation menu(), clickVPC network>VPC networks.
2. Clickdefault.
3. ClickSubnets.

Notice thedefaultnetwork with its subnets.Each subnet is associated with a Google Cloud region and a private RFC 1918 CIDR block for its internalIP addresses rangeand agateway.

### View the routes

Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside  Google Cloud. Each VPC network comes with some default routes to route traffic among its subnets and send traffic from eligible instances to the internet.

1. In the left pane, clickRoutes.
2. InEffective RoutesclickNetwork, and then selectdefault.
3. ClickRegionand select the Lab Region assigned to you by Google Skills.
4. ClickView.Notice that there is a route for each subnet.These routes are managed for you, but you can create custom static routes to direct some packets to specific destinations. For example, you can create a route that sends all outbound traffic to an instance configured as a NAT gateway.

### View the Firewall rules

Each VPC network implements a distributed virtual firewall that you can configure. Firewall rules allow you to control which packets are allowed to travel to which destinations. Every VPC network has two implied firewall rules that block all incoming connections and allow all outgoing connections.

* In the left pane, clickFirewall.Notice that there are 4Ingressfirewall rules for thedefaultnetwork:default-allow-icmpdefault-allow-rdpdefault-allow-sshdefault-allow-internal

> ℹ️ **Note:**
> Note:These firewall rules allowICMP,RDP, andSSHingress traffic from anywhere (0.0.0.0/0) and allTCP,UDP, andICMPtraffic within the network (10.128.0.0/9). TheTargets,Filters,Protocols/ports, andActioncolumns explain these rules.

### Delete the Firewall rules

1. Select all of the default network firewall rules.
2. ClickDelete.
3. ClickDeleteto confirm the deletion of the firewall rules.

### Delete the default network

1. In the Cloud console, in theNavigation menu(), clickVPC network>VPC networks.
2. Select thedefaultnetwork.
3. ClickDelete VPC network.
4. ClickDeleteto confirm the deletion of thedefaultnetwork.Wait for the network to be deleted before continuing.
5. In the left pane, clickRoutes.Notice that there are no routes.
6. In the left pane, clickFirewall.Notice that there are no firewall rules.

> ⚠️ **Warning:**
> Note:Without a VPC network, there are no routes and no firewall rules!

### Try to create a VM instance

Verify that you cannot create a VM instance without a VPC network.

1. In theNavigation menu(), clickCompute Engine>VM instances.
2. ClickCreate instance.
3. Accept the default values and clickCreate.
An error is shown on theNetworkingtab.
4. ClickGo to Issues.
5. InNetwork Interfaces, notice the no more networks and no network available errors.
6. ClickCancel.

> ⚠️ **Warning:**
> Note:As expected, you cannot create a VM instance without a VPC network!

## Task 2. Create a VPC network and VM instances

Create a VPC network so that you can create VM instances.

### Create an auto mode VPC network with Firewall rules

Replicate thedefaultnetwork by creating an auto mode network.

1. In theNavigation menu(), clickVPC network>VPC networks.
2. ClickCreate VPC network.
3. ForName, typemynetwork.
4. ForSubnet creation mode, clickAutomatic.
Auto mode networks create subnets in each region automatically.
5. ForFirewall rules, select all available rules.
These are the same standard firewall rules that the default network had.
Thedeny-all-ingressandallow-all-egressrules are also displayed, but you cannot check or uncheck them because they are implied. These two rules have a lowerPriority(higher integers indicate lower priorities) so that the allow ICMP, custom, RDP and SSH rules are considered first.
6. ClickCreate.
When the new network is ready, notice that a subnet was created for each region.
7. Explore the IP address range for the subnets inand.

> ℹ️ **Note:**
> Note:If you ever delete the default network, you can quickly re-create it by creating an auto mode network as you just did. After recreating the network, allow-internal changes to allow-custom firewall rule.

### Create a VM instance in

Create a VM instance in theregion. Selecting a region and zone determines the subnet and assigns the internal IP address from the subnet's IP address range.

1. In theNavigation menu(), clickCompute Engine>VM instances.
2. ClickCreate Instance.
3. Specify the following:PropertyValue (type value or select option as specified)Namemynet-us-vmRegionZone
4. ForSeries, selectE2.
5. ForMachine type, selecte2-micro (2 vCPU, 1 GB memory).
6. ClickCreate.

### Create a VM instance in

Create a VM instance in theregion.

1. ClickCreate Instance.
2. Specify the following, and leave the remaining settings as their defaults:PropertyValue (type value or select option as specified)Namemynet-r2-vmRegionZone
3. ForSeries, selectE2.
4. ForMachine type, selecte2-micro (2 vCPU, 1 GB memory).
5. ClickCreate.

> ℹ️ **Note:**
> Note:TheExternal IP addressesfor both VM instances are ephemeral. If an instance is stopped, any ephemeral external IP addresses assigned to the instance are released back into the general Compute Engine pool and become available for use by other projects.When a stopped instance is started again, a new ephemeral external IP address is assigned to the instance. Alternatively, you can reserve a static external IP address, which assigns the address to your project indefinitely until you explicitly release it.

ClickCheck my progressto verify the objective.Create a VPC network and VM instance

## Task 3. Explore the connectivity for VM instances

Explore the connectivity for the VM instances. Specifically, try to SSH to your VM instances using tcp:22, and ping both the internal and external IP addresses of your VM instances using ICMP. Then explore the effects of the firewall rules on connectivity by removing the firewall rules individually.

### Verify connectivity for the VM instances

The firewall rules that you created withmynetworkallow ingress SSH and ICMP traffic from withinmynetwork(internal IP) and outside that network (external IP).

1. In theNavigation menu(), clickCompute Engine>VM instances.Note the external and internal IP addresses formynet-r2-vm.
2. Formynet-us-vm, clickSSHto launch a terminal and connect.
3. If anAuthorizepopup appears, click onAuthorize

> ℹ️ **Note:**
> Note:You can SSH because of theallow-sshfirewall rule, which allows incoming traffic from anywhere (0.0.0.0/0) fortcp:22. The SSH connection works seamlessly because Compute Engine generates an SSH key for you and stores it in one of the following locations:By default, Compute Engine adds the generated key to project or instance metadata.If your account is configured to use OS Login, Compute Engine stores the generated key with your user account.Alternatively, you can control access to Linux instances by creating SSH keys and editing public SSH key metadata.

1. To test connectivity tomynet-r2-vm's internal IP, run the following command, replacingmynet-r2-vm's internal IP:

```bash
ping -c 3 <Enter mynet-r2-vm's internal IP here>
```

You can pingmynet-r2-vm's internal IP because of theallow-customfirewall rule.

1. To test connectivity tomynet-r2-vm's external IP, run the following command, replacingmynet-r2-vm's external IP:

```bash
ping -c 3 <Enter mynet-r2-vm's external IP here>
```

> ℹ️ **Note:**
> Note:You can SSH tomynet-us-vmand pingmynet-r2-vm's internal and external IP address as expected. Alternatively, you can SSH tomynet-r2-vmand pingmynet-us-vm's internal and external IP address, which also works.

### Remove the allow-icmp firewall rules

Remove theallow-icmpfirewall rule and try to ping the internal and external IP address ofmynet-r2-vm.

1. In theNavigation menu(), clickVPC network>Firewall.
2. Select themynetwork-allow-icmprule.
3. ClickDelete.
4. ClickDeleteto confirm the deletion.Wait for the firewall rule to be deleted.
5. Return to themynet-us-vmSSH terminal.
6. To test connectivity tomynet-r2-vm's internal IP, run the following command, replacingmynet-r2-vm's internal IP:

```bash
ping -c 3 <Enter mynet-r2-vm's internal IP here>
```

You can pingmynet-r2-vm's internal IP because of theallow-customfirewall rule.

1. To test connectivity tomynet-r2-vm's external IP, run the following command, replacingmynet-r2-vm's external IP:

```bash
ping -c 3 <Enter mynet-r2-vm's external IP here>
```

> ⚠️ **Warning:**
> Note:The100% packet lossindicates that you cannot pingmynet-r2-vm's external IP. This is expected because you deleted theallow-icmpfirewall rule!

### Remove the allow-custom firewall rules

Remove theallow-customfirewall rule and try to ping the internal IP address ofmynet-r2-vm.

1. In theNavigation menu(), clickVPC network>Firewall.
2. Select themynetwork-allow-customrule.
3. ClickDelete.
4. ClickDeleteto confirm the deletion.Wait for the firewall rule to be deleted.
5. Return to themynet-us-vmSSH terminal.
6. To test connectivity tomynet-r2-vm's internal IP, run the following command, replacingmynet-r2-vm's internal IP:

```bash
ping -c 3 <Enter mynet-r2-vm's internal IP here>
```

> ⚠️ **Warning:**
> Note:The100% packet lossindicates that you cannot pingmynet-r2-vm's internal IP. This is expected because you deleted theallow-customfirewall rule!

1. Close the SSH terminal:

```bash
exit
```

### Remove the allow-ssh firewall rules

Remove theallow-sshfirewall rule and try to SSH tomynet-us-vm.

1. In theNavigation menu(), clickVPC network>Firewall.
2. Select themynetwork-allow-sshrule.
3. ClickDelete.
4. ClickDeleteto confirm the deletion.
5. Wait for the firewall rule to be deleted.
6. In theNavigation menu, clickCompute Engine>VM instances.
7. Formynet-us-vm, clickSSHto launch a terminal and connect.

> ⚠️ **Warning:**
> Note:TheConnection failedmessage indicates that you cannot SSH tomynet-us-vmbecause you deleted theallow-sshfirewall rule!

## Task 4. Review

In this lab, you explored the default network along with its subnets, routes, and firewall rules. You deleted the default network and determined that you cannot create any VM instances without a VPC network.

Thus, you created a new auto mode VPC network with subnets, routes, firewall rules, and two VM instances. Then you tested the connectivity for the VM instances and explored the effects of the firewall rules on connectivity.

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

Copyright 2026 Google LLC All rights reserved. Google and the Google logo are trademarks of Google LLC. All other company and product names may be trademarks of the respective companies with which they are associated.


---

## 🎓 Associate Cloud Engineer (ACE) Exam Anchors
| Core Exam Domain | Practical Architectural Takeaway |
| :--- | :--- |
| **VPC architecture** | Global VPCs, regional subnets, and non-overlapping CIDR ranges |
| **Firewall rules** | Targets (network tags), source IP ranges, protocols, and ports |
| **Key Takeaway** | Compute Engine VMs across different zones in the same region vs different regions |
| **Key Takeaway** | Internal DNS and private IP reachability vs external IP reachability via SSH and ICMP |

## ✅ Objective Verification Checklist
- [ ] Lab sandbox environment provisioned and active.
- [ ] Task 1 completed and verified.
- [ ] Task 2 completed and verified.
- [ ] Task 3 completed and verified.
- [ ] Task 4 completed and verified.
- [ ] All Qwiklabs progress checkmarks scored 100%.
- [ ] Lab ended cleanly to avoid quota leakage.