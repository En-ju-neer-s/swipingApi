from flask import Blueprint
from bson.json_util import dumps
from ..connection import client

swipesStats = Blueprint('swipesStats', __name__)

# Connect to client
db = client.swiper


@swipesStats.route('/swipesStats', methods=['GET'])
def swipesStatsGetter():
    # Get all iitems with how many yesses and nos
    totalSwipes = db.testTitles.aggregate([
        {
            '$lookup': {
                'from': "binary",
                'localField': "primary_key",
                'foreignField': "primaryKey",
                'as': "binaryData"
            }
        },
        {
            '$project': {'title': 1, 'source': 1, 'description': 1, 'url': 1, 'primary_key': 1, 'timestamp': 1, '_id': 0, 'binaryData.clickbait': 1}
        }
    ])

    clicbaitYes = 0
    clicbaitNo = 0
    newItems = []

    for value in totalSwipes:
        test = value
        clickbait = value['binaryData']
        if(len(clickbait) > 0):  # function to change catorogies things
            for result in clickbait:
                if result['clickbait']:
                    clicbaitYes = clicbaitYes + 1
                else:
                    clicbaitNo = clicbaitNo + 1

            clickbaitTotal = clicbaitYes + clicbaitNo

            test['clickbait'] = {'clicbaitYes': clicbaitYes, 'clicbaitNo': clicbaitNo, 'total': clickbaitTotal}

            clicbaitNo = clicbaitYes = 0
            pass
        else:
            test['clickbait'] = {'clicbaitYes': 0, 'clicbaitNo': 0, 'total': 0}

        test.pop('binaryData')
        newItems.append(test)
    pass

    return dumps(newItems)
