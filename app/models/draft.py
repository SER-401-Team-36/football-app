from app.models import db
from app.models.user import User
from app.models.mixins.timestamps import HasTimestamps


class Draft(HasTimestamps, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship(User, backref="draft")

    def __repr__(self):
        return f"<Draft {self.id}>"
