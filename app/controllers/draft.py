from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.models import db
from app.models.user import User
from app.models.draft import Draft

drafts = Blueprint('drafts', __name__, url_prefix='/draft')


@drafts.route('/', methods=['POST'])
@jwt_required
def create_draft():
    body = request.json()
    user = User.query.filter_by(id=body['user_id'])

    draft = Draft(user=user)

    db.session.add(draft)
    db.session.commit()
