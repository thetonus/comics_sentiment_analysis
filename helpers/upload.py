''' Helper functions for upload.py '''
import re

from typing import Dict


def clean_tweet(tweet_txt: str) -> str:
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.

    args
        str - Text of the Tweet

    return
        str - Cleaned of the Tweet
    '''
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet_txt).split())


def get_tweet(tweet_json: Dict[str, str]) -> str:
    '''
    Get tweet from Twitter Api Resonse

    args
        dict - Twitter Api Response

    return
        str - text of tweet
    '''

    tweet_text: str = tweet_json['text']
    return clean_tweet(tweet_text)
