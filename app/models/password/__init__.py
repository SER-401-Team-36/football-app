from sqlalchemy.types import TypeDecorator, LargeBinary
from .passwordHash import PasswordHash


class Password(TypeDecorator):
    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        return value.hash

    def process_result_value(self, value, dialect):
        return PasswordHash(value)
