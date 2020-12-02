from flask import Blueprint
from app.models import db
from app.models.player import Player

calculate_derived_values_bp = Blueprint(
    'calculate-derived-values',
    __name__,
    cli_group=None
)


@calculate_derived_values_bp.cli.command("calculate-derived-value")
def calculate_derived_values():
    players = Player.query.all()

    for player in players:
        total = 0
        for projection in player.projections:
            total += projection.points
        player.average_projection = round(total / len(player.projections), 3)

    # Calculate player groupings here

    db.session.commit()
