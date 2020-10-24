from flask import Blueprint, render_template, jsonify, abort
from marketplace.goods.models import Goods


goods_blueprint = Blueprint('goods', __name__, template_folder='templates')


@goods_blueprint.route('/<int:category_id>', methods=['GET'], strict_slashes=False)
def get_product_by_category(category_id):
    goods = Goods.query.filter_by(category_id=category_id).all()
    return render_template('goods/good_list.html', test=goods)