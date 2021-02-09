from app.models import db
from app.models.projection import Projection
from app.models.mixins.timestamps import HasTimestamps


class Player(HasTimestamps, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    team = db.Column(db.String)
    average_projection = db.Column(db.Float)
    projections = db.relationship(Projection, backref="player", lazy=True)

    def __repr__(self):
        return f"<Player {self.position} {self.name}>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
