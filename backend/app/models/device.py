from pydantic import BaseModel


class DeviceCreate(BaseModel):
    name: str
    ip_address: str
    device_type: str


class Device(DeviceCreate):
    id: int
