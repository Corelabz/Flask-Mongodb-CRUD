from flask_wtf import FlaskForm 
from wtforms import validators, StringField, IntegerField, DecimalField

class CountyForm(FlaskForm):
	name = StringField('County Name', [validators.DataRequired()])
	year = StringField('Financial Year', [validators.DataRequired()])
	amount = DecimalField('Amount Allocated', [validators.DataRequired()])