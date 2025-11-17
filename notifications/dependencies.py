from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db
from .repositories import NotificationRepository
from .services import NotificationService
from .services import NotificationService, get_sender, NotificationSender
from .schemas import NotificationSchema

from typing import Callable


def get_notification_service(db: AsyncSession = Depends(get_db)) -> NotificationService:
    repository = NotificationRepository(db)

    # Inject sender factory
    sender_factory: Callable[[NotificationSchema],
                             NotificationSender] = get_sender

    return NotificationService(repository, sender_factory)
