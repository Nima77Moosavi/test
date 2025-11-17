from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from notifications.database import get_db
from .repositories import NotificationRepository
from .services import NotificationService


def get_notification_service(db: AsyncSession = Depends(get_db)) -> NotificationService:
    """
    Dependency provider for UserService.
    Wires together DB session -> UserRepository -> UserService.
    """
    repository = NotificationRepository(db)
    return NotificationService(repository)
