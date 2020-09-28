from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User


@app.route('/')
def get_index():
    return render_template('index.html', test_var="Zzzz")


@app.route('/items/<string:name>')
def get_items(name):
    return render_template('items.html', item_name=name)

