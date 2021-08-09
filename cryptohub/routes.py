from flask import render_template, url_for, flash, redirect
from cryptohub import app
from cryptohub.forms import SpotTradeForm, PerpetualTradeForm
from cryptohub.models import User, Spot, Perpetual

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spot')
def spot():
    form = SpotTradeForm()
    if form.validate_on_submit():
        spot_trade = Spot(
                        date=form.date.data,
                        ticker1=form.ticker1.data,
                        ticker2=form.ticker2.data,
                        type=form.type.data,
                        price=form.price.data,
                        quantity=form.quantity.data,
                        fee_quantity=form.fee_quantity.data,
                        fee_currency=form.fee_currency.data)
    return render_template('spot.html', form=form)

@app.route('/perpetual')
def perpetual():
    return render_template("perpetual.html")

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
