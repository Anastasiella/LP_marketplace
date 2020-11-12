from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class CartForm(FlaskForm):
    submit = SubmitField('оформить заказ', render_kw={"class": "btn btn-primary"})
    cancel= SubmitField('отменить заказ', render_kw={"class": "btn btn-primary"})

class CartItemForm(FlaskForm):
    delete = SubmitField('удалить', render_kw={"class": "btn btn-primary"})



