from app.models import db
from app.models.mixins.timestamps import HasTimestamps


class PlayerDraftUser(HasTimestamps, db.Model):
    player_id = db.Column(
        db.Integer,
        db.ForeignKey('player.id', ondelete='CASCADE'),
        primary_key=True,
    )
    draft_id = db.Column(
        db.Integer,
        db.ForeignKey('draft.id'),
        primary_key=True,
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
    )
