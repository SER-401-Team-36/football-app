from .. import db
from .passwordHash import PasswordHash


class Password(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value):
        return value.hash

    def process_result_value(self, value):
        return PasswordHash.from_password(value)