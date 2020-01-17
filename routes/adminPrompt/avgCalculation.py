from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps
from flask_pymongo import ObjectId


avgCalcRoute = Blueprint('avgCalcRoute', __name__)

# Connect to DB
db = client.swiper


@avgCalcRoute.route('/average', methods=['POST'])
def avgChange():

    if 1:
        # if db.apiKey.find({'apiKey': request.form['apiKey']}).count() > 0:
        if request.json['calculate']:
            db.average.update(
                {'_id': ObjectId("5e21a054546570923dfdb3c0")},
                {'$set': {'calculate': True}}
            )

            if request.json['staticAverage']:
                db.average.update(
                    {'_id': ObjectId("5e21a054546570923dfdb3c0")},
                    {'$set': {'staticAverage': request.json['staticAverage']}}
                )

            return "updated", 202
        else:
            db.average.update(
                {'_id': ObjectId("5e21a054546570923dfdb3c0")},
                {'$set': {'staticAverage': request.json['staticAverage']}}
            )

            return "updated", 202

    else:
        return dumps({"succes": False, 'errorMessage': 'Api key expired get a new one'}), 301
