from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import db
from scripts import register_scripts

from app.controllers.players import players


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_object("app.config.Config")
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(players)

    register_scripts(app)

    return app
