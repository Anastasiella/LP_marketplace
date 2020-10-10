from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from marketplace.category.models import Category, Product


category_blueprint = Blueprint('category', __name__, template_folder='templates')


@category_blueprint.route('/')
def get_index():
    all_category = Category.query.with_entities(Category.name, Category.image, Category.category_id).all()
    return render_template('category/index.html', categories=all_category)


@category_blueprint.route('/<int:category_id>', methods=['GET'], strict_slashes=False)
def get_product_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    for h in products:
        print(h.name)
    return render_template('category/category.html', test=products)
