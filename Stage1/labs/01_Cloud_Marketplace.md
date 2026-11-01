# Lab 1: Google Cloud Fundamentals: Getting Started with Cloud Marketplace

> **Progression Rank:** 1 of 4 (Starter / Easy)
> **Estimated Time:** 30 Minutes · **Target Track:** Module 1 & 2: Introduction & Resource Management
> **Role Trajectory:** Google Cloud Associate Cloud Engineer (ACE)

---

## 📖 Lab Instructions & Walkthrough


## Overview

In this lab, you use Google Cloud Marketplace to quickly and easily deploy a LAMP stack on a Compute Engine instance. The Google Click to Deploy LAMP Stack provides a complete web development environment for Linux that can be launched in one click.

| Component | Role |
| --- | --- |
| Linux | Operating system |
| Apache HTTP Server | Web server |
| MySQL | Relational database |
| PHP | Web application framework |
| phpMyAdmin | PHP administration tool |

## Objectives

In this lab, you learn how to launch a solution using Cloud Marketplace.

## Task 1. Sign in to the Google Cloud console

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

## Task 2. Use Cloud Marketplace to deploy a LAMP stack

1. In the Google Cloud console, in theNavigation menu(), clickMarketplace.
2. In the search bar, typeLAMPand then pressENTER.
3. In the search results, clickLAMP Stack, byGoogle Click to Deploy.If you choose another LAMP stack, the lab instructions may not work as expected.
4. On the LAMP page, clickGET STARTED.
5. On the Agreements page, check the box forTerms and agreements, and clickAGREE.
6. On theSuccessfully agreed to termspop up, clickDEPLOY.If prompted, click on Enable for the Compute Engine API and the Infrastructure Manager API.
7. ForZone, select the deployment zone to.
8. ForMachine Type, selectE2as theSeriesande2-mediumas theMachine Type.
9. Leave the remaining settings as their defaults.
10. ClickDeploy.

> ℹ️ **Note:**
> Note:Warnings may appear as the deployment is happening. You can disregard these for this lab.

The status of the deployment appears in the console window:lamp-1 is being deployed. When the deployment of the infrastructure is complete, the status changes tolamp-1 has been deployed.

After the software is installed, a summary of the details for the instance, including the site address, is displayed.

ClickCheck my progressto verify the objective.Use Cloud Marketplace to deploy a LAMP stack

## Task 3. Verify your deployment

1. When the deployment is complete, clicklamp-1-vm > Details.
2. Click theSite Urllink. (If the website is not responding, wait 30 seconds and try again.)  If you see a redirection notice, click on that link to view your new site. A new browser tab displays a congratulations message. This page confirms that, as part of the LAMP stack, the Apache HTTP Server is running.

> ℹ️ **Note:**
> Note:If you can't see the web page in the browser on your corporate laptop:
If possible, exit any corporate VPN/network and try again.
Enter the IP address on another device, such as a tablet or even a phone.

## Congratulations!

In this lab, you deployed a LAMP stack to a Compute Engine instance.

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

### More resources

Read theGoogle Cloud documentation on Cloud Marketplace.


---

## 🎓 Associate Cloud Engineer (ACE) Exam Anchors
| Core Exam Domain | Practical Architectural Takeaway |
| :--- | :--- |
| **Key Takeaway** | Compute Engine instance creation via pre-configured Marketplace solutions (LAMP stack) |
| **Key Takeaway** | Default vs custom network interfaces and external IP assignment |
| **Key Takeaway** | Firewall rule verification (allow-http, port 80) |
| **Shared responsibility model** | OS/software maintenance on Marketplace VM deployments |

## ✅ Objective Verification Checklist
- [ ] Lab sandbox environment provisioned and active.
- [ ] Task 1 completed and verified.
- [ ] Task 2 completed and verified.
- [ ] Task 3 completed and verified.
- [ ] All Qwiklabs progress checkmarks scored 100%.
- [ ] Lab ended cleanly to avoid quota leakage.