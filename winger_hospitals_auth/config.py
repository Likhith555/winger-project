import os

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:likhith@localhost/medinsight_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False