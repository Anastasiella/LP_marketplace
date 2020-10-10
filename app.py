from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from models import User, Category, Product


@app.route('/')
def get_index():
    all_category = Category.query.with_entities(Category.name, Category.image, Category.category_id).all()
    return render_template('index.html', categories=all_category)


@app.route('/category/<int:category_id>', methods=['GET'], strict_slashes=False)
def get_product_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    for h in products:
        print(h.name)
    return render_template('category.html', test=products)

