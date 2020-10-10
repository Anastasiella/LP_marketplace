from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
import pathlib
from os.path import dirname

# Update root path for project
sys.path.append(dirname(pathlib.Path(__file__).parent))

from marketplace import app
from marketplace.db import db


app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
