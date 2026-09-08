from fastapi import APIRouter, HTTPException

from app.models.device import Device, DeviceCreate


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


devices: list[Device] = []
next_id = 1
