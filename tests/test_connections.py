''' Tests for connections in api '''
import tweepy

from upload import twitter_setup
from settings import client as mongo_client


def test_tweepy():
    ''' Make sure twitter_setup() is a valid tweepy.API instance '''
    assert isinstance(twitter_setup(), tweepy.API)


def test_mongo():
    ''' Make sure the Mongo Client instance connects to my database '''
    db = mongo_client.get_database()
    assert db.name == 'heroku_v6ds7xrr'
