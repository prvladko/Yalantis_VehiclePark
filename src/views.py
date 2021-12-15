from flask import Response, jsonify, request
from flask_restful import Resource, reqparse
from app import db
from src.models import Driver, Vehicle
import datetime


class Home(Resource):
    def get(self):
        return {"message": "VehicleParkAPI home page"}


class AllDrivers(Resource):
    def get(self):
        def parse_date(date):
            (day, month, year) = date.split("-")
            return datetime.date(int(day), int(month), int(year))

        parser = reqparse.RequestParser()
        parser.add_argument("created_at__gte", type=str, help="Drivers created after this date")
        parser.add_argument("created_at__lte", type=str, help="Drivers created before this date")
        args = parser.parse_args()
        if args['created_at__gte']:
            d = parse_date(args['created_at__gte'])
            drivers = db.session.query(Driver).filter(Driver.created_at >= d).all()
        elif args['created_at__lte']:
            d = parse_date(args['created_at__lte'])
            drivers = db.session.query(Driver).filter(Driver.created_at <= d).all()
        else:
            drivers = db.session.query(Driver).all()
        return jsonify(drivers)

    def post(self):
        driver = Driver(first_name=request.json.get('first_name'),
                        last_name=request.json.get('last_name'))
        db.session.add(driver)
        db.session.commit()
        return Response(status=201)


class Drivers(Resource):
    def get(self, driver_id):
        try:
            driver = db.session.query(Driver).filter(Driver.id == driver_id).one()
            return jsonify(driver)
        except:
            return jsonify({"error": "Driver not found"})

    def put(self, driver_id):
        try:
            driver = db.session.query(Driver).filter(Driver.id == driver_id).one()
            if request.json.get('first_name'):
                driver.first_name = request.json['first_name']
            if request.json.get('last_name'):
                driver.last_name = request.json['last_name']
            db.session.commit()
            return Response(status=200)
        except:
            return jsonify({"error": "Driver not found"})

    def delete(self, driver_id):
        try:
            driver = db.session.query(Driver).filter(Driver.id == driver_id).one()
            db.session.delete(driver)
            db.session.commit()
            return Response(status=200)
        except:
            return jsonify({"error": "Driver not found"})


class AllVehicles(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('with_drivers', type=str)
        args = parser.parse_args()
        if args['with_drivers'] == 'yes':
            vehicles = db.session.query(Vehicle).filter(Vehicle.driver_id.is_not(None)).all()
        elif args['with_drivers'] == 'no':
            vehicles = db.session.query(Vehicle).filter(Vehicle.driver_id.is_(None)).all()
        else:
            vehicles = db.session.query(Vehicle).all()
        return jsonify(vehicles)

    def post(self):
        vehicle = Vehicle(make=request.json.get('make'),
                          model=request.json.get('model'),
                          plate_number=request.json.get('plate_number'))
        db.session.add(vehicle)
        db.session.commit()
        return Response(status=200)


class Vehicles(Resource):
    def get(self, vehicle_id):
        vehicle = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()
        return jsonify(vehicle)

    def put(self, vehicle_id):
        try:
            vehicle = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()
            for param in ('make', 'model', 'plate_number'):
                if request.json.get(param):
                    setattr(vehicle, param, request.json[param])
            db.session.commit()
            return Response(status=200)
        except:
            return jsonify({"error": "car not found"})

    def post(self, vehicle_id):
        vehicle = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()
        if request.json.get('driver_id'):
            driver = int(request.json['driver_id'])
            exists = db.session.query(Driver).filter(Driver.id == driver).count()
            if exists > 0:
                vehicle.driver_id = request.json['driver_id']
                db.session.commit()
                return Response(status=200)
            return jsonify({"error": "Driver does not exists"})
        vehicle.driver_id = None
        db.session.commit()
        return Response(status=200)

    def delete(self, vehicle_id):
        try:
            vehicle = db.session.query(Vehicle).filter(Vehicle.id == vehicle_id).one()
            db.session.delete(vehicle)
            db.session.commit()
            return Response(status=200)
        except:
            return jsonify({"error": "car not found"})
