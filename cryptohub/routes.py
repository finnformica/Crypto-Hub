from flask import render_template, url_for, flash, redirect
from cryptohub import app
# from forms import SpotTradeForm, PerpetualTradeForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spot')
def spot():
    return render_template('spot.html')

@app.route('/perpetual')
def perpetual():
    return render_template("perpetual.html")

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
