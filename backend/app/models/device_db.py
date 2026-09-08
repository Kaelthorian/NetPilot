from sqlalchemy import Column, Integer, String

from app.database import Base


class DeviceDB(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
