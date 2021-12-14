from datetime import date, datetime
from src.app import db
from src.models import Driver, Vehicle
from flask import request, jsonify

import os
import sqlite3


# ********************************************************
def datetime_format():
    return "%d/%m/%Y %H:%M:%S"


def query_date_format():
    return "%d-%m-%Y"


def now():
    return datetime.now().strftime(datetime_format())


# **********************************************************


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

# def find_drivers(filters: dict):  # нужно изменить на ^^^
#     q = db.session.query(Driver).filter(Driver.first_name.like(f'%{filters["first_name"]}%'),
#                                         Driver.last_name.like(f'%{filters["last_name"]}%'))
#     if filters['created_at[gte]']:
#         q = q.filter(Driver.created_at >= filters['created_at[gte]'])
#     if filters['created_at[lte]']:
#         q = q.filter(Driver.created_at <= filters['created_at[lte]'])
#
#     if filters['updated_at[gte]']:
#         q = q.filter(Driver.updated_at >= filters['updated_at[gte]'])
#     if filters['updated_at[lte]']:
#         q = q.filter(Driver.updated_at <= filters['updated_at[lte]'])
#     return q.all()
def find_drivers(filters: dict):  # def find_drivers(filters: dict):
    # Save the data in db
    db_path = os.path.join('create_db', 'DV')
    conn = sqlite3.connect(db_path)
    # query = f'Driver (first_name: {Driver.first_name}, last_name: {Driver.last_name}, ' \
    #         f'created_at: {Driver.created_at}, updated_at: {Driver.updated_at})'
    q = db.session.query(Driver).filter(Driver.first_name.like(f'%{filters["first_name"]}%'),
                                        Driver.last_name.like(f'%{filters["last_name"]}%'))
    # cur = conn.cursor()
    # cur.execute(query)
    # conn.commit()
    #
    # return jsonify({'id': cur.lastrowid})
    # # q = db.session.query(Driver).filter(Driver.first_name.like(f'%{filters["first_name"]}%'),
    # #                                     Driver.last_name.like(f'%{filters["last_name"]}%'))

    created_at__gte = request.args.get('created_at__gte')
    created_at__lte = request.args.get('created_at__lte')

    # query = 'SELECT * FROM Driver;'
    # conn.row_factory = dict_factory
    cur = conn.cursor()
    all_drivers = cur.execute(q).fetchall()

    if created_at__gte is not None:
        gte_drivers = []
        dt_gte = datetime.strptime(created_at__gte, query_date_format())
        for dr in all_drivers:
            # log(str(dr))
            dt = datetime.strptime(dr.get('created_at'), datetime_format())
            if dt >= dt_gte:
                gte_drivers.append(dr)
        return jsonify(gte_drivers)
    else:
        if created_at__lte is not None:
            lte_drivers = []
            dt_lte = datetime.strptime(created_at__lte, query_date_format())
            for dr in all_drivers:
                dt = datetime.strptime(dr.get('created_at'), datetime_format())
                if dt <= dt_lte:
                    lte_drivers.append(dr)
            return jsonify(lte_drivers)

    return jsonify(all_drivers)


# def find_vehicles(filters: dict):  # возможно лишняя функция
#     q = db.session.query(Vehicle).filter(Vehicle.make.like(f'%{filters["make"]}%'),
#                                          Vehicle.model.like(f'%{filters["model"]}%'),
#                                          Vehicle.plate_number.like(f'%{filters["plate_number"]}%'))
#     if filters['start_date[gte]']:
#         q = q.filter(Vehicle.start_date >= filters['start_date[gte]'])
#     if filters['start_date[lte]']:
#         q = q.filter(Vehicle.start_date <= filters['start_date[lte]'])
#
#     if filters['end_date[gte]']:
#         q = q.filter(Vehicle.end_date >= filters['end_date[gte]'])
#     if filters['end_date[lte]']:
#         q = q.filter(Vehicle.end_date <= filters['end_date[lte]'])
#     return q.all()

def find_vehicles(filters: dict):
    q = db.session.query(Vehicle).filter(Vehicle.plate_number.like(f'%{filters["plate_number"]}%'))
    if filters['start_date[gte]']:
        q = q.filter(Vehicle.start_date >= filters['start_date[gte]'])
    if filters['start_date[lte]']:
        q = q.filter(Vehicle.start_date <= filters['start_date[lte]'])

    if filters['end_date[gte]']:
        q = q.filter(Vehicle.end_date >= filters['end_date[gte]'])
    if filters['end_date[lte]']:
        q = q.filter(Vehicle.end_date <= filters['end_date[lte]'])
    return q.all()


def delete_all_drivers():
    db.session.query(Driver).delete()
    db.session.commit()


def delete_all_vehicles():
    db.session.query(Vehicle).delete()
    db.session.commit()