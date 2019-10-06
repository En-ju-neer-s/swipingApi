# File to fix count the swipes
from flask import Blueprint, request

swipe_route = Blueprint('swipe_route', __name__)
@swipe_route.route('/', methods=['GET', 'POST'])
def swipes():
    if request.method == 'GET':
        return 'This is a get.'
    else:
        return 'Welcome to the post'
