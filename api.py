''' Api for finding sentiment analysis of comic creators '''
import json
import falcon

from application import app
from helpers import validate_creator


class TwitterSentiment(object):

	 def on_get(self, req, resp):
        """Handles GET requests"""

        # Check to see if user entered a creator to search
        if req.get_param("creator"):
            #  Check to make sure user's input is a legit creator
            if validate_creator(req.get_param("creator")):

                creator, pos_percent, neu_percent, neg_percent  = app(req.get_param("creator"))

                result = {
                    'creator': creator, 
                    'postive_percent': pos_percent,
                    'neutral_percent': neu_percent,
                    'negative_percent': neg_percent
                }
            else:
                result = {'error': f'{req.get_param("creator")} is not an acceptable twitter handle. '}
        else:
            result = {'error': 'No twitter handle to search'}
        resp.body = json.dumps(result)


api = falcon.API()
api.add_route('/creator', TwitterSentiment())