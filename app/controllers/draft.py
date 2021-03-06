from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required

from app.models import db
from app.models.user import User
from app.models.draft import Draft
from app.models.player import Player
from app.models.associations.player_draft_user import PlayerDraftUser

drafts = Blueprint('drafts', __name__, url_prefix='/draft')


@drafts.route('', methods=['POST'])
@jwt_required
def create_draft():
    body = request.json
    user = User.query.filter_by(id=body['user_id']).first()

    draft = Draft(user=user)

    db.session.add(draft)
    db.session.commit()

    return jsonify({"id": draft.id}), 201


@drafts.route('/<int:draft_id>/player', methods=['POST'])
@jwt_required
def add_user_to_draft(draft_id):
    body = request.json
    user_id = body.get('user_id')
    player_id = body.get('player_id')

    player = Player.query.filter_by(id=player_id).first()
    draft = Draft.query.filter_by(id=draft_id).first()

    association = PlayerDraftUser(player=player, draft=draft)
    if (user_id is not None):
        user = User.query.filter_by(id=user_id).first()
        association.user = user

    db.session.add(association)
    db.session.commit()

    return Response(status=200)


@drafts.route('/<int:draft_id>/reset', methods=['POST'])
@jwt_required
def reset_draft(draft_id):
    draft = Draft.query.filter_by(id=draft_id).first()

    for player_draft_user in draft.player_users:
        db.session.delete(player_draft_user)

    db.session.commit()

    return Response(status=200)
