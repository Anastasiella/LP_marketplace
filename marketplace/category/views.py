from flask import Flask, Blueprint, render_template, jsonify, abort
from marketplace.category.models import Category


category_blueprint = Blueprint('category', __name__, template_folder='templates')


@category_blueprint.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@category_blueprint.route('/<string:type_of_category>', methods=['GET'], strict_slashes=False)
def get_categories_by_type(type_of_category):
    category_items = None
    if type_of_category == 'frut':
        category_items = Category.query.with_entities(
            Category.name,
            Category.image,
            Category.category_id).filter(Category.category_type == "фрукты").all()
    elif type_of_category == 'veg':
        category_items = Category.query.with_entities(
            Category.name,
            Category.image,
            Category.category_id).filter(Category.category_type == "овощи").all()
    else:
        abort(404, description="Resource not found")

    return render_template('category/item.html', category_by_type=category_items)

