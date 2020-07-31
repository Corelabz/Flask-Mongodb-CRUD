from flask import Flask 
from flask_mongoengine import MongoEngine

from .config import DevelopmentConfig

db = MongoEngine()

def create_app():
	app = Flask(__name__)
	app.config.from_object(DevelopmentConfig())

	db.init_app(app)

	from .backend import backend
	from .front import front

	app.register_blueprint(backend)
	app.register_blueprint(front)

	return app