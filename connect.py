from pymongo import MongoClient

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('mongodb://tonus:Hammacktony1150*@ds135003.mlab.com:35003/heroku_v6ds7xrr')


db = client.heroku_v6ds7xrr
tweets = db.tweets
# print('One post: {0}'.format(result.inserted_id))
import json
with open('tweets.json', 'r') as f:
    data = json.load(f)