from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import (
    RepairOrder,
    RepairOrderCreate,
    RepairOrderResponse
)

router = APIRouter(
    prefix="/repair-orders",
    tags=["Repair Orders"]
)


@router.post("/", response_model=RepairOrderResponse)
def create_order(
    order: RepairOrderCreate,
    db: Session = Depends(get_db)
):
    db_order = RepairOrder(**order.model_dump())

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


@router.get("/", response_model=list[RepairOrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(RepairOrder).all()