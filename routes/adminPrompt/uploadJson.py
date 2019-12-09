from flask import Blueprint
from ..connection import client
from bson.json_util import dumps

upload_route = Blueprint('upload_route', __name__)  # set route

# connect to DB
db = client.swiper


@upload_route.route('/upload', methods=['post'])
def uploadRoute():
    return 'is working'
