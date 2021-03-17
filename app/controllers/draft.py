from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import db
from app.models.user import User
from app.models.draft import Draft
from app.models.player import Player
from app.models.associations.player_draft_user import PlayerDraftUser

drafts = Blueprint('drafts', __name__, url_prefix='/draft')


@drafts.route('', methods=['POST'])
@jwt_required
def create_draft():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    draft = Draft(user=user)
    db.session.add(draft)
    db.session.commit()

    return jsonify({"id": draft.id}), 201


@drafts.route('', methods=['GET'])
@jwt_required
def find_draft():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if (len(user.drafts) == 0):
        return Response(status=404)

    draft = user.drafts[0]

    return jsonify({"id": draft.id}), 200


@drafts.route('/<int:draft_id>/player', methods=['POST'])
@jwt_required
def add_user_to_draft(draft_id):
    user_id = get_jwt_identity()
    for_user = request.args.get('for_user')
    body = request.json
    player_id = body.get('player_id')

    player = Player.query.filter_by(id=player_id).first()
    draft = Draft.query.filter_by(id=draft_id).first()

    association = PlayerDraftUser(player=player, draft=draft)
    if (for_user is not None):
        user = User.query.filter_by(id=user_id).first()
        association.user = user

    db.session.add(association)
    db.session.commit()

    return Response(status=200)


@drafts.route('/<int:draft_id>/player', methods=['GET'])
@jwt_required
def find_draft_players(draft_id):
    user_id = get_jwt_identity()

    user = User.query.filter_by(id=user_id).first()
    draft = next(
        (draft for draft in user.drafts if draft.id == draft_id),
        None
    )

    if (draft is None):
        return Response(status=400)

    user_draft_players = [
        {
            **player_user.player.as_dict(),
            'available': False,
            'user_id': user.id
        } for player_user in
        draft.player_users if
        player_user.user is not None
    ]

    non_user_draft_players = [
        {
            **player_user.player.as_dict(),
            'available': False,
            'user_id': None
        } for player_user in
        draft.player_users if
        player_user.user is None
    ]

    available_players = [
        {
            **player.as_dict(),
            'available': True,
            'user_id': None
        } for player in
        Player.query.all() if
        player.id not in [player['id'] for player in user_draft_players] and
        player.id not in [player['id'] for player in non_user_draft_players]
    ]

    return jsonify(
        user_draft_players + non_user_draft_players + available_players
    )


@drafts.route('/<int:draft_id>/player/recommended', methods=['GET'])
@jwt_required
def get_recommended_draft_player(draft_id):
    pos = request.args.get('position')
    draft = Draft.query.filter_by(id=draft_id).first()

    taken_player_ids = list(map(
        lambda player_user: player_user.player_id, draft.player_users
        ))

    query = (
              Player
              .query
              .filter(Player.id.notin_(taken_player_ids))
              .order_by(Player.average_projection.desc())
            )

    if pos:
        query = query.filter_by(position=pos.upper())

    return jsonify(query.first().as_dict())


@drafts.route('/<int:draft_id>/reset', methods=['POST'])
@jwt_required
def reset_draft(draft_id):
    draft = Draft.query.filter_by(id=draft_id).first()

    for player_draft_user in draft.player_users:
        db.session.delete(player_draft_user)

    db.session.commit()

    return Response(status=200)
