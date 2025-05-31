import os
from zoneinfo import ZoneInfo
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FRONTEND_URL = os.getenv('FRONTEND_URL')

    ## DATABASE ##
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_HOST = os.getenv('DB_HOST')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')

    ## MAIL KEYS ##
    MAIL_API_KEY = os.getenv('MAIL_API_KEY')
    MAIL_SECRET_KEY = os.getenv('MAIL_SECRET_KEY')

    ## JWT KEYS ##
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')