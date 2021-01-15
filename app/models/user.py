from . import db
from .password import Password


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = Password

    def __repr__(self):
        return f"<User {self.id} {self.email}>"
