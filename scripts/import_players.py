import csv
import requests
from flask import Blueprint
from app.models import db
from app.models.player import Player
from app.models.projection import Projection

import_players_bp = Blueprint('import-players', __name__, cli_group=None)


@import_players_bp.cli.command("import-players")
def import_players():
    """Uploads players from csv files and API into the db"""
    # All sources are expected to have the same column names:
    # player_name, pos, projection, team
    csv_list = ["espn_Players.csv", "fantasydata_players.csv"]
    api_list = ["https://www.fantasyfootballdatapros.com/api/projections"]

    print('Removing all current projections...')
    Projection.query.delete()

    print('Adding from csv...')
    for csv_path in csv_list:
        print(f' - {csv_path}')
        with open(csv_path, newline='', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                add_projection(row)

    print('Adding from apis...')
    for api_path in api_list:
        print(f' - {api_path}')
        response = requests.get(api_path)
        if response.status_code == 200:
            players = response.json()
            for player in players:
                add_projection(row=player)
    print('Committing changes')
    db.session.commit()


def add_projection(row):
    player = find_or_create_player(row)
    player.projections.append(
        Projection(points=row["projection"])
    )


def find_or_create_player(row):
    player = Player.query.filter_by(
        name=row["player_name"],
        position=row["pos"],
        team=row["team"]
    ).first()

    if player is None:
        player = Player(
            name=row["player_name"],
            position=row["pos"],
            team=row["team"]
        )
        db.session.add(player)
    return player
