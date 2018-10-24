''' Helper functions for upload.py '''
import re

from typing import Dict


def clean_text(text: str) -> str:
    '''
    Utility function to clean text by removing
    links and special characters using regex.

    args
        text: str - text that needs to be cleaned

    return
        str - Cleaned text
    '''

    return ' '.join(
        re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
               " ", text).split())


def get_tweet(tweet_json: Dict[str, str]) -> str:
    '''
    Get tweet from Twitter Api Resonse

    args
        tweet_json: dict - Twitter Api Response

    return
        str - text of tweet
    '''

    tweet_text = tweet_json['text']
    return clean_text(tweet_text)
