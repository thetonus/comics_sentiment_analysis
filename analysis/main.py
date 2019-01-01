''' Main guts of sentiment analysis '''
import numpy as np
from typing import Tuple
from settings import mongo_connections
from queries import queries
from helpers.analyze import analyze_sentiment


def app(handle: str) -> Tuple:
    ''' Connect to mongodb to get posts about a creator
    and declare those posts are positive, neutral, or negative

    args
        str - handle: Name creator in mind

    returns
         tuple - Returns name, 
                    len of posts about person, 
                    mean of postive posts,
                    standard deviation of postive posts, 
                    mean of neutral posts, 
                    standard deviation of neutral posts, 
                    mean of negative posts,
                    standard deviation of negative posts,   

    '''

    # Initialize
    conn = mongo_connections[handle]
    posts = [doc['text'] for doc in conn.find()]

    # We create a list with the result of the analysis:
    sentiment_scores = list(map(analyze_sentiment, posts))

    # Each type of post
    pos_posts, neu_posts, neg_posts = list(), list(), list()

    # Collect sentiments for each type of post
    for i in range(len(sentiment_scores)):
        # Basic idea is one-hot encoding data at each index i
        if sentiment_scores[i] == 1:
            pos_posts.append(1)
            neu_posts.append(0)
            neg_posts.append(0)
        if sentiment_scores[i] == 0:
            pos_posts.append(0)
            neu_posts.append(1)
            neg_posts.append(0)
        if sentiment_scores[i] == -1:
            pos_posts.append(0)
            neu_posts.append(0)
            neg_posts.append(1)

    try:
        # Calculate mean and std of posts
        pos_mean, pos_std = np.mean(pos_posts), np.std(pos_posts)
        neu_mean, neu_std = np.mean(neu_posts), np.std(neu_posts)
        neg_mean, neg_std = np.mean(neg_posts), np.std(neg_posts)

    except ZeroDivisionError:
        # If there are no posts (which will be rare, if ever), 
        #    return 0 for means and stds
        pos_mean, pos_std = 0, 0
        neu_mean, neu_std = 0, 0
        neg_mean, neg_std = 0, 0

    data = (handle, len(posts), pos_mean, pos_std,
            neu_mean, neu_std, neg_mean, neg_std)
    return data
