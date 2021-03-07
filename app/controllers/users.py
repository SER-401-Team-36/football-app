from flask import Blueprint, request, Response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models import db

users = Blueprint("users", __name__, url_prefix="/user")


@users.route('', methods=['POST'])
def create_user():
    body = request.json
    email = body["email"]
    password = body["password"]

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return Response(status=201)


@users.route('/current', methods=['get'])
@jwt_required
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).one()

    return jsonify(user.as_dict())
