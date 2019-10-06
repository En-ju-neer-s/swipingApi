from flask import request, Blueprint, json
from bson.json_util import dumps
from flask_pymongo import MongoClient

title_route = Blueprint('title_route', __name__)

# connect with mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper
collection = db.testTitles


@title_route.route('/', methods=['GET', 'POST'])
def returnTitles():
    if request.method == 'GET':
        # print(collection.find({}))
        return dumps(collection.find({})), 200
