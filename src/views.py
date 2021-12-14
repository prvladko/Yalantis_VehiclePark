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

        id = db_methods.add_driver(first_name, last_name, created_at, updated_at)
        return {"message": {'id': id, 'first_name': first_name, 'last_name': last_name,
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
            updated_at = transfer_date(args['updated_at'])
        except ValueError as e:
            return {"message": {
                "updated_at": f'{e}\nThe date must be in the format: "%d-%m-%Y"\n Example: "14-12-2021"'}}, 400

        id = db_methods.add_vehicle(make, model, plate_number, created_at, updated_at)
        return {"message": {'id': id, 'make': make, 'model': model, 'plate_number': plate_number,
                            'created_at': str(created_at), 'updated_at': str(updated_at)}}, 201