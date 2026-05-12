from database import SessionLocal
from models import (
    Client,
    Master,
    Motorcycle,
    RepairOrder,
    Status
)

db = SessionLocal()

statuses = [
    Status(status_name="Принят"),
    Status(status_name="В ремонте"),
    Status(status_name="Готов")
]

masters = [
    Master(
        full_name="Иван Петров",
        specialization="Двигатель",
        phone="111111"
    ),
    Master(
        full_name="Алексей Смирнов",
        specialization="Электрика",
        phone="222222"
    ),
    Master(
        full_name="Дмитрий Волков",
        specialization="Подвеска",
        phone="333333"
    )
]

clients = [
    Client(
        full_name="Артем Иванов",
        phone="900001",
        email="client1@test.com"
    ),
    Client(
        full_name="Максим Соколов",
        phone="900002",
        email="client2@test.com"
    ),
    Client(
        full_name="Никита Орлов",
        phone="900003",
        email="client3@test.com"
    ),
    Client(
        full_name="Егор Кузнецов",
        phone="900004",
        email="client4@test.com"
    ),
    Client(
        full_name="Илья Морозов",
        phone="900005",
        email="client5@test.com"
    )
]

db.add_all(statuses)
db.add_all(masters)
db.add_all(clients)

db.commit()

motorcycles = [
    Motorcycle(
        client_id=1,
        brand="Yamaha",
        model="R1",
        year=2020,
        vin="VIN001"
    ),
    Motorcycle(
        client_id=2,
        brand="Honda",
        model="CBR600",
        year=2019,
        vin="VIN002"
    ),
    Motorcycle(
        client_id=3,
        brand="Suzuki",
        model="GSX-R750",
        year=2021,
        vin="VIN003"
    ),
    Motorcycle(
        client_id=4,
        brand="Kawasaki",
        model="Ninja 650",
        year=2018,
        vin="VIN004"
    ),
    Motorcycle(
        client_id=5,
        brand="BMW",
        model="S1000RR",
        year=2022,
        vin="VIN005"
    )
]

db.add_all(motorcycles)

db.commit()

orders = [
    RepairOrder(
        client_id=1,
        motorcycle_id=1,
        master_id=1,
        status_id=1,
        problem_description="Замена масла"
    ),
    RepairOrder(
        client_id=2,
        motorcycle_id=2,
        master_id=2,
        status_id=2,
        problem_description="Проблема с электрикой"
    ),
    RepairOrder(
        client_id=3,
        motorcycle_id=3,
        master_id=3,
        status_id=3,
        problem_description="Ремонт подвески"
    ),
    RepairOrder(
        client_id=4,
        motorcycle_id=4,
        master_id=1,
        status_id=1,
        problem_description="Диагностика двигателя"
    ),
    RepairOrder(
        client_id=5,
        motorcycle_id=5,
        master_id=2,
        status_id=2,
        problem_description="Замена аккумулятора"
    )
]

db.add_all(orders)

db.commit()

db.close()
