from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.models.user import User

authenticate = Blueprint('authenticate', __name__)


@authenticate.route('/auth', methods=['POST'])
def authenticate_user():
    body = request.json
    email = body["email"]
    password = body["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg": "Invalid user"}), 400

    if user.password != password:
        return jsonify({"msg": "Invalid email or password"}), 401

    return jsonify(access_token=create_access_token(identity=user.id))
