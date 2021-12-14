from datetime import date

from flask_restful import Resource, reqparse
import db_methods
from app import app
from utils import transfer_date
import datetime


@app.route('/')
def home():
    return '<h1>Home page!</h1>'


class CreateDriver(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('created_at', type=datetime,
                            help='The date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"')
        parser.add_argument('updated_at', type=datetime,
                            help='The date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"')
        args = parser.parse_args(strict=True)
        first_name = args['first_name']
        last_name = args['last_name']

        try:
            created_at = transfer_date(args['created_at'])
        except ValueError as e:
            return {"message": {
                "created_at": f'{e}\nThe date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"'}}, 400
        try:
            updated_at = transfer_date(args['updated_at'])
        except ValueError as e:
            return {"message": {
                "updated_at": f'{e}\nThe date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"'}}, 400

        driver_id = db_methods.add_driver(first_name, last_name, created_at, updated_at)
        return {"message": {'driver_id': driver_id, 'first_name': first_name, 'last_name': last_name,
                            'created_at': str(created_at), 'updated_at': str(updated_at)}}, 201


class CreateVehicle(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('driver_id', type=int, required=True)  # db.ForeignKey('driver.id')
        parser.add_argument('make', type=str, required=True)
        parser.add_argument('model', type=str, required=True)
        parser.add_argument('plate_number', type=str(8), unique=True, required=True)  # example "AA 1234 OO"
        parser.add_argument('created_at', type=datetime,
                            help='The date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"')
        parser.add_argument('updated_at', type=datetime,
                            help='The date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"')
        args = parser.parse_args(strict=True)
        make = args['make']
        model = args['model']
        plate_number = args['plate_number']

        try:
            created_at = transfer_date(args['created_at'])
        except ValueError as e:
            return {"message": {
                "created_at": f'{e}\nThe date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"'}}, 400
        try:
            updated_at: date = transfer_date(args['updated_at'])
        except ValueError as e:
            return {"message": {
                "updated_at": f'{e}\nThe date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"'}}, 400

        vehicle_id = db_methods.add_vehicle(make, model, plate_number, created_at, updated_at)
        return {"message": {'id': vehicle_id, 'make': make, 'model': model, 'plate_number': plate_number,
                            'created_at': str(created_at), 'updated_at': str(updated_at)}}, 201


class Drivers(Resource):
    def get(self):
        drivers = db_methods.get_all_drivers()
        drivers_list = []
        for driver in drivers:
            # drivers_list.append({'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name,
            #                      'created_at': str(driver.start_date), 'updated_at': str(driver.end_date)})
            drivers_list.append({'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name})
        return {"message": {"drivers": drivers_list}}, 200


class Driver(Resource):
    def get(self, driver_id):
        driver = db_methods.get_driver_by_id(driver_id)
        if driver:
            driver_info = {'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name,
                           'created_at': str(driver.start_date), 'updated_at': str(driver.end_date)}
            return {"message": {"driver": driver_info}}, 200
        else:
            return {"message": {"driver": f"Driver with id={driver_id} not found"}}, 400

    def delete(self, driver_id):
        if db_methods.driver_exists(driver_id):
            db_methods.delete_driver_by_id(driver_id)
            return {"message": {"delete": f"Driver with id={driver_id} successfully deleted!"}}, 200
        else:
            return {"message": {"delete": f"Driver with id={driver_id} not found!"}}, 400


class Vehicles(Resource):
    def get(self):
        vehicles = db_methods.get_all_vehicles()
        vehicles_list = []
        for vehicle in vehicles:
            # vehicles_list.append({'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
            #                       'plate_number': vehicle.plate_number, 'created_at': str(vehicle.start_date),
            #                       'updated_at': str(vehicle.end_date)})
            vehicles_list.append({'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
                                  'plate_number': vehicle.plate_number})
        return {"message": {"vehicles": vehicles_list}}, 200


class Vehicle(Resource):
    def get(self, vehicle_id):
        vehicle = db_methods.get_vehicle_by_id(vehicle_id)
        if vehicle:
            vehicle_info = {'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
                            'plate_number': vehicle.plate_number, 'created_at': str(vehicle.start_date),
                            'updated_at': str(vehicle.end_date)}
            return {"message": {"vehicle": vehicle_info}}, 200
        else:
            return {"message": {"vehicle": f"Vehicle with id={vehicle_id} not found"}}, 400

    def delete(self, vehicle_id):
        if db_methods.vehicle_exists(vehicle_id):
            db_methods.delete_vehicle_by_id(vehicle_id)
            return {"message": {"delete": f"Vehicle with id={vehicle_id} successfully deleted!"}}, 200
        else:
            return {"message": {"delete": f"Vehicle with id={vehicle_id} not found!"}}, 400