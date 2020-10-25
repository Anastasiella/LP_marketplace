from marketplace.db import db


class Goods(db.Model):
    __tablename__ = 'goods'

    good_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    image_path = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)

    def __init__(self, good_id, name, description, price, quantity, created_at, image_path, category_id):
        self.good_id = good_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.created_at = created_at
        self.image_path = image_path
        self.category_id = category_id

    def __repr__(self):
        return f'<Good {self.good_id}>'
