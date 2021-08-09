from datetime import datetime
from cryptohub import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    spots = db.relationship('Spot', backref='trader', lazy=True)
    perpetuals = db.relationship('Perpetual', backref='trader', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Spot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ticker1 = db.Column(db.String(5), nullable=False)
    ticker2 = db.Column(db.String(5), nullable=False)
    type = db.Column(db.String(4), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    fee_quantity = db.Column(db.Float, nullable=False)
    fee_currency = db.Column(db.String(5), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Spot('{self.ticker1}', '{self.ticker2}', '{self.type}', '{self.price}', '{self.date}')"


class Perpetual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ticker1 = db.Column(db.String(5), nullable=False)
    ticker2 = db.Column(db.String(5), nullable=False)
    type = db.Column(db.String(4), nullable=False)
    leverage = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    percent_risked = db.Column(db.Float, nullable=False)
    entry_price = db.Column(db.Float, nullable=False)
    stop_loss = db.Column(db.Float, nullable=False)
    take_profit = db.Column(db.Float, nullable=False)
    exit_price = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(250), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Perpetual('{self.ticker1}', '{self.ticker2}', '{self.type}', '{self.date}')"
