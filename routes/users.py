from flask import Blueprint, request

users_route = Blueprint('users_route', __name__)

@users_route.route('/', methods=['GET', 'POST'])
def topUsers():
    if request.method == 'GET':
        return 'Welcome on this page'