import os

import boto3
from mypy_boto3_ses.type_defs import SendEmailResponseTypeDef

endpoint_url = (
    "http://localstack:4566" if os.getenv("DOCKER") else "http://127.0.0.1:4566"
)

client = boto3.client(
    service_name="ses",
    region_name="eu-west-1",
    endpoint_url=endpoint_url,
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
)


def send_email(email: str, subject: str, message: str) -> SendEmailResponseTypeDef:
    return client.send_email(
        Source="test@test.test",
        Destination={"ToAddresses": [email]},
        Message={
            "Subject": {"Data": subject, "Charset": "string"},
            "Body": {"Text": {"Data": message, "Charset": "string"}},
        },
    )
