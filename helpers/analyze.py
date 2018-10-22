''' Helper functions '''

from textblob import TextBlob
from queries import queries

def analyze_sentiment(tweet: str) -> int:
    '''
    Utility function to classify the polarity of a tweet
    using textblob.

    args
        str - Text of tweet

    returns
        int - sentiment analysis score
    '''
    
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

