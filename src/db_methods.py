from datetime import date
from app import db
from models import Driver, Vehicle


def add_driver(first_name: str, last_name: str, created_at: date, updated_at: date) -> int:
    new_driver = Driver(first_name=first_name, last_name=last_name,
                        created_at=created_at, updated_at=updated_at)
    db.session.add(new_driver)
    db.session.commit()
    return new_driver.id


def add_vehicle(driver_id: int, make: str, model: str, plate_number: str, created_at: date, updated_at: date) -> int:
    new_vehicle = Vehicle(driver_id=driver_id, make=make, model=model, plate_number=plate_number,
                          created_at=created_at, updated_at=updated_at)
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle.id


def get_all_drivers():
    return db.session.query(Driver).all()


def get_all_vehicles():
    return db.session.query(Vehicle).all()


def get_driver_by_id(driver_id):
    return db.session.query(Driver).filter(Driver.id == driver_id).first()


def get_vehicle_by_id(id_):
    return db.session.query(Vehicle).filter(Vehicle.id == id_).first()