import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_AUTH_USERNAME_KEY = 'email'
