from fastapi import FastAPI

from .aws import send_email
from .schemas import EmailSchema

app = FastAPI()


@app.post("/api/v1/email/send", status_code=201)
async def email_route(email: EmailSchema):
    response = send_email(**email.__dict__)

    return {
        "message": "Email sent successfully",
        "message_id": response["MessageId"],
    }
