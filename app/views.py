from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from app import app

@app.route('/')
def index():
    return render_template('index.html');