from dataclasses import dataclass


@dataclass
class EmailMessage:
    to_address: str
    subject: str
    message: str
