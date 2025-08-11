#!/bin/bash

AWS_REGION=eu-west-2
AWS_ACCOUNT_ID=873559750924
ECR_REPOSITORY=mlops-app-repo

# Authenticate Docker to AWS ECR
aws ecr get-login-password --region $AWS_REGION | \
docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Build and push Docker image for amd64 (x86_64) architecture directly to ECR
docker buildx build --platform linux/amd64 \
  -t $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:latest \
  --push .