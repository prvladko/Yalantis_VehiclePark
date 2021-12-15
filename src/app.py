from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(Configuration):
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    api = Api(app)

    import src.views as views
    api.add_resource(views.AllDrivers, '/drivers/driver/')
    api.add_resource(views.Drivers, '/drivers/driver/<int:id>')
    api.add_resource(views.AllVehicles, '/vehicles/vehicle/')
    api.add_resource(views.Vehicles, '/vehicles/vehicle/<int:id>')
    api.add_resource(views.Home, '/')
    return app
