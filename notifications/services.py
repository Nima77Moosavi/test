from sqlalchemy.ext.asyncio import AsyncSession
from .repositories import NotificationRepository
from .schemas import NotificationSchema
from typing import Protocol, Optional


class NotificationSender(Protocol):
    async def send_notification(self, notification: NotificationSchema) -> str:
        """Send a notification and return a message"""
        ...


class EmailSender:
    async def send_notification(self, notification: NotificationSchema) -> str:
        return f"Sending email with content: {notification.content}"


class SMSSender:
    async def send_notification(self, notification: NotificationSchema) -> str:
        return f"Sending SMS with content: {notification.content}"


def get_sender(notification: NotificationSchema) -> NotificationSender:
    if notification.type == "email":
        return EmailSender()
    elif notification.type == "sms":
        return SMSSender()
    else:
        raise ValueError("Unsupported notification type")


class NotificationService:
    def __init__(self, repository: NotificationRepository, sender_factory: callable):
        self.repository = repository
        self.sender_factory = sender_factory

    async def send_notification(self, notification: NotificationSchema):
        # Save to database
        created_notification = await self.repository.create_notification(notification)

        # Choose sender dynamically
        sender = get_sender(notification)
        message = await sender.send_notification(notification)

        return {"notification": created_notification, "message": message}
