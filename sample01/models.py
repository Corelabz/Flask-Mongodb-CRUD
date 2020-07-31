from . import db

class County(db.Document):
	name = db.StringField(max_length=80, unique=True)
	year = db.StringField()
	amount = db.DecimalField()