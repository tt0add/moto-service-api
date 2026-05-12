from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import (
    Status,
    StatusCreate,
    StatusResponse
)

router = APIRouter(
    prefix="/statuses",
    tags=["Statuses"]
)


@router.post("/", response_model=StatusResponse)
def create_status(
    status: StatusCreate,
    db: Session = Depends(get_db)
):
    db_status = Status(**status.model_dump())

    db.add(db_status)
    db.commit()
    db.refresh(db_status)

    return db_status


@router.get("/", response_model=list[StatusResponse])
def get_statuses(db: Session = Depends(get_db)):
    return db.query(Status).all()