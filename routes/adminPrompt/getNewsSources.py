from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

news_source_route = Blueprint('news_source_route', __name__)

# connect to db
db = client.swiper

# TODO: ADD AUTHENTICATION
@news_source_route.route('/newsSources', methods=['get', 'post'])
def newsSources():
    # Return all articles
    if request.method == 'GET':
        return(dumps(db.newsProviders.find({})))
    if request.method == 'POST':
        if request.json['source'] and len(request.json['source']) > 0:  # Validation
            print(request.json['source'])
            newsSourceObject = {"name": request.json['source'], "value": request.json['source']}
            # insert to DB
            db.newsProviders.insert(newsSourceObject)
        else:
            return dumps({'success': False, 'message': 'Json name is not good/Value is empty'})

        return dumps({'success': True, 'message': 'created'})
