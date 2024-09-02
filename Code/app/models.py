from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Trade(db.Model):
    id = db.Column(db.String, primary_key=True)
    buyer = db.Column(db.String, nullable=False)
    seller = db.Column(db.String, nullable=False)
    item = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Cargo(db.Model):
    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    expected_delivery = db.Column(db.DateTime, nullable=False)

class Inventory(db.Model):
    station_id = db.Column(db.String, primary_key=True)
    item_id = db.Column(db.String, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

class Event(db.Model):
    id = db.Column(db.String, primary_key=True)
    event_type = db.Column(db.String, nullable=False)
    trade_id = db.Column(db.String, db.ForeignKey('trade.id'), nullable=True)
    cargo_id = db.Column(db.String, db.ForeignKey('cargo.id'), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
