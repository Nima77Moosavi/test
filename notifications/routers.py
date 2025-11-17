from fastapi import APIRouter, Depends, HTTPException
from .schemas import NotificationSchema
from .services import NotificationService
from .dependencies import get_notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/")
async def create_notification(
    notification: NotificationSchema,
    service: NotificationService = Depends(get_notification_service)
):
    return await service.send_notification(notification)
