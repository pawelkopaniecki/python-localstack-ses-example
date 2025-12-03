from pydantic import BaseModel, EmailStr


class EmailRequestSchema(BaseModel):
    """Pydantic model schema for email data validation.

    Attributes:
        address (str): The recipient's email address
        subject (str): The subject line of the email
        message (str): The main body content of the email
    """

    address: EmailStr
    subject: str
    message: str


class EmailResponseSchema(BaseModel):
    message: str
    message_id: str
