from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import (
    Motorcycle,
    MotorcycleCreate,
    MotorcycleResponse
)

router = APIRouter(
    prefix="/motorcycles",
    tags=["Motorcycles"]
)


@router.post("/", response_model=MotorcycleResponse)
def create_motorcycle(
    motorcycle: MotorcycleCreate,
    db: Session = Depends(get_db)
):
    db_motorcycle = Motorcycle(**motorcycle.model_dump())

    db.add(db_motorcycle)
    db.commit()
    db.refresh(db_motorcycle)

    return db_motorcycle


@router.get("/", response_model=list[MotorcycleResponse])
def get_motorcycles(db: Session = Depends(get_db)):
    return db.query(Motorcycle).all()