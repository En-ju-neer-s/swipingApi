from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

news_source_route = Blueprint('news_source_route', __name__)

# connect to db
db = client.swiper


@news_source_route.route('/newsSources', methods=['get', 'post'])
def newsSources():
    # Return all articles
    if request.method == 'GET':
        return(dumps(db.newsSources.find({})))
