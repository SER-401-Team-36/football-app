from app.models.user import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()

    if (user is not None and user.password == password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return User.query.filter_by(id=user_id)
