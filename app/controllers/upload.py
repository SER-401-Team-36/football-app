from flask import Blueprint, request, Response, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from werkzeug.utils import secure_filename
import os

upload = Blueprint("upload", __name__, url_prefix="/upload")


def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit("." , 1)[1]

    if ext.upper() in ["CSV"]:
        return True
    else:
        return False

@upload.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == "POST":

        if request.files:

            file = request.files["file"]

            if file.filename== "":
                print("You must name the file")
                return redirect(request.url)

            if not allowed_file(file.filename):
                print("File type not allowed")
                return redirect(request.url)

            else:
                filename = secure_filename(file.filename)
                
                file.save(os.path.join('../football-app', filename))
                

            print("Saved")

            return redirect(request.url)

    return redirect("http://localhost:3000/Upload")
    