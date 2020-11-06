import os

from flask import Flask
from flask_migrate import Migrate
from app.models import db

from app.controllers.players import players


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object("app.config.Config")
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(players)

    return app
