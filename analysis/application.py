''' Main guts of sentiment analysis '''
import numpy as np
import pandas as pd

from typing import Tuple
from settings import mongo_connections
from queries import queries
from helpers.analyze import analyze_sentiment

def app(handle: str) -> Tuple:
    ''' Connect to mongodb to get tweets about creator and declare what if their tweets are positive, neutral, or negative
    
    args
        str - handle: Twitter handle of creator in mind

    returns
        tuple - Returns twitter handle, and positive, neutral, and negative percentages of tweets
    '''
    conn = mongo_connections[handle]

    tweet_text = [txt for txt in conn.find()]
    df = pd.DataFrame(tweet_text)
    del tweet_text # Save memory by getting rid of big list

    # We create a column with the result of the analysis:
    df['SA'] = np.array([ analyze_sentiment(tweet) for tweet in df['text'] ])

    # We construct lists with classified tweets:
    pos_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] < 0]

    length = len(df['text'])
    pos_percent = len(pos_tweets)*100/length
    neu_percent = len(neu_tweets)*100/length
    neg_percent = len(neg_tweets)*100/length

    return handle, pos_percent, neu_percent, neg_percent