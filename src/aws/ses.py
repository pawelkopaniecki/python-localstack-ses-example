from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from functools import cache

from aioboto3 import Session
from types_aiobotocore_ses import SESClient

from ..core.settings import settings


@cache
def _get_session() -> Session:
    """Get cached aioboto3 session instance.

    Returns:
        Session: Cached aioboto3 Session instance.
    """

    return Session()


@asynccontextmanager
async def get_ses_client() -> AsyncIterator[SESClient]:
    """Get SES client instance.

    Yields:
        SESClient: SES client instance.
    """

    session = _get_session()

    async with session.client(
        service_name="ses",
        region_name=settings.AWS_REGION,
        endpoint_url=settings.AWS_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    ) as client:
        yield client
