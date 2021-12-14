from app import db
from datetime import datetime


class Driver(db.Model):
    __tablename__ = 'driver_data'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, primary_key=True)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return f'Driver>>> {self.first_name} {self.last_name}'


class Vehicle(db.Model):
    __tablename__ = 'vehicle_data'
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver_data.id'), unique=True)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    plate_number = db.Column(db.String(10), unique=True, nullable=False)  # example "AA 1234 OO"
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return f'Vehicle>>> {self.make} {self.model} {self.plate_number}'