from sqlalchemy.orm import validates
from app.models import db
from app.models.password import Password, PasswordHash
from app.models.mixins.timestamps import HasTimestamps


class User(HasTimestamps, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(Password, nullable=False)

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }


    @validates('password')
    def validate_password(self, key, password):
        if (isinstance(password, PasswordHash)):
            return password

        return PasswordHash.from_password(password)
