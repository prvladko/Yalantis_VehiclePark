from app import db
from sqlalchemy.sql import func
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Driver(db.Model):
    id: int
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())


@dataclass
class Vehicle(db.Model):
    id: int
    driver_id: int
    make: str
    model: str
    plate_number: str
    created_at: datetime
    updated_at: datetime

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    make = db.Column(db.String(4))
    model = db.Column(db.String(120))
    plate_number = db.Column(db.String(8))
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
