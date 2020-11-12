from scripts.import_players import import_players_bp


def register_scripts(app):
    app.register_blueprint(import_players_bp)
