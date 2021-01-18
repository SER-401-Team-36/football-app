from flask import Blueprint, request, Response
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
