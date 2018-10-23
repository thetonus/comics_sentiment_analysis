''' Api for finding sentiment analysis of comic creators '''
import ujson
import falcon

from analysis.application import app
from queries import queries


class TwitterSentiment(object):
    ''' Meat of api '''

    def on_get(self, req, resp):
        """ Handles GET requests """
        # Check to see if user entered a creator to search
        if req.get_param("creator"):
            #  Check to make sure user's input is a legit creator
            if req.get_param("creator") in queries:

                creator, pos_percent, neu_percent, neg_percent = app(
                    req.get_param("creator"))

                result = {
                    'creator': creator,
                    'postive_percent': pos_percent,
                    'neutral_percent': neu_percent,
                    'negative_percent': neg_percent
                }
                resp.body = ujson.dumps(result)
                # return successful request
                resp.status = falcon.HTTP_200
            else:
                result = {
                    'error': f'{req.get_param("creator")} is not a supported creator.'}
                resp.body = ujson.dumps(result)
                # return 406 if parameters are not acceptable
                resp.status = falcon.HTTP_406
        else:
            result = {'error': 'No query parameter'}
            resp.body = ujson.dumps(result)
            # return 404 if bad search
            resp.status = falcon.HTTP_404


def create():
    api = falcon.API()
    api.add_route('/', TwitterSentiment())
    return api


api = create()
