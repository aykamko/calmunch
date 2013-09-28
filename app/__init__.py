from flask import Flask, url_for

application = Flask(__name__)
app = application

from database import db_session
from app import views
