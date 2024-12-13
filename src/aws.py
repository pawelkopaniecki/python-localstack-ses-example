import os

import boto3

from mypy_boto3_ses.type_defs import SendEmailResponseTypeDef
from mypy_boto3_ses.client import SESClient
from .schemas import EmailSchema

ENDPOINT_URL = (
    "http://localstack:4566" if os.getenv("DOCKER") else "http://127.0.0.1:4566"
)

client: SESClient = boto3.client(
    service_name="ses",
    region_name="eu-west-1",
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
)


def send_email(email: EmailSchema) -> SendEmailResponseTypeDef:
    """Send email using AWS SES.

    Args:
        email (EmailSchema): Email to be sent.

    Returns:
        SendEmailResponseTypeDef: AWS SES email response.
    """

    return client.send_email(
        Source="test@test.test",
        Destination={"ToAddresses": [email.address]},
        Message={
            "Subject": {"Data": email.subject, "Charset": "string"},
            "Body": {"Text": {"Data": email.message, "Charset": "string"}},
        },
    )
