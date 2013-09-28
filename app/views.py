from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/about_us')
def about_us():
    return render_template('about_us.html');
