from pydantic import BaseModel, ConfigDict


class DeviceCreate(BaseModel):
    name: str
    ip_address: str
    device_type: str


class Device(DeviceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
