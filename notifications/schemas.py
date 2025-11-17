from pydantic import BaseModel
from typing import Literal


class NotificationSchema(BaseModel):
    name: str
    content: str
    type: Literal["email", "sms"]