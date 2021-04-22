from scripts.import_players import import_players_bp
from scripts.calculate_derived_values import calculate_derived_values_bp
from scripts.create_default_user import create_default_user_bp


def register_scripts(app):
    app.register_blueprint(import_players_bp)
    app.register_blueprint(calculate_derived_values_bp)
    app.register_blueprint(create_default_user_bp)
