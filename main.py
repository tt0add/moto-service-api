from fastapi import FastAPI

from database import Base, engine

from models import (
    Client,
    Master,
    Motorcycle,
    RepairOrder,
    Status
)

from routers.clients import router as clients_router
from routers.motorcycles import router as motorcycles_router
from routers.repair_orders import router as repair_orders_router
from routers.statuses import router as statuses_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Moto Service API")

app.include_router(clients_router)
app.include_router(motorcycles_router)
app.include_router(repair_orders_router)
app.include_router(statuses_router)


@app.get("/")
def root():
    return {"message": "Moto Service API"}
