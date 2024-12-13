from fastapi import FastAPI

from .aws import send_email
from .schemas import EmailSchema

app = FastAPI()


@app.get("/api/v1/ping", status_code=200)
async def ping():
    """Liveness check endpoint."""

    return {"message": "Email service is running"}


@app.post("/api/v1/email/send", status_code=201)
async def email_route(email: EmailSchema):
    """Send email endpoint.

    Args:
        email (EmailSchema): Email to be sent.
    """

    response = send_email(email)

    return {
        "message": "Email sent successfully",
        "message_id": response["MessageId"],
    }
