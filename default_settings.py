import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
# database+adapter://user:password@host:port/dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")
        if not value:
            raise ValueError("DB_URI is not set")
        return value

    @property
    def AWS_ACCESS_KEY_ID(self):
        value = os.environ.get("AWS_ACCESS_KEY_ID")
        if not value:
            raise ValueError("AWS_ACCESS_KEY_ID is not set")
        return value

    @property
    def AWS_SECRET_ACCESS_KEY_ID(self):
        value = os.environ.get("AWS_SECRET_ACCESS_KEY")
        if not value:
            raise ValueError("AWS_SECRET_ACCESS_KEY is not set")
        return value
    
    @property
    def AWS_S3_BUCKET(self):
        value = os.environ.get("AWS_S3_BUCKET")
        if not value:
            raise ValueError("AWS_S3_BUCKET is not set")
        return value
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_PROD_KEY")
        if not value:
            raise ValueError("JWT Production Key is not set")  
        return value

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
