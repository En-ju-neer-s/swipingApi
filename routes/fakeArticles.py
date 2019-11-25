from flask import Blueprint, request
from flask_pymongo import MongoClient
from bson.json_util import dumps

fake_route = Blueprint('fake_route', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.swiper


@fake_route.route('/', methods=['GET', 'POST'])
def fakeRoute():
    if request.method == 'GET':
        fakeTitles = db.fakeTitles.find().sort('primary_key', 1)
        return dumps(fakeTitles)
