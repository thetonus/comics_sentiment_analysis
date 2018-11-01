''' Helper functions '''

from textblob import TextBlob
from queries import queries


def analyze_sentiment(post: str) -> int:
    '''
    Utility function to classify the polarity of a post
    using textblob.

    args
        str - Text of post

    returns
        int - sentiment analysis score (scale from 1-3)
    '''

    analysis = TextBlob(post)
    if analysis.sentiment.polarity > 0:
        return 3
    elif analysis.sentiment.polarity == 0:
        return 2
    else:
        return 1
