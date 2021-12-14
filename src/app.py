from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# from src.config import Configuration

db = SQLAlchemy()


def create_app(Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    api = Api(app)

    import src.views as views
    api.add_resource(views.CreateDriver, '/drivers/driver/')
    api.add_resource(views.CreateVehicle, '/vehicles/vehicle/')
    api.add_resource(views.Driver, '/drivers/driver/<driver_id>/')
    api.add_resource(views.Vehicle, '/vehicles/vehicle/<vehicle_id>')
    api.add_resource(views.Drivers, '/drivers/driver/')
    api.add_resource(views.Vehicles, '/vehicles/vehicle/')

    api.add_resource(views.FindDriver, '/drivers/driver/search')
    # api.add_resource(views.FindVehicle, '/vehicles/vehicle/search')  # no need, just for test

    api.add_resource(views.Home, '/')

    return app
