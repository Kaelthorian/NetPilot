from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.device import Device, DeviceCreate
from app.models.device_db import DeviceDB


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.post("/", response_model=Device, status_code=201)
def create_device(
    device_data: DeviceCreate,
    db: Session = Depends(get_db),
):
    device = DeviceDB(
        name=device_data.name,
        ip_address=device_data.ip_address,
        device_type=device_data.device_type,
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


@router.get("/", response_model=list[Device])
def get_devices(db: Session = Depends(get_db)):
    return db.query(DeviceDB).all()


@router.get("/{device_id}", response_model=Device)
def get_device(device_id: int, db: Session = Depends(get_db)):
    device = (
        db.query(DeviceDB)
        .filter(DeviceDB.id == device_id)
        .first()
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.delete("/{device_id}", status_code=204)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    device = (
        db.query(DeviceDB)
        .filter(DeviceDB.id == device_id)
        .first()
    )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    db.delete(device)
    db.commit()

    return
