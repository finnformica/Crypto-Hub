from flask import render_template, url_for, flash, redirect, request
from cryptohub import app, db, bcrypt
from cryptohub.forms import RegistrationForm, LoginForm, SpotTradeForm, PerpetualTradeForm
from cryptohub.models import User, Spot, Perpetual
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have been logged in', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/spot', methods=['GET', 'POST'])
@login_required
def spot():
    form = SpotTradeForm()
    if form.validate_on_submit():
        flash('Spot trade logged.', 'success')
        spot_trade = Spot(
                        date=form.date.data,
                        ticker1=form.ticker1.data,
                        ticker2=form.ticker2.data,
                        type=form.type.data,
                        price=form.price.data,
                        quantity=form.quantity.data,
                        fee_quantity=form.fee_quantity.data,
                        fee_currency=form.fee_currency.data)
        db.session.add(spot_trade)
        db.session.commit()
        # return redirect(url_for('spot'))
    return render_template('spot.html', form=form)

@app.route('/perpetual', methods=['GET', 'POST'])
@login_required
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
                            notes=form.notes.data)
        db.session.add(perpetual_trade)
        db.session.commit()
    return render_template("perpetual.html", form=form)

@app.route('/charts')

def charts():
    return render_template('charts.html')

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')
