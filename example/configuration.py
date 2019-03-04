import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/todos_dev'
    DESTROY_ON_CLOSE = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/todos_prod'


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = True
    DESTROY_ON_CLOSE = True


class TestingConfig(Config):
    TESTING = True


def get_config():
    if os.getenv('FLASK_MODE') == 'PRODUCTION':
        return ProductionConfig
    else:
        return DevelopmentConfig
