from types_aiobotocore_ses import SESClient

from domain.email.models.email_message import EmailMessage
from domain.email.models.email_send_result import EmailSendResult
from domain.email.ports.email_client import EmailClient


class AWSEmailClient(EmailClient):
    def __init__(self, ses_client: SESClient, sender_email_address: str):
        self.ses_client = ses_client
        self.sender_email_address = sender_email_address

    async def send_email(self, email_message: EmailMessage) -> EmailSendResult:
        result = await self.ses_client.send_email(
            Source=self.sender_email_address,
            Destination={"ToAddresses": [email_message.to_address]},
            Message={
                "Subject": {"Data": email_message.subject, "Charset": "string"},
                "Body": {"Text": {"Data": email_message.message, "Charset": "string"}},
            },
        )

        return EmailSendResult(success=True, message=result["MessageId"])
