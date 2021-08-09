from flask import render_template, url_for, flash, redirect, current_user
from cryptohub import app
from cryptohub.forms import SpotTradeForm, PerpetualTradeForm
from cryptohub.models import User, Spot, Perpetual

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/spot')
def spot():
    form = SpotTradeForm()
    if form.validate_on_submit():
        flash(f'Spot trade logged.', 'success')
        spot_trade = Spot(
                        date=form.date.data,
                        ticker1=form.ticker1.data,
                        ticker2=form.ticker2.data,
                        type=form.type.data,
                        price=form.price.data,
                        quantity=form.quantity.data,
                        fee_quantity=form.fee_quantity.data,
                        fee_currency=form.fee_currency.data,
                        user_id=current_user.id)
        db.session.add(spot_trade)
        db.session.commit()
        # return redirect(url_for('spot'))
    return render_template('spot.html', form=form)

@app.route('/perpetual')
def perpetual():
    form = PerpetualTradeForm()
    if form.validate_on_submit():
        perpetual_trade = Perpetual(
                            date=form.date.data,
                            ticker1=form.ticker1.data,
                            ticker2=form.ticker2.data,
                            type=form.type.data,
                            leverage=form.leverage.data,
                            balance=form.balance.data,
                            percent_risked=form.percent_risked.data,
                            entry_price=form.entry_price.data,
                            stop_loss=form.entry_price.data,
                            take_profit=form.take_profit.data,
                            exit_price=form.exit_price.data,
                            notes=form.notes.data,
                            user_id=current_user.id)
        db.session.add(perpetual_trade)
        db.session.commit()
    return render_template("perpetual.html", form=form)

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
