from flask import Blueprint, render_template
from marketplace.category.models import Category


general_blueprint = Blueprint('general', __name__, template_folder='templates')


@general_blueprint.route('/')
def get_index():
    all_category = Category.query.with_entities(Category.name, Category.image, Category.category_id).all()
    return render_template('general/index.html', categories=all_category)

