import datetime
from flask_restful import abort
from src.db_methods import driver_exists, vehicle_exists


def transfer_date(raw_date: str) -> datetime.date:
    date_obj = datetime.datetime.strptime(raw_date, '%d-%m-%Y').date()
    return date_obj


# just for test
def validate_dates(start_date, end_date):
    if start_date > end_date:
        abort(400, message={"message": {'date': f"The parameter start_date must be less than end_date"}})


def abort_if_driver_doesnt_exist(driver_id):
    if not driver_exists(driver_id):
        abort(404, message=f"Driver {driver_id} doesn't exist!")


def abort_if_vehicle_doesnt_exist(vehicle_id):
    if not vehicle_exists(vehicle_id):
        abort(404, message=f"Vehicle {vehicle_id} doesn't exist!")