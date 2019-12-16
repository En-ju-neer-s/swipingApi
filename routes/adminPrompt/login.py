import datetime
from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

login_route = Blueprint('login_route', __name__)

# Connect to swiper
db = client.swiper

# This route is to make a api key
@login_route.route('/login', methods=['POST'])
def loginRoute():
    # request.json['testing']
    # argon2 hashing
    # TODO SET IN MONGODB
    if 1
       if 1:
            apiKey = 'je kleine pienel'

            collection = db.apiKey

            collection.create_index('inserted', expireAfterSeconds=10)
            collection.insert_one({'apiKey': apiKey, "inserted": datetime.datetime.utcnow()})

            return dumps({'success': True, 'message': 'You are logged in', 'apiKey': apiKey})
        else:
            return dumps({'success': False, 'message': 'Credits are not correct!'})
