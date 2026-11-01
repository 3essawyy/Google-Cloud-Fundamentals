# Lab 3: Google Cloud Fundamentals: Getting Started with Cloud Storage and Cloud SQL

> **Progression Rank:** 3 of 4 (Medium)
> **Estimated Time:** 45 Minutes · **Target Track:** Module 4: Storage in the Cloud
> **Role Trajectory:** Google Cloud Associate Cloud Engineer (ACE)

---

## ⚡ Cloud Shell Quick-Reference Script
*Consolidated CLI commands ready for pasting into Google Cloud Shell:*

```bash
#!/usr/bin/env bash
# Lab 3: Google Cloud Fundamentals: Getting Started with Cloud Storage and Cloud SQL - Quick Execution Script
set -euo pipefail

# Step Command block 1
#!/bin/bash
apt-get install apache2 php php-mysql -y
service apache2 restart

# Step Command block 2
export LOCATION=US

# Step Command block 3
export LOCATION=EU

# Step Command block 4
export LOCATION=ASIA

# Step Command block 5
gcloud storage buckets create -l $LOCATION gs://$DEVSHELL_PROJECT_ID

# Step Command block 6
gcloud storage cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png

# Step Command block 7
gcloud storage cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png

# Step Command block 8
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png

# Step Command block 9
35.192.208.2/32

# Step Command block 10
cd /var/www/html

# Step Command block 11
sudo nano index.php

# Step Command block 12
<html>
<head><title>Welcome to my excellent blog</title></head>
<body>
<h1>Welcome to my excellent blog</h1>
<?php
 $dbserver = "CLOUDSQLIP";
$dbuser = "blogdbuser";
$dbpassword = "DBPASSWORD";
// In a production blog, we would not store the MySQL
// password in the document root. Instead, we would store
//  it in a Secret Manger. For more information see 
// https://cloud.google.com/sql/docs/postgres/use-secret-manager

 try {
  $conn = new PDO("mysql:host=$dbserver;dbname=mysql", $dbuser, $dbpassword);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully";
} catch(PDOException $e) {
  echo "Database connection failed:: " . $e->getMessage();
}

?>
</body></html>

# Step Command block 13
sudo service apache2 restart

# Step Command block 14
35.192.208.2/index.php

# Step Command block 15
Database connection failed: ...

# Step Command block 16
sudo nano index.php

# Step Command block 17
sudo service apache2 restart

# Step Command block 18
Connected successfully

# Step Command block 19
cd /var/www/html

# Step Command block 20
sudo nano index.php

# Step Command block 21
<img src='

# Step Command block 22
'>

# Step Command block 23
<img src='https://storage.googleapis.com/qwiklabs-gcp-0005e186fa559a09/my-excellent-blog.png'>

# Step Command block 24
sudo service apache2 restart

```

---

## 📖 Lab Instructions & Walkthrough


## Overview

In this lab, you create a Cloud Storage bucket and place an image in it. You also configure an application running in Compute Engine to use a database managed by Cloud SQL. For this lab, you configure a web server with PHP, a web development environment that is the basis for popular blogging software. Outside this lab, you will use analogous techniques to configure these packages.

You also configure the web server to reference the image in the Cloud Storage bucket.

## Objectives

In this lab, you learn how to perform the following tasks:

* Create a Cloud Storage bucket and place an image into it.
* Create a Cloud SQL instance and configure it.
* Connect to the Cloud SQL instance from a web server.
* Use the image in the Cloud Storage bucket on a web page.

## Task 1. Sign in to the Google Cloud Console

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

## Task 2. Deploy a web server VM instance

In this task you provision a virtual machine (VM) instance using Compute Engine, configure it with a web server (Apache) and necessary scripting for initial setup using a startup script. Next, you note its network identifiers.

1. In the Google Cloud console, on theNavigation menu(), clickCompute Engine>VM instances.
2. ClickCreate instance.
3. ForName, typebloghost
4. ForRegionselect.
5. ForZone, select.
6. ForMachine type, selecte2-standard-2.
7. In the left pane clickOS and storage, if theImageshown is notDebian GNU/Linux 12 (bookworm), clickChangeand select version toDebian GNU/Linux 12 (bookworm).
8. ClickNetworking.
9. InFirewall, clickAllow HTTP traffic.
10. In the left pane, clickAdvanced.
11. InAutomation, copy and paste the following script as the value forStartup script:

```bash
#!/bin/bash
apt-get install apache2 php php-mysql -y
service apache2 restart
```

> ℹ️ **Note:**
> Note:Be sure to supply that script as the value of theStartup scriptfield. If you accidentally put it into another field, it won't be executed when the VM instance starts.

1. Leave the remaining settings as their defaults, and clickCreate.

> ℹ️ **Note:**
> Note:Instance can take about two minutes to launch and be fully available for use.

1. On theVM instancespage, copy thebloghostVM instance's internal and external IP addresses to a text editor for use later in this lab.

ClickCheck my progressto verify the objective.Deploy a web server VM instance

## Task 3. Create a Cloud Storage bucket using the gcloud storage command line

In this task you use the gcloud storage command-line tool to create a globally unique Cloud Storage bucket, set its location, upload a public image to it, and make that specific object publicly readable.

All Cloud Storage bucket names must be globally unique. To ensure that your bucket name is unique, these instructions will guide you to give your bucket the same name as your Google Cloud project ID, which is also globally unique.

Cloud Storage buckets can be associated with either a region or a multi-region location:US,EU, orASIA. In this activity, you associate your bucket with the multi-region closest to the region and zone that the lab or your instructor assigned you to.

1. On theGoogle Cloud console, on the top right toolbar, click theActivate Cloud Shell. If a dialog box appears, clickContinue.
2. For convenience, enter your chosen location into an environment variable called LOCATION. Enter one of these commands:

```bash
export LOCATION=US
```

Or

```bash
export LOCATION=EU
```

Or

```bash
export LOCATION=ASIA
```

1. In Cloud Shell, the DEVSHELL_PROJECT_ID environment variable contains your project ID. Enter this command to make a bucket named after your project ID:

```bash
gcloud storage buckets create -l $LOCATION gs://$DEVSHELL_PROJECT_ID
```

If prompted, clickAuthorizeto continue.

1. Retrieve a banner image from a publicly accessible Cloud Storage location:

```bash
gcloud storage cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png
```

1. Copy the banner image to your newly created Cloud Storage bucket:

```bash
gcloud storage cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```

1. Modify the Access Control List of the object you just created so that it's readable by everyone:

```bash
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```

ClickCheck my progressto verify the objective.Create a Cloud Storage bucket using the gcloud storage command line

## Task 4. Create the Cloud SQL instance

In this task you create and configure a managed MySQL database instance using Cloud SQL, set up a specific user account, and crucially, authorize the external IP address of your future web server for network connectivity.

1. In the Google Cloud console, on theNavigation menu(), clickCloud SQL.
2. Scroll to the bottom of the page, then clickCreate instance.
3. ForChoose a database engine, selectChoose MySQL.
4. ForChoose a Cloud SQL edition, clickEnterprise, and forEdition presetselectSandboxfrom the dropdown.
5. ForInstance ID,typeblog-db, and forPasswordtypePassw0rd1!
6. ForRegion, select.
7. ForZonal availability, selectSingle zone.
8. ExpandSpecify zones, and inPrimary zone, select.

> ℹ️ **Note:**
> Note:This is the same region and zone into which you launched thebloghostinstance. The best performance is achieved by placing the client and the database close to each other.

1. In Customize your instance, expandShow configuration options.
2. ExpandSecurity, and then clickAllow unencrypted network traffic (not recommended).

> ℹ️ **Note:**
> Note:This lab does not use SSL, so ensure you set the above option.

1. ClickCreate instance.

> ℹ️ **Note:**
> Note:Wait for the instance to finish deploying. It will take a few minutes.

### Configure User and Connections

1. From the SQL instances details page, underConnect to this instance,  copy thePublic IP addressfor your SQL instance to a text editor for use later in this lab.
2. In the left pane, clickUsers, and then clickAdd user account.
3. ForUser name, typeblogdbuser
4. ForPassword, typePassw0rd1!
5. ClickAddto add the user account in the database.

> ℹ️ **Note:**
> Note:Wait for the user to be created.

1. In the left pane, clickConnections, and then clickNetworkingtab.
2. ClickAdd a network.

> ℹ️ **Note:**
> Note:If you're offered the choice between aPrivate IPconnection and aPublic IPconnection, choosePublic IPfor purposes of this lab.

> ℹ️ **Note:**
> Note:TheAdd a networkbutton may be unavailable if the user account creation is not yet complete.

1. ForName, typeweb front end
2. ForNetwork, type the external IP address of yourbloghostVM instance, followed by/32

The result will look like this:

```bash
35.192.208.2/32
```

> ℹ️ **Note:**
> Note:Be sure to use the external IP address of your VM instance followed by /32. Do not use the VM instance's internal IP address. Do not use the sample IP address shown here.

1. ClickDoneto finish defining the authorized network.
2. ClickSaveto save the configuration change.

> ℹ️ **Note:**
> Note: If the message appears likeAnother operation is in progress, wait for few minutes until you see the green check forblog-dbto save the configuration.

ClickCheck my progressto verify the objective.Create the Cloud SQL instance

## Task 5. Configure an application in a Compute Engine instance to use Cloud SQL

In this task you securely connect the Apache web server running on your VM instance to the Cloud SQL database by modifying the PHP application code (index.php) to include the database's IP address and credentials, thereby establishing a successful database connection.

1. On theNavigation menu(), clickCompute Engine>VM instances.
2. In the VM instances list, clickSSHin the row for your VM instancebloghost. If prompted, clickAuthorize.
3. In your ssh session onbloghost, change your working directory to the document root of the web server:

```bash
cd /var/www/html
```

1. Use thenanotext editor to edit a file calledindex.php:

```bash
sudo nano index.php
```

1. Copy and paste the content below into the file:

```bash
<html>
<head><title>Welcome to my excellent blog</title></head>
<body>
<h1>Welcome to my excellent blog</h1>
<?php
 $dbserver = "CLOUDSQLIP";
$dbuser = "blogdbuser";
$dbpassword = "DBPASSWORD";
// In a production blog, we would not store the MySQL
// password in the document root. Instead, we would store
//  it in a Secret Manger. For more information see 
// https://cloud.google.com/sql/docs/postgres/use-secret-manager

 try {
  $conn = new PDO("mysql:host=$dbserver;dbname=mysql", $dbuser, $dbpassword);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully";
} catch(PDOException $e) {
  echo "Database connection failed:: " . $e->getMessage();
}

?>
</body></html>
```

> ℹ️ **Note:**
> Note:In a later step, you will insert your Cloud SQL instance's IP address and your database password into this file. For now, leave the file unmodified.

1. PressCtrl+O, and then pressEnterto save your edited file.
2. PressCtrl+Xto exit the nano text editor.
3. Restart the web server:

```bash
sudo service apache2 restart
```

1. Open a new web browser tab and paste into the address bar yourbloghostVM instance's external IP address followed by/index.php. The URL will look like this:

```bash
35.192.208.2/index.php
```

> ℹ️ **Note:**
> Note:Be sure to use the external IP address of your VM instance followed by /index.php. Do not use the VM instance's internal IP address. Do not use the sample IP address shown here.

If you see the message that the IP address doesn't support a secure connection, clickContinue to site.

When you load the page, you will see that its content includes an error message beginning with the words:

```bash
Database connection failed: ...
```

> ℹ️ **Note:**
> Note:This message occurs because you have not yet configured PHP's connection to your Cloud SQL instance.

1. Return to your ssh session onbloghost. Use thenanotext editor to editindex.phpagain. Ensure that you are in the /var/www/html directory.

```bash
sudo nano index.php
```

1. In thenanotext editor, replaceCLOUDSQLIPwith the Cloud SQL instance (blog-db) Public IP address that you noted above. Leave the quotation marks around the value in place.
2. In thenanotext editor, replaceDBPASSWORDwith the Cloud SQL database password that you defined above, which isPassw0rd1!Leave the quotation marks around the value in place.
3. PressCtrl+O, and then pressEnterto save your edited file.
4. PressCtrl+Xto exit the nano text editor.
5. Restart the web server:

```bash
sudo service apache2 restart
```

1. Return to the web browser tab in which you opened yourbloghostVM instance's external IP address. When you load the page, the following message appears:

```bash
Connected successfully
```

> ℹ️ **Note:**
> Note:In an actual blog, the database connection status would not be visible to blog visitors. Instead, the database connection would be managed solely by the administrator.

## Task 6. Configure an application in a Compute Engine instance to use a Cloud Storage object

In this task you integrate the publicly accessible image stored in your Cloud Storage bucket into your web application by editing the index.php file on the Compute Engine instance to include the correct image source URL.

1. In the Google Cloud console, on theNavigation menu(), clickCloud Storage>Buckets.
2. Click the bucket that is named after your Google Cloud project.
3. In this bucket, there is an object calledmy-excellent-blog.png. Copy the URL behind the link icon that appears in that object'sPublic accesscolumn, or behind the words "Public link" if shown.

> ℹ️ **Note:**
> Note:If you see neither a link icon nor a "Public link", try refreshing the browser. If you still do not see a link icon, return to Cloud Shell and confirm that your attempt to change the object's Access Control list with thegsutil acl chcommand was successful.

1. Return to your ssh session on yourbloghostVM instance.
2. Enter this command to set your working directory to the document root of the web server:

```bash
cd /var/www/html
```

1. Use thenanotext editor to editindex.php:

```bash
sudo nano index.php
```

1. Use the arrow keys to move the cursor to the line that contains theh1element. PressEnterto open up a new, blank screen line, and then paste the URL you copied earlier into the line.
2. Paste this HTML markup immediately before the URL:

```bash
<img src='
```

1. Place a closing single quotation mark and a closing angle bracket at the end of the URL:

```bash
'>
```

The resulting line will look like this:

```bash
<img src='https://storage.googleapis.com/qwiklabs-gcp-0005e186fa559a09/my-excellent-blog.png'>
```

The effect of these steps is to place the line containing<img src='...'>immediately before the line containing<h1>...</h1>

> ℹ️ **Note:**
> Note:Do not copy the URL shown here. Instead, copy the URL shown by the Storage browser in your own Cloud Platform project.

1. PressCtrl+O, and then pressEnterto save your edited file.
2. PressCtrl+Xto exit the nano text editor.
3. Restart the web server:

```bash
sudo service apache2 restart
```

1. Return to the web browser tab in which you opened yourbloghostVM instance's external IP address. When you load the page, its content now includes a banner image.

## Congratulations!

In this lab, you configured a Cloud SQL instance and connected an application in a Compute Engine instance to it. You also worked with a Cloud Storage bucket.

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

## More resources

Read theGoogle Cloud Platform documentation on Cloud SQL.

Read theGoogle Cloud Platform documentation on Cloud Storage.



---

## 📝 Lab Run Notes: how Lab 3 went

Done on Mon 19 Oct 2026 after four grill rounds on the M4 notes. The run was **smooth**, with no errors and no steps that differed from the video.

> 💡 **Exam takeaway:** the lab's shortcuts (an `allUsers` ACL for the image, a public Cloud SQL IP with the VM's external IP as a `/32`, the password written in `index.php`) work for a demo. The production versions are IAM or a signed URL, a private IP, and Secret Manager. See Part 5 of the Lab 3 study notes.

---

## 🎓 Associate Cloud Engineer (ACE) Exam Anchors
| Core Exam Domain | Practical Architectural Takeaway |
| :--- | :--- |
| **Cloud Storage** | Globally unique bucket names, multi-regional vs regional storage classes |
| **Key Takeaway** | Cloud Storage CLI (`gcloud storage` vs legacy `gsutil`) and ACLs / public access prevention |
| **Cloud SQL** | Managed relational DB (MySQL), instance provisioning, public vs private IP |
| **Application integration** | Startup scripts, environment variables, and secure DB credentials |

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