# -*- coding: utf-8 -*-

from app import app, api, db
from models import Driver, Vehicle
import views

api.add_resource(views.CreateDriver, '/drivers/driver/')
api.add_resource(views.CreateVehicle, '/vehicles/vehicle/')
api.add_resource(views.Driver, '/drivers/driver/<driver_id>/')
api.add_resource(views.Vehicle, '/vehicles/vehicle/<vehicle_id>')
api.add_resource(views.Drivers, '/drivers/driver/')
api.add_resource(views.Vehicles, '/vehicles/vehicle/')


if __name__ == '__main__':
    db.create_all()
    app.run()