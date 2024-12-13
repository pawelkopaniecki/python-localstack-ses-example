from pydantic import BaseModel


class EmailSchema(BaseModel):
    """Pydantic model schema for email data validation.

    Attributes:
        address (str): The recipient's email address
        subject (str): The subject line of the email
        message (str): The main body content of the email
    """

    address: str
    subject: str
    message: str
