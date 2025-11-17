from fastapi import APIRouter, Depends, HTTPException
from .schemas import NotificationSchema
from .services import NotificationService
from .dependencies import get_notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/", summary="Send a notification")
async def create_notification(
    notification: NotificationSchema,
    service: NotificationService = Depends(get_notification_service)
):
    """
    Creates a notification in the database and sends it via the appropriate channel
    (email or SMS) depending on the `type` field.
    """
    try:
        result = await service.send_notification(notification)
        return result
    except ValueError as e:
        # This will catch unsupported notification types
        raise HTTPException(status_code=400, detail=str(e))
