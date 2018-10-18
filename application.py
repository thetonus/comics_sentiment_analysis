''' Main guts of sentiment analysis '''
import numpy as np
import pandas as pd
from typing import Tuple
from settings import mongo_connections
from queries import queries

def app(searchQuery: str) -> Tuple:
    ''' Connect to mongodb to get tweets about creator and declare what if their tweets are positive, neutral, or negative
    
    args
        str - searchQuery: Twitter handle of creator in mind

    returns
        tuple - Returns twitter handle, and positive, neutral, and negative percentages of tweets
    '''
    conn = mongo_connections[searchQuery]

    # tweet_text = list()
    # for doc in conn.find():
    #     tweet_text.append({'text': doc['text']})

    tweet_text = [{'text': doc['text']} for doc in conn.find()]
    df = pd.DataFrame(tweet_text)
    del tweet_text # Save memory by getting rid of big list

    # We create a column with the result of the analysis:
    df['SA'] = np.array([ analize_sentiment(tweet) for tweet in df['text'] ])

    # We construct lists with classified tweets:
    pos_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(df['text']) if df['SA'][index] < 0]

    pos_percent = len(pos_tweets)*100/len(df['text']))
    neu_percent = len(neu_tweets)*100/len(df['text']))
    neg_percent = len(neg_tweets)*100/len(df['text']))

    # We print percentages:
    print(f"Percentage of positive tweets: {pos_percent}%")
    print(f"Percentage of neutral tweets: {neu_percent}%")
    print(f"Percentage de negative tweets: {neg_percent}%")

    del df # Save memory by getting rid of big dataframe
    
    return handle, pos_percent, neu_percent, neg_percent