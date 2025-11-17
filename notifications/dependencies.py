from services.notification_service import NotificationService


async def get_notification_service():
    return NotificationService()