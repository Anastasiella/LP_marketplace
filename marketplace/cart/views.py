from flask import Blueprint, render_template, flash, redirect, url_for
from webapp.cart.models import Cart, CartItem
from webapp import db


cart_blueprint = Blueprint('cart', __name__, url_prefix='/cart', template_folder='templates')

# создание заказа
@cart_blueprint.route('/')
def cart():
    title = "Корзина"
    return render_template('cart/cart.html', page_title=title)

