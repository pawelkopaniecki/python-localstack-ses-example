from fastapi import APIRouter, Depends

from .schemas.email import EmailRequestSchema, EmailResponseSchema
from .service import EmailService, get_email_service

router = APIRouter(prefix="/v1/email", tags=["email"])


@router.post("/send", response_model=EmailResponseSchema)
async def email_route(
    request: EmailRequestSchema,
    email_service: EmailService = Depends(get_email_service),
):
    """Send email endpoint.

    Args:
        email (EmailSchema): Email to be sent.
        ses_client (SESClient): Boto3 SES client instance.
    """

    response = email_service.send_email(
        request.address, request.subject, request.message
    )

    return EmailResponseSchema(
        message="Email sent successfully", message_id=response["MessageId"]
    )
