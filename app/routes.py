from flask import render_template, url_for
from app import app

@app.route("/home")
def home():
    return render_template('home.html')
