from sqlalchemy.ext.asyncio import AsyncSession
from .models import NotificationModel
from .schemas import NotificationSchema

class NotificationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def create_notification(self, notification: NotificationSchema) -> NotificationModel:
        new_notification = NotificationModel(
            name=notification.name,
            content=f"Notification of type {notification.type} for {notification.name}",
            type=notification.type
        )
        self.db.add(new_notification)
        await self.db.commit()
        await self.db.refresh(new_notification)
        return new_notification
        