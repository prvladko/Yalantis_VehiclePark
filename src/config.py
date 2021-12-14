class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    # So that it would not display a warning when starting the server
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'