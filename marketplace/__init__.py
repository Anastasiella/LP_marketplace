from flask import Flask
from flask_login import LoginManager, current_user, login_user, login_required, logout_user, UserMixin

from marketplace.db import db

from marketplace.category.views import category_blueprint
from marketplace.general.views import general_blueprint
from marketplace.user.views import user_blueprint

from marketplace.user.models import User


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(category_blueprint, url_prefix='/category')
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(general_blueprint, url_prefix='/')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run()
