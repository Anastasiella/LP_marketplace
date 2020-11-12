from marketplace.db import db
from sqlalchemy.orm import relationship
from webapp.goods.models import Good

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_finished = db.Column(db.Boolean, default=False)
    
    buyer = relationship("User", back_populates="cart")
    

    def __init__(self, id, buyer_id, is_finished):
        self.id = id
        self.buyer_id = buyer_id
        self.is_finished = is_finished
        
    def __repr__(self):
        return f'<Cart {self.id}>' 

class CartItem(db.Model):
    __tablename__ = 'cartitem'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    good_id = db.Column(db.Integer, db.ForeignKey(Good.good_id))
    quantity = db.Column(db.Integer)
       
    cart = relationship("Cart", back_populates="cart_items")
    goods = relationship("Good", back_populates="cart_items")

       
    def __repr__(self):
        return f'<CartItem {self.id}>' 