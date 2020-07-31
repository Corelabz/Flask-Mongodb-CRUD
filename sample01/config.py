class Config(object):
	# Application settings
	APP_NAME = "Sample01"
	SECRET_KEY = 'corelabz-sample01'

	# Flask settings

	DEBUG = False
	TESTING = False


	# MongoDB Config
	MONGODB_DB = 'sample01'
	MONGODB_HOST = 'localhost'
	MONGODB_PORT = 27017

class ProductionConfig(Config):
	MONGODB_DB = 'sample'

class DevelopmentConfig(Config):
	DEBUG = True
	TESTING = True

class TestingConfig(Config):
	DEBUG = True
	TESTING = True