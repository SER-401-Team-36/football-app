from flask import Blueprint, request, Response, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
import os

upload = Blueprint("upload", __name__, url_prefix="/upload")



@upload.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":

        if request.files:

            file = request.files["file"]

            file.save(os.path.join('../football-app', file.filename))

            print("Saved")

            return redirect(request.url)

    return "The item has been saved"
    