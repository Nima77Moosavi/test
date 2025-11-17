from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from database import Base


class NotificationModel(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
