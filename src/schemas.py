from pydantic import BaseModel


class EmailSchema(BaseModel):
    email: str
    subject: str
    message: str
