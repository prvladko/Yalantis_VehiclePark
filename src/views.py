from datetime import date
from flask_restful import Resource, reqparse
from src import db_methods
from src.utils import transfer_date, abort_if_driver_doesnt_exist, abort_if_vehicle_doesnt_exist, validate_dates
import datetime


class Home(Resource):
    def get(self):
        return {"message": "VehicleParkAPI home page"}


class CreateDriver(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('created_at', type=transfer_date, required=True)  # type=datetime
        parser.add_argument('updated_at', type=transfer_date, required=True)  # type=datetime
        args = parser.parse_args(strict=True)
        validate_dates(args["created_at"], args["updated_at"])
        driver_id = db_methods.add_driver(args['first_name'], args['last_name'],
                                          args['created_at'], args['updated_at'])
        return {"message": {'driver_id': driver_id, 'first_name': args['first_name'], 'last_name': args['last_name'],
                            'created_at': str(args['created_at']),
                            'updated_at': str(args['updated_at'])}}, 201


class CreateVehicle(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('driver_id', type=int, required=True)  # db.ForeignKey('driver.id')
        parser.add_argument('make', type=str, required=True)
        parser.add_argument('model', type=str, required=True)
        parser.add_argument('plate_number', type=str, required=True)  # example "AA 1234 OO"
        parser.add_argument('created_at', type=transfer_date, required=True)  # type=datetime
        parser.add_argument('updated_at', type=transfer_date, required=True)  # type=datetime
        args = parser.parse_args(strict=True)
        validate_dates(args["created_at"], args["updated_at"])
        vehicle_id = db_methods.add_vehicle(args['driver_id'], args['make'], args['model'], args['plate_number'],
                                            args['created_at'], args['updated_at'])
        return {"message": {'vehicle_id': vehicle_id, 'make': args['make'], 'model': args['model'],
                            'plate_number': args['plate_number'],
                            'created_at': str(args['created_at']),
                            'updated_at': str(args['updated_at'])}}, 201


class Drivers(Resource):
    def get(self):
        drivers = db_methods.get_all_drivers()
        drivers_list = []
        for driver in drivers:
            drivers_list.append({'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name})
        return {"message": {"drivers": drivers_list}}, 200


class Driver(Resource):
    def get(self, driver_id):
        driver = db_methods.get_driver_by_id(driver_id)
        if driver:
            driver_info = {'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name,
                           'created_at': str(driver.created_at), 'updated_at': str(driver.updated_at)}
            return {"message": {"driver": driver_info}}, 200
        else:
            return {"message": {"driver": f"Driver with id={driver_id} not found"}}, 400

    def delete(self, driver_id):
        abort_if_driver_doesnt_exist(driver_id)
        db_methods.delete_driver_by_id(driver_id)
        return {"message": {"delete": f"Driver with id={driver_id} successfully deleted!"}}, 200

    def patch(self, driver_id):
        abort_if_driver_doesnt_exist(driver_id)
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('created_at', type=transfer_date)
        parser.add_argument('updated_at', type=transfer_date)
        args = parser.parse_args(strict=True)
        update_data = {}
        for key, value in args.items():
            if value:
                update_data[key] = value
        if len(update_data) == 0:
            return {"message": {"patch": "No arguments passed"}}, 400
        # --- ValidateDates
        created_at = args['created_at']
        updated_at = args['updated_at']
        driver = db_methods.get_driver_by_id(driver_id)
        if created_at is None:
            created_at = driver.created_at
        if updated_at is None:
            updated_at = driver.updated_at
        validate_dates(created_at, updated_at)

        db_methods.update_driver_info(driver_id, update_data)
        driver = db_methods.get_driver_by_id(driver_id)
        driver_info = {'id': driver.id, 'first_name': driver.first_name, 'last_name': driver.last_name,
                       'created_at': str(driver.created_at),
                       'updated_at': str(driver.updated_at)}
        return {"message": {"driver": driver_info}}, 200


class Vehicles(Resource):
    def get(self):
        vehicles = db_methods.get_all_vehicles()
        vehicles_list = []
        for vehicle in vehicles:
            vehicles_list.append({'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
                                  'plate_number': vehicle.plate_number})
        return {"message": {"vehicles": vehicles_list}}, 200


class Vehicle(Resource):
    def get(self, vehicle_id):
        vehicle = db_methods.get_vehicle_by_id(vehicle_id)
        if vehicle:
            vehicle_info = {'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
                            'plate_number': vehicle.plate_number, 'created_at': str(vehicle.created_at),
                            'updated_at': str(vehicle.updated_at)}
            return {"message": {"vehicle": vehicle_info}}, 200
        else:
            return {"message": {"vehicle": f"Vehicle with id={vehicle_id} not found"}}, 400

    def delete(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        db_methods.delete_vehicle_by_id(vehicle_id)
        return {"message": {"delete": f"Vehicle with id={vehicle_id} successfully deleted!"}}, 200

    def patch(self, vehicle_id):
        abort_if_vehicle_doesnt_exist(vehicle_id)
        parser = reqparse.RequestParser()
        parser.add_argument('make', type=str)
        parser.add_argument('model', type=str)
        parser.add_argument('plate_number', type=str)
        parser.add_argument('created_at', type=transfer_date)
        parser.add_argument('updated_at', type=transfer_date)
        args = parser.parse_args(strict=True)
        update_data = {}
        for key, value in args.items():
            if value:
                update_data[key] = value
        if len(update_data) == 0:
            return {"message": {"patch": "No arguments passed"}}, 400
        # --- ValidateDates
        created_at = args['created_at']
        updated_at = args['updated_at']
        vehicle = db_methods.get_vehicle_by_id(vehicle_id)
        if created_at is None:
            created_at = vehicle.created_at
        if updated_at is None:
            updated_at = vehicle.updated_at
        validate_dates(created_at, updated_at)

        db_methods.update_vehicle_info(vehicle_id, update_data)
        vehicle = db_methods.get_vehicle_by_id(vehicle_id)
        vehicle_info = {'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model,
                        'plate_number': vehicle.plate_number,
                        'created_at': str(vehicle.created_at),
                        'updated_at': str(vehicle.updated_at)}
        return {"message": {"vehicle": vehicle_info}}, 200


class FindDriver(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('created_at[gte]', type=transfer_date)
        parser.add_argument('created_at[lte]', type=transfer_date)
        parser.add_argument('updated_at[gte]', type=transfer_date)
        parser.add_argument('updated_at[lte]', type=transfer_date)

        args = parser.parse_args(strict=True)
        drivers = db_methods.find_drivers(args)
        drivers_list = []
        for driver in drivers:
            drivers_list.append({'driver_id': driver.driver_id,
                                 'first_name': driver.first_name,
                                 'last_name': driver.last_name,
                                 'created_at': str(driver.created_at),
                                 'updated_at': str(driver.updated_at)})
        return {"message": {"drivers": drivers_list}}


# for test
class FindVehicle(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('make', type=str, required=True)
        parser.add_argument('model', type=str, required=True)
        parser.add_argument('plate_number', type=str, required=True)
        parser.add_argument('created_at[gte]', type=transfer_date)
        parser.add_argument('created_at[lte]', type=transfer_date)
        parser.add_argument('updated_at[gte]', type=transfer_date)
        parser.add_argument('updated_at[lte]', type=transfer_date)

        args = parser.parse_args(strict=True)
        vehicles = db_methods.find_vehicles(args)
        vehicles_list = []
        for vehicle in vehicles:
            vehicles_list.append({'vehicle_id': vehicle.vehicle_id,
                                  'make': vehicle.make,
                                  'model': vehicle.model,
                                  'plate_number': vehicle.plate_number,
                                  'created_at': str(vehicle.created_at),
                                  'updated_at': str(vehicle.updated_at)})
        return {"message": {"vehicles": vehicles_list}}