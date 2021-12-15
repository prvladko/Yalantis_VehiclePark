from datetime import date, datetime
from src.app import db
from src.models import Driver, Vehicle

from flask import jsonify, request


def add_driver(first_name: str, last_name: str, created_at: datetime.now(), updated_at: datetime.now()) -> int:
    new_driver = Driver(first_name=first_name, last_name=last_name,
                        created_at=created_at, updated_at=updated_at)
    db.session.add(new_driver)
    db.session.commit()
    return new_driver.id


def add_vehicle(driver_id: int, make: str, model: str, plate_number: str,
                created_at: datetime.now(), updated_at: datetime.now()) -> int:
    new_vehicle = Vehicle(driver_id=driver_id, make=make, model=model, plate_number=plate_number,
                          created_at=created_at, updated_at=updated_at)
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle.id


def get_all_drivers():
    return db.session.query(Driver).all()


def get_all_vehicles():
    return db.session.query(Vehicle).all()


def get_driver_by_id(driver_id: int):
    return db.session.query(Driver).filter(Driver.id == driver_id).first()


def get_vehicle_by_id(vehicle_id: int):
    return db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).first()


def driver_exists(driver_id: int) -> bool:
    return bool(db.session.query(Driver).filter(Driver.id == driver_id).count())


def delete_driver_by_id(driver_id: int):
    db.session.query(Driver).filter(Driver.id == driver_id).delete()
    db.session.commit()


def vehicle_exists(vehicle_id: int) -> bool:
    return bool(db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).count())


def delete_vehicle_by_id(vehicle_id: int):
    db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).delete()
    db.session.commit()


def update_driver_info(driver_id: int, update_data: dict):
    db.session.query(Driver).filter(Driver.id == driver_id).update(update_data)
    db.session.commit()


def update_vehicle_info(vehicle_id: int, update_data: dict):
    db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).update(update_data)
    db.session.commit()


# + GET /drivers/driver/?created_at__gte=10-11-2021 - вивід списку водіїв, які створені після 10-11-2021
# + GET /drivers/driver/?created_at__lte=16-11-2021 - вивід списку водіїв, котрі створені до 16-11-2021

def find_drivers(filters: dict):
    q = db.session.query(Driver).filter(Driver.first_name.like(f'%{filters["first_name"]}%'),
                                        Driver.last_name.like(f'%{filters["last_name"]}%'))
    if filters['created_at[gte]']:
        q = q.filter(Driver.created_at >= filters['created_at[gte]'])
    if filters['created_at[lte]']:
        q = q.filter(Driver.created_at <= filters['created_at[lte]'])

    if filters['updated_at[gte]']:
        q = q.filter(Driver.updated_at >= filters['updated_at[gte]'])
    if filters['updated_at[lte]']:
        q = q.filter(Driver.updated_at <= filters['updated_at[lte]'])
    return q.all()


def find_vehicles(filters: dict):  # just for testing
    # q = db.session.query(Vehicle).filter(Vehicle.make.like(f'%{filters["make"]}%'),
    #                                      Vehicle.model.like(f'%{filters["model"]}%'),
    #                                      Vehicle.plate_number.like(f'%{filters["plate_number"]}%'))
    q = db.session.query(Vehicle).filter()
    if filters['created_at[gte]']:
        q = q.filter(Vehicle.created_at >= filters['created_at[gte]'])
    if filters['created_at[lte]']:
        q = q.filter(Vehicle.created_at <= filters['created_at[lte]'])
    #
    # if filters['updated_at[gte]']:
    #     q = q.filter(Vehicle.updated_at >= filters['updated_at[gte]'])
    # if filters['updated_at[lte]']:
    #     q = q.filter(Vehicle.updated_at <= filters['updated_at[lte]'])
    return q.all()


def find_vehicles_gte(filters: date):
    dt = datetime.strptime("10/11/21", "%d/%m/%y")
    q = db.session.query(Vehicle).filter()
    if filters:
        q = q.filter(Vehicle.created_at >= dt)
    return q.all()


def find_vehicles_lte(filters: date):
    dt = datetime.strptime("16/11/21", "%d/%m/%y")
    q = db.session.query(Vehicle).filter()
    if filters:
        q = q.filter(Vehicle.created_at <= dt)
    return q.all()


# *************************************************************************
def get_drivers() -> dict:
    """Return drivers"""
    args = request.args
    if args:
        if args.get('created_at__gte'):
            query_date = args.get('created_at__gte')
            datetime_obj = datetime.strptime(query_date, "%d-%m-%Y")
            drivers = Driver.query.filter(Driver.created_at >= datetime_obj)
            return jsonify({'drivers': [driver.to_json() for driver in drivers]})

        elif args.get('created_at__lte'):
            query_date = args.get('created_at__lte')
            datetime_obj = datetime.strptime(query_date, "%d-%m-%Y")
            drivers = Driver.query.filter(Driver.created_at <= datetime_obj)
            return jsonify({'drivers': [driver.to_json() for driver in drivers]})

    drivers = Driver.query.all()
    return jsonify({'drivers': [driver.to_json() for driver in drivers]})


# *************************************************************************


def delete_all_drivers():
    db.session.query(Driver).delete()
    db.session.commit()


def delete_all_vehicles():
    db.session.query(Vehicle).delete()
    db.session.commit()
