import datetime
import argon2
from hashlib import sha256
from argon2 import PasswordHasher, verify_password
from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

ph = PasswordHasher()
login_route = Blueprint('login_route', __name__)

# Connect to swiper
db = client.swiper

# This route is to make a api key
@login_route.route('/login', methods=['POST'])
def loginRoute():
    # TODO SET IN MONGODB
    if db.authUsers.find({'username': request.json['username']}):

        # Check if user is correct in DB
        try:
            ph.verify(db.authUsers.find_one({'username': request.json['username']}, {'password': 1, '_id': 0})['password'], request.json['password'])

        except argon2.exceptions.VerifyMismatchError:
            return dumps({'success': False, 'message': 'Credits are not correct!'}), 300

        time = datetime.datetime.utcnow()
        apiKey = request.json['username'] + format(time.hour) + format(time.minute) + format(time.second) + format(time.microsecond)

        # Set collection
        collection = db.apiKey

        collection.create_index('inserted at: ' + format(datetime.datetime.utcnow()), expireAfterSeconds=60)
        collection.insert_one({'apiKey': apiKey, 'user': request.json['username'], "inserted": datetime.datetime.utcnow()})

        return dumps({'success': True, 'message': 'You are logged in', 'apiKey': 'apikey'}), 200
    else:
        return dumps({'success': False, 'message': 'Username not valid or username not filled in'}), 404
