''' Upload tweets of that mention certain comics creators '''
import tweepy

from helpers.upload import get_tweet
from settings import mongo_connections, twitter_credentials
from queries import queries