class ProdConfiguration(object):
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    # To avoid displaying a warning when the server starts
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'


class TestConfiguration(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'