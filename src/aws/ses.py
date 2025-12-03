from functools import cache

import boto3
from mypy_boto3_ses.client import SESClient

from ..core.settings import settings


@cache
def get_ses_client() -> SESClient:
    """Get cached SES client instance.

    Returns:
        SESClient: Boto3 SES client instance.
    """

    return boto3.client(
        service_name="ses",
        region_name=settings.AWS_REGION,
        endpoint_url=settings.AWS_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
