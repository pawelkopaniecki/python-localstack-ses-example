#!/usr/bin/env bash

set -e pipefail


echo "########### Creating profile ###########"

aws configure set aws_access_key_id "dummy" --profile test-profile
aws configure set aws_secret_access_key "dummy" --profile test-profile
aws configure set region "eu-west-1" --profile test-profile
aws configure set output "table" --profile test-profile

echo "########### Verifying identity ###########"

aws ses verify-email-identity \
    --endpoint-url=http://localhost:4566 \
    --region eu-west-1 \
    --profile test-profile \
    --email-address test@test.test
