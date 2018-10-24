''' Tests for connections in api '''
import tweepy
import praw

from upload.twitter import twitter_setup
from upload.reddit import reddit_setup
from settings import client as mongo_client


def test_tweepy():
    ''' Make sure twitter_setup() returns a valid tweepy.API instance '''
    assert isinstance(twitter_setup(), tweepy.API)


def test_mongo():
    ''' Make sure the Mongo Client instance connects to my database '''
    db = mongo_client.get_database()
    assert db.name == 'heroku_v6ds7xrr'

def test_reddit():  
    ''' Make sure redit_setup() returns a valid praw.Reddit instance '''
    assert isinstance(reddit_setup(), praw.Reddit)