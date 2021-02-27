from sqlalchemy.orm import validates
from . import db
from app.models.password import Password, PasswordHash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(Password, nullable=False)
    players = db.Column(db.Array) #is this the right way to do this?

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

    @validates('password')
    def validate_password(self, key, password):
        if (isinstance(password, PasswordHash)):
            return password

        return PasswordHash.from_password(password)
