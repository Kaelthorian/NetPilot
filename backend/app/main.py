from fastapi import FastAPI

from app.database import Base, engine
from app.models.device_db import DeviceDB
from app.routers.devices import router as devices_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="NetPilot API",
    description="Network automation and monitoring platform",
    version="0.1.0",
)


app.include_router(devices_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "NetPilot API",
    }