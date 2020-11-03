from . import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    position = db.Column(db.String())

    def __repr__(self):
        return f"<Player {self.position} {self.name}>"
