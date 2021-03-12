from app.models import db
from app.models.projection import Projection
from app.models.associations.player_draft_user import PlayerDraftUser
from app.models.mixins.timestamps import HasTimestamps
from sqlalchemy.inspection import inspect


class Player(HasTimestamps, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    team = db.Column(db.String)
    average_projection = db.Column(db.Float)

    projections = db.relationship(Projection, backref="player", lazy=True)
    draft_users = db.relationship(PlayerDraftUser, backref='player')

    def __repr__(self):
        return f"<Player {self.position} {self.name}>"

    def as_dict(self):
        all_projections = inspect(self.__table__.columns).relationship.items()
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
