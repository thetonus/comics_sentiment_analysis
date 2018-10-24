''' Getting credentials and initializing connections '''
import os

from collections import namedtuple
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())

# Establishing Twitter Credentials
TWITTER = namedtuple('CONSUMER_KEY',
                     'CONSUMER_SECRET',
                     'ACCESS_TOKEN',
                     'ACCESS_SECRET')

twitter_credentials = TWITTER(os.getenv('TWITTER_CONSUMER_KEY'),
                              os.getenv('TWITTER_CONSUMER_SECRET'),
                              os.getenv('TWITTER_ACCESS_TOKEN'),
                              os.getenv('TWITTER_ACCESS_SECRET')
                              )

# Establishing Reddit Credentials
REDDIT = namedtuple('CLIENT_ID',
                    'CLIENT_SECRET',
                    'USER_AGENT',
                    'USERNAME',
                    'PASSWORD')
                    
reddit_credentials = REDDIT(os.getenv('REDDIT_CLIENT_ID'),
                            os.getenv('REDDIT_CLIENT_SECRET'),
                            os.getenv('REDDIT_USER_AGENT'),
                            os.getenv('REDDIT_USERNAME'),
                            os.getenv('REDDIT_PASSWORD'))

# MongoDB Connection
client = MongoClient(os.getenv('MONGODB_URI'))
mongo = client.heroku_v6ds7xrr

mongo_connections = {
    'Tom King': mongo.t_king,
    'Scott Snyder': mongo.s_snyder,
    'James Tynion': mongo.j_t4,
    'Joelle Jones': mongo.j_jones,
    'Geoff Johns': mongo.g_johns,
    'James Robinson': mongo.j_robinson,
}
