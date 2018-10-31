''' Api for finding sentiment analysis of comic creators '''
import ujson
import falcon

from analysis import app
from queries import queries
# from stats import retrieve_stats

class ComicsWritersSentiment(object):
    ''' Meat of api '''

    def on_get(self, req, resp):
        """ Handles GET requests """
        # Check to see if user entered a creator to search
        try:
            if req.get_param("creator"):
                #  Check to make sure user's input is a legit creator
                if req.get_param("creator") in queries:

                    data = app(req.get_param("creator"))

                    result = {
                        'creator': data[0],
                        'total tweets': data[1],
                        'postive_mean': data[2],
                        'postive_std': data[3],
                        'neutral_mean': data[4],
                        'neutral_std': data[5],
                        'negative_mean': data[6],
                        'negative_std': data[7],
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
        # Shit Catcher
        except Exception as e:
            result = {'error': str(e)}
            resp.body = ujson.dumps(result)
            # return 404 if bad search
            resp.status = falcon.HTTP_500

api = falcon.API()
api.add_route('/', ComicsWritersSentiment())