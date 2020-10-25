from flask import Blueprint, render_template, jsonify, abort, current_app
from marketplace.goods.models import Goods
from flask_paginate import Pagination, get_page_args


goods_blueprint = Blueprint('goods', __name__, template_folder='templates')


def get_items_per_page(items_result, offset=0, per_page=20):
    """
    :param items_result: result of select db
    :param offset: from 0 by default
    :param per_page: show item on page, default from config.py value PAGE_ON_VIEWS
    :return: slice of select result
    """
    return items_result[offset: offset + per_page]


@goods_blueprint.context_processor
def goods_processor():
    def convert_data_to_hr_format(date_of_item):
        return date_of_item.strftime("%Y-%m-%d %H:%M:%S")
    return dict(convert_data_to_hr_format=convert_data_to_hr_format)


@goods_blueprint.route('/<int:category_id>', methods=['GET'], strict_slashes=False)
def get_product_by_category(category_id):
    goods_result = Goods.query.filter_by(category_id=category_id).all()

    # тут надо получать данные из нашего конфига app.config['PAGES_ON_VIEW'],
    # но сделать from marketplace import app не работает.
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page=current_app.config['PAGES_ON_VIEW'])

    good_items = get_items_per_page(goods_result, offset=offset, per_page=per_page)
    total_goods = len(goods_result)

    pagination = Pagination(page=page, per_page=per_page, total=total_goods,
                            css_framework='bootstrap4')
    return render_template('goods/good_list.html',
                           items=good_items,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
