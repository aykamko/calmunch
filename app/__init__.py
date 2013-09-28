from flask import Flask, url_for

application = Flask(__name__)
app = application

from app import views
