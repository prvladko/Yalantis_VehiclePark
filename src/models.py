from src.app import db
from datetime import datetime


class Driver(db.Model):

    __tablename__ = 'drivers'  # may need changes

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    vehicle = db.relationship('Vehicle', backref='driver', uselist=False)
    #vehicle = db.Column(db.Integer, db.ForeignKey('vehicle_data.id'))

    def init(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = None
        self.updated_at = None

    def __repr__(self):
        return f'Driver id: {self.id}, First name: {self.first_name}, lastname: {self.first_name}, ' \
               f'created at: {self.created_at}, updated at: {self.updated_at}'


class Vehicle(db.Model):

    __tablename__ = 'vehicles'  # may need changes

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    make = db.Column(db.String(40), nullable=False)  # nullable?
    model = db.Column(db.String(80), nullable=False)
    plate_number = db.Column(db.String(10), unique=True, nullable=False)  # example "AA 1234 OO"
    created_at = db.Column(db.DateTime, default=datetime.now())  # server_default=db.func.now()
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def init(self, driver_id, make, model, plate_number):
        self.driver_id = driver_id
        self.make = make
        self.model = model
        self.plate_number = plate_number
        self.created_at = None
        self.updated_at = None

    def __repr__(self):
        return f'Driver id: {self.driver_id}, make: {self.make}, model: {self.model}, ' \
               f'plate number: {self.plate_number}, created at: {self.created_at},' \
               f'updated at: {self.updated_at}'