import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  db = SQLAlchemy(app)
  migrate = Migrate(app, db)

  @app.route('/hello')
  def hello():
    return "Hello, World!"

  return app