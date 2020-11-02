import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db

from app.models.player import Player


def create_app(test_config=None):
  app = Flask(__name__)

  if test_config is None:
    app.config.from_object('app.config.Config')
  else:
    app.config.from_mapping(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  db.init_app(app)
  migrate = Migrate(app, db)

  @app.route('/hello')
  def hello():
    return "Hello, World!"

  return app