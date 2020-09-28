from app import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, user_id, name):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.user_id)
