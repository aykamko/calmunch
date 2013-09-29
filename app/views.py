from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from app import app
from app.models import Event
from app.database import db_session

@app.route('/')
def index():
  event_query = db_session.query(Event).all()
  return render_template('index.html', event_query = event_query);

@app.route('/about_us')
def about_us():
    return render_template('about_us.html');
