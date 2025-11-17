from fastapi import APIRouter
from schemas import NotificationSchema

router = APIRouter()

@router.post("/send-notification")
async def send_notification(notification: NotificationSchema):
    return {"message": "Notification sent"}