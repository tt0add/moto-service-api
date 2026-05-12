from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)


class ClientCreate(BaseModel):
    full_name: str
    phone: str
    email: str


class ClientResponse(ClientCreate):
    id: int

    class Config:
        from_attributes = True


class Motorcycle(Base):
    __tablename__ = "motorcycles"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))

    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)

    year = Column(Integer)
    vin = Column(String, unique=True)


class MotorcycleCreate(BaseModel):
    client_id: int
    brand: str
    model: str
    year: int
    vin: str


class MotorcycleResponse(MotorcycleCreate):
    id: int

    class Config:
        from_attributes = True


class Master(Base):
    __tablename__ = "masters"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)
    specialization = Column(String)
    phone = Column(String)


class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String, unique=True)


class StatusCreate(BaseModel):
    status_name: str


class StatusResponse(StatusCreate):
    id: int

    class Config:
        from_attributes = True


class RepairOrder(Base):
    __tablename__ = "repair_orders"

    id = Column(Integer, primary_key=True, index=True)

    client_id = Column(Integer, ForeignKey("clients.id"))
    motorcycle_id = Column(Integer, ForeignKey("motorcycles.id"))
    master_id = Column(Integer, ForeignKey("masters.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))

    problem_description = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)


class RepairOrderCreate(BaseModel):
    client_id: int
    motorcycle_id: int
    master_id: int
    status_id: int
    problem_description: str


class RepairOrderResponse(RepairOrderCreate):
    id: int

    class Config:
        from_attributes = True