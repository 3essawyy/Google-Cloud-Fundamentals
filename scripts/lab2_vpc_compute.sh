#!/usr/bin/env bash
# Lab 2: Get Started with Virtual Private Cloud Networking and Compute Engine
# Shell script reference for Google Cloud Shell
set -euo pipefail

echo "==> [Task 1 & 2] Custom VPC & Subnets should be verified or configured in Console or CLI"
echo "To create auto-mode VPC network via CLI:"
# gcloud compute networks create mynetwork --subnet-mode=auto

echo "To create firewall rules for ICMP, SSH, and RDP:"
# gcloud compute firewall-rules create mynetwork-allow-icmp-ssh-rdp \
#     --network=mynetwork \
#     --allow=icmp,tcp:22,tcp:3389

echo "To create VM instances in different zones:"
# gcloud compute instances create mynet-us-vm --zone=us-central1-c --machine-type=e2-micro --network=mynetwork
# gcloud compute instances create mynet-eu-vm --zone=europe-west1-d --machine-type=e2-micro --network=mynetwork

echo "==> [Task 3] Connectivity Test commands (run from inside mynet-us-vm SSH):"
echo "ping -c 3 <mynet-eu-vm-internal-ip>"
echo "ping -c 3 <mynet-eu-vm-external-ip>"
