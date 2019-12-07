from flask import Blueprint, request
from bson.json_util import dumps
from .connection import client

fake_route = Blueprint('fake_route', __name__)

# Connect to collection
db = client.swiper


@fake_route.route('/', methods=['GET', 'POST'])
def fakeRoute():
    if request.method == 'GET':
        fakeTitles = db.fakeTitles.find().sort('primary_key', 1)
        return dumps(fakeTitles)
