#!/usr/bin/env bash
# Lab 3: Getting Started with Cloud Storage and Cloud SQL
# Shell script reference for Google Cloud Shell
set -euo pipefail

# 1. Variables
export PROJECT_ID=$(gcloud config get-value project)
export BUCKET_NAME="${PROJECT_ID}-bucket"
export LOCATION="US"

echo "==> Project: ${PROJECT_ID}"
echo "==> Bucket Name: ${BUCKET_NAME}"

# 2. Create Cloud Storage Bucket using modern gcloud storage CLI
echo "==> Creating Cloud Storage Bucket..."
gcloud storage buckets create gs://${BUCKET_NAME} --location=${LOCATION}

# 3. Download sample asset and upload to bucket
echo "==> Uploading sample image..."
curl -s -O https://storage.googleapis.com/cloud-training/gcpfci/my-excellent-blog.png || true
if [ -f my-excellent-blog.png ]; then
    gcloud storage cp my-excellent-blog.png gs://${BUCKET_NAME}/my-excellent-blog.png
    gcloud storage objects update gs://${BUCKET_NAME}/my-excellent-blog.png --add-acl-grant=entity=AllUsers,role=READER || true
fi

echo "==> Bucket created and object configured. Proceed with Cloud SQL deployment in Console/CLI."
