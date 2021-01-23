from flask_bcrypt import Bcrypt

flask_bcrypt = Bcrypt()


class PasswordHash:
    def __init__(self, hash):
        self.hash = hash

    def __eq__(self, potential):
        return flask_bcrypt.check_password_hash(self.hash, potential)

    @classmethod
    def from_password(cls, password):
        return cls(flask_bcrypt.generate_password_hash(password))
