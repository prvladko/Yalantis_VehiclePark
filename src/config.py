import os
from dotenv import load_dotenv

load_dotenv()


class ProdConfiguration(object):
    SECRET_KEY = os.getenv('secret_key')
    # To avoid displaying a warning when the server starts
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///drivers.db'


class TestConfiguration(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
