from flask import Blueprint, render_template, flash, redirect, url_for
from marketplace.cart.models import Cart, CartItem
from marketplace import db


cart_blueprint = Blueprint('cart', __name__, template_folder='templates')

# создание заказа
@cart_blueprint.route('/')
def cart():
    title = "Корзина"
    return render_template('cart/cart.html', page_title=title)

