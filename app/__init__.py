from flask import Flask, url_for
import os

application = Flask(__name__)
app = application

app.config.from_object('config')

env = 'Local'
if os.environ.get('LIVE'):
    env = 'Live'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_SILVER_URL']

from database import db_session
from app import views
