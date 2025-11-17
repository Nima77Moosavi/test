from sqlalchemy.ext.asyncio import AsyncSession
from .repositories import NotificationRepository
from .schemas import NotificationSchema

class NotificationService:
    def __init__(self, repository: NotificationRepository):
        self.repository = repository
        
    async def send_notification(self, notification: NotificationSchema):
        created_notification = await self.repository.create_notification(notification)
        # Here you would add logic to actually send the notification (e.g., via email or SMS)
        return created_notification