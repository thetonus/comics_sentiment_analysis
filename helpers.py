''' Helper functions '''
import re

from textblob import TextBlob
from queries import queries


def clean_tweet(tweet: str) -> str:
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analize_sentiment(tweet: str) -> int:
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def validate_creator(creator: str) -> bool:
    ''' Validate creator

    args
        str - creator twitter handle

    return 
        bool - if creator is in set of twitter handles '''

    if creator in queries:
        return True
    return False
