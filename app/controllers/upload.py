from flask import Blueprint, request, Response, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from werkzeug.utils import secure_filename
import os
import glob
import csv
import requests
from array import array
from app.models import db
from app.models.player import Player
from app.models.projection import Projection
from app.models.associations.player_draft_user import PlayerDraftUser

upload = Blueprint("upload", __name__, url_prefix="/upload")

def import_players():
    csv_list = [glob.glob('*.csv')]

    print('Removing all current projections...')
    Projection.query.delete()
    PlayerDraftUser.query.delete()
    Player.query.delete()

    print('Adding from csv...')
    i=0
    while i < len(csv_list):
        for csv_path in csv_list[i]:
            print(f' - {csv_path}')
            with open(csv_path, newline='', encoding='utf-8-sig') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    add_projection(row)
                    calculate_derived_values()
            i+=1

    print('Committing changes')
    db.session.commit()

def calculate_derived_values():
    players = Player.query.all()

    for player in players:
        total = 0
        for projection in player.projections:
            total += float(projection.points)
        player.average_projection = round(total/len(player.projections), 3)

def add_projection(row):
    player = find_or_create_player(row)
    player.projections.append(
        Projection(points=row["projection"])
    )


def find_or_create_player(row):
    player = Player.query.filter_by(
        name=row["player_name"],
        position=row["pos"],
    ).first()

    if player is None:
        player = Player(
            name=row["player_name"],
            position=row["pos"],
            team=row["team"]
        )
        db.session.add(player)
    return player

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
                import_players()

            print("Saved")

            return redirect(request.url)

    return redirect("http://localhost:3000/Upload")

@upload.route('/delete', methods=['POST', 'GET'])
def delete_file():
    directory='../football-app'
    os.chdir(directory)
    files=glob.glob('*.csv')
    for filename in files:
        os.unlink(filename)
    return redirect("http://localhost:3000/Upload")