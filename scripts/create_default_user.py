from flask import Blueprint
from app.models import db
from app.models.user import User

create_default_user_bp = Blueprint(
    'create-default-user',
    __name__,
    cli_group=None
)


@create_default_user_bp.cli.command("create-default-user")
def create_default_user():
    print('looking for default user...')
    user = User.query.filter_by(email='user').first()

    if user is None:
        user = User(email='user', password='password')
        db.session.add(user)
        db.session.commit()
        print('creating default user...')
    else:
        print('user found. skipping create.')
