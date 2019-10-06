from flask import Blueprint, request

user_route = Blueprint('user_route', __name__)

@user_route.route('/', methods = ['GET', 'POST'])
def userCreate():
    if request.method == 'GET':
        return 'This is a get. user'
    else:
        return 'Welcome to the post user'
