from typing import Protocol

from domain.email.models.email_message import EmailMessage
from domain.email.models.email_send_result import EmailSendResult


class EmailClient(Protocol):
    async def send_email(self, email_message: EmailMessage) -> EmailSendResult: ...
