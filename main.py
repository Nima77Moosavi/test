from fastapi import FastAPI

from notifications.database import Base, engine
from notifications.routers import router as notification_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(notification_router)
