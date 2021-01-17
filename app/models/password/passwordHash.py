import bcrypt


class PasswordHash:
    def __init__(self, hash):
        self.hash = hash

    def __eq__(self, potential):
        return bcrypt.checkpw(self.hash, potential)

    @classmethod
    def from_password(cls, password):
        return cls(bcrypt.hashpw(password, bcrypt.gensalt()))
