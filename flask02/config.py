import os

class Config:
    ENV='Development'
    DEBUG = True
    WORKDIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{WORKDIR}/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False