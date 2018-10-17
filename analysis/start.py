import pandas as pd
import sys
import os
from settings import mongo_connections
from queries import queries

conn = mongo_connections['@TomKingTK']
tweet_text = []

for doc in conn.find():
    data.append(doc['text'])

data = {'text', tweet_text}
del tweet_text
df = pd.DataFrame.from_dict(data)
print(df.shape())

