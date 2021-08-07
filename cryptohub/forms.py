from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, SelectField
from wtf.validators import DataRequired, Length

class SpotTradeForm(FlaskForm):
    date = DateField('Date Executed', format='%d-%m-%Y', validators=[DataRequired()], default=datetime.utcnow())
    type = SelectField('Type', choices=['Buy', 'Sell', 'Stake'], default='Buy')


class PerpetualTradeForm(FlaskForm):
    date = DateField('Date Executed', format='%d-%m-%Y', validators=[DataRequired()], default=datetime.utcnow())
    type = SelectField('Type', choices=['Long', 'Short'], default='Long')
