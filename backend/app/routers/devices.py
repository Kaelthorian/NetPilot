from fastapi import APIRouter, HTTPException

from app.models.device import Device, DeviceCreate


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


devices: list[Device] = []
next_id = 1

@router.post("/", response_model=Device, status_code=201)
def create_device(device_data: DeviceCreate):
    global next_id

    device = Device(
        id=next_id,
        **device_data.model_dump(),
    )

    devices.append(device)
    next_id += 1

    return device
    
@router.get("/", response_model=list[Device])
def get_devices():
    return devices
    
    
@router.get("/{device_id}", response_model=Device)
def get_device(device_id: int):
    for device in devices:
        if device.id == device_id:
            return device

    raise HTTPException(
        status_code=404,
        detail="Device not found",
    )
    
    
@router.delete("/{device_id}", status_code=204)
def delete_device(device_id: int):
    for index, device in enumerate(devices):
        if device.id == device_id:
            devices.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Device not found",
    )