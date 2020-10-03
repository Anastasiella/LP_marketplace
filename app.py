from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from models import User, Category, Product


@app.route('/')
def get_index():
    #all_category = Category.query.all()
    #for i in all_category:
       # print(i)
    all_category = Category.query.with_entities(Category.name, Category.image).all()
    return render_template('index.html', categories=all_category)


@app.route('/items/', methods=['GET'], strict_slashes=False)
def get_items():
    return render_template('items.html')

