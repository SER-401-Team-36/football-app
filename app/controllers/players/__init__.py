from flask import Blueprint, jsonify
from app.models.player import Player

players = Blueprint("players", __name__, url_prefix="/players")


@players.route("/")
def get_players():
    return jsonify(Player.query.all())
