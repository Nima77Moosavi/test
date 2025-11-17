from pydantic import BaseModel


class NotificationSchema(BaseModel):
    name: str
    email: str
    type: str = "email"
