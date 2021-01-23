from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.models.player import Player

players = Blueprint("players", __name__, url_prefix="/players")


@players.route("/")
@jwt_required
def get_players():
    pos = request.args.get('position')
    name_matcher = request.args.get('match_on_name')

    query = Player.query

    if pos:
        query = query.filter_by(
            position=pos.upper()
            )

    if name_matcher:
        query = query.filter(Player.name.ilike(f"%{name_matcher}%"))

    query = query.all()
    return jsonify([player.as_dict() for player in query])
