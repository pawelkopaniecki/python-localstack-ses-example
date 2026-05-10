from dataclasses import dataclass


@dataclass
class EmailSendResult:
    success: bool
    message: str
