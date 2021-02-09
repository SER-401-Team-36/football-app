from app.models import db
from app.models.mixins.timestamps import HasTimestamps


class Projection(HasTimestamps, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Float)
    player_id = db.Column(
        db.Integer,
        db.ForeignKey('player.id'),
        nullable=False
    )

    def __repr__(self):
        return f"<Player {self.position} {self.name}>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
