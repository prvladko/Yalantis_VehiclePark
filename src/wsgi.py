# -*- coding: utf-8 -*-

from app import app, api, db
from models import Driver, Vehicle
import views

api.add_resource(views.CreateDriver, '/drivers/driver/')
api.add_resource(views.CreateVehicle, '/vehicles/vehicle/')
# api.add_resource(views.Catalog, '/<string:todo_id>')


if __name__ == '__main__':
    db.create_all()
    app.run()