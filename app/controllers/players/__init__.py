from flask import Blueprint, jsonify, request
from sqlalchemy import desc
from app.models.player import Player

players = Blueprint("players", __name__, url_prefix="/players")


@players.route("/")
def get_players():
    pos = request.args.get('position')

    if pos:
        return jsonify([player.as_dict()for player in Player.query.filter_by(
            position=pos.upper()).order_by(desc('projection'))])
    else:
        return jsonify(
            [player.as_dict() for player in Player.query.all().order_by(
                desc('projection'))])
