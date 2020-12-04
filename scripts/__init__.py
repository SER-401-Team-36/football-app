from scripts.import_players import import_players_bp
from scripts.calculate_derived_values import calculate_derived_values_bp


def register_scripts(app):
    app.register_blueprint(import_players_bp)
    app.register_blueprint(calculate_derived_values_bp)
