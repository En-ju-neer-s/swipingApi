from flask import Blueprint, request
from flask_pymongo import MongoClient

user_route = Blueprint('user_route', __name__)

# the client to whe we connect
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper
collection = db.users

# Post/get route acceser
@user_route.route('/', methods=['GET', 'POST'])
def userCreate():
    if request.method == 'POST':

        # Check if object is complete
        if request.json['username'] and type(request.json['username']) == str:
            if collection.find({'user': request.json['username']}).count != 0:
                return 'Username bestaat al', 400
            else:
                userObject = request.json
                userObject['strikes'] = 0
                userObject['seenTitles'] = []
                userObject['id'] = request.json['id']

                collection.insert_one(userObject)
                return 'success', 201
        else:
            return 'POST REQUEST KLOPT NIET', 400
    else:
        return 'Welcome to the post user'
