from marketplace.db import db


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    image = db.Column(db.String(70))
    category_type = db.Column(db.String(15))

    def __init__(self, category_id, name, image, category_type):
        self.name = name
        self.category_id = category_id
        self.image = image
        self.category_type = category_type

    def __repr__(self):

        return f'<Category {self.category_id}>'


class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)

    def __init__(self, product_id, name, category_id):
        self.product_id = product_id
        self.name = name
        self.category_id = category_id

    def __repr__(self):
        return f'<Category {self.product_id}>'
