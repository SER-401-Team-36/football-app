import csv
from flask import Blueprint
from app.models import db
from app.models.player import Player

import_players_bp = Blueprint('import-players', __name__, cli_group=None)


@import_players_bp.cli.command("import-players")
def import_players():
    """Uploads players from a local players.csv into the db"""
    with open("players.csv", newline='', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            player = Player(
                name=row["player_name"],
                position=row["pos"],
                team=row["team"],
                projection=row["projection"]
            )
            db.session.add(player)
    db.session.commit()
