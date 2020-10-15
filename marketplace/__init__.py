from flask import Flask
from marketplace.db import db

from marketplace.category.views import category_blueprint
from marketplace.general.views import general_blueprint


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(category_blueprint, url_prefix='/category')
app.register_blueprint(general_blueprint, url_prefix='/')



if __name__ == "__main__":
    app.run()
