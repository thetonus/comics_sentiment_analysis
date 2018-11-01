''' Api for finding sentiment analysis of comic creators '''
import ujson
import falcon

from analysis import app
from queries import queries
from stats import retrieve_stats

class ComicsWritersSentiment(object):
    ''' Meat of api '''

    def on_get(self, req, resp):
        """ Handles GET requests """
        
        # Check to see if user entered a creator to search
        try:
            if req.get_param("creator"):
                #  Check to make sure user's input is a legit creator
                if req.get_param("creator") in queries:

                    result = retrieve_stats(req.get_param("creator"))
                    result.pop('_id', None) # Delete ID field

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