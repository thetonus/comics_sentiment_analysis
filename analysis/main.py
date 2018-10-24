''' Main guts of sentiment analysis '''

from typing import Tuple
from settings import mongo_connections
from queries import queries
from helpers.analyze import analyze_sentiment


def app(handle: str) -> Tuple:
    ''' Connect to mongodb to get tweets about creator 
    and declare what if their tweets are positive, neutral, or negative

    args
        str - handle: Twitter handle of creator in mind

    returns
        tuple - Returns twitter handle, and positive, neutral, and negative percentages of tweets
    '''

    conn = mongo_connections[handle]

    tweets = [doc['text'] for doc in conn.find()]

    # We create a column with the result of the analysis:
    sentiment_scores = list(map(analyze_sentiment, tweets))

    # We construct lists with classified tweets:
    pos_tweets = [tweet for index, tweet in enumerate(
        tweets) if sentiment_scores[index] > 0]
    neu_tweets = [tweet for index, tweet in enumerate(
        tweets) if sentiment_scores[index] == 0]
    neg_tweets = [tweet for index, tweet in enumerate(
        tweets) if sentiment_scores[index] < 0]

    try:
        length = len(tweets)
        pos_percent = len(pos_tweets)*100/length
        neu_percent = len(neu_tweets)*100/length
        neg_percent = len(neg_tweets)*100/length
    except ZeroDivisionError:
        # There are no tweets. So return 0%
        # for positive, neutral, and negative percents
        pos_percent, neu_percent, neg_percent = 0, 0, 0

    return handle, pos_percent, neu_percent, neg_percent
