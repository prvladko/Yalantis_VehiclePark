import datetime
from flask_restful import abort
from src.db_methods import driver_exists, vehicle_exists


def transfer_date(raw_date: str) -> datetime.date:
    """
    Example:
    "14-12-2021" => datetime(day=14, month=12, year=2021)
    :param raw_date: str
    :return: datetime.date
    """
    date_obj = datetime.datetime.strptime(raw_date, '%d-%m-%Y').date()
    return date_obj


def abort_if_driver_doesnt_exist(driver_id):
    if not driver_exists(driver_id):
        abort(404, message=f"Driver {driver_id} doesn't exist!")


def abort_if_vehicle_doesnt_exist(vehicle_id):
    if not vehicle_exists(vehicle_id):
        abort(404, message=f"Vehicle {vehicle_id} doesn't exist!")