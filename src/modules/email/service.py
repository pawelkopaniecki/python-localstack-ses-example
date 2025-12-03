from mypy_boto3_ses.client import SESClient
from mypy_boto3_ses.type_defs import SendEmailResponseTypeDef

from ...aws.ses import get_ses_client
from ...core.settings import settings


class EmailService:
    """Class containing service methods related to email."""

    def __init__(self, ses_client: SESClient):
        self.ses_client = ses_client

    def send_email(
        self, to_address: str, subject: str, message: str
    ) -> SendEmailResponseTypeDef:
        """Send email using AWS SES.

        Args:
            email (EmailSchema): Email to be sent.

        Returns:
            SendEmailResponseTypeDef: AWS SES email response.
        """

        return self.ses_client.send_email(
            Source=settings.SENDER_EMAIL_ADDRESS,
            Destination={"ToAddresses": [to_address]},
            Message={
                "Subject": {"Data": subject, "Charset": "string"},
                "Body": {"Text": {"Data": message, "Charset": "string"}},
            },
        )


def get_email_service() -> EmailService:
    """Dependency injection method for creating new EmailService."""

    return EmailService(ses_client=get_ses_client())
