#!/usr/bin/env bash
# Lab 4: Hello Cloud Run
# Shell script reference for Google Cloud Shell
set -euo pipefail

# 1. Variables
export PROJECT_ID=$(gcloud config get-value project)
export REGION="us-central1"
export REPO_NAME="my-repository"
export IMAGE_NAME="helloworld"
export SERVICE_NAME="helloworld"

echo "==> Configuring Project: ${PROJECT_ID} in Region: ${REGION}"
gcloud config set compute/region ${REGION}

# 2. Enable APIs
echo "==> Enabling Cloud Run and Artifact Registry APIs..."
gcloud services enable run.googleapis.com artifactregistry.googleapis.com

# 3. Create Artifact Registry Docker Repository
echo "==> Creating Artifact Registry repository: ${REPO_NAME}..."
gcloud artifacts repositories create ${REPO_NAME} \
    --repository-format=docker \
    --location=${REGION} \
    --description="Docker repository for Cloud Run labs" || true

# 4. Build Container using Cloud Build
echo "==> Submitting Cloud Build for ${IMAGE_NAME}..."
gcloud builds submit --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:v1

# 5. Deploy to Cloud Run
echo "==> Deploying service to Cloud Run..."
gcloud run deploy ${SERVICE_NAME} \
    --image=${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:v1 \
    --platform=managed \
    --region=${REGION} \
    --allow-unauthenticated

echo "==> Cloud Run deployment complete! Run 'gcloud run services list' to inspect."
