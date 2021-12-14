class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
    # Чтоб не выводило предупреждение при запуске сервера
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_ECHO = True


# class TestConfiguration(object):
#     DEBUG = True
#     SECRET_KEY = 'TEST_SECRET_SECRET_KEY'
#     # Чтоб не выводило предупреждение при запуске сервера
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
#