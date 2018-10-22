''' Getting credentials and initializing connections '''
import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())

# Establishing Twitter Credentials
twitter_credentials = {
    "CONSUMER_KEY": os.getenv('CONSUMER_KEY'),
    "CONSUMER_SECRET": os.getenv('CONSUMER_SECRET'),
    "ACCESS_TOKEN": os.getenv('ACCESS_TOKEN'),
    "ACCESS_SECRET": os.getenv('ACCESS_SECRET'),
}

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
