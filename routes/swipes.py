# File to fix count the swipes
from flask import Blueprint, request

swipe_route = Blueprint('swipe_route', __name__)
@swipe_route.route('/', methods=['GET', 'POST'])
def swipes():
    if request.method == 'POST':
        return 'This is a get.'

        # Als er een post wordt gestuud moet die worden toegevoegd aan binary

    else:
        return 'Welcome to the get'
