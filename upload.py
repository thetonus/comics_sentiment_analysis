''' Upload tweets of that mention certain comics creators '''
import tweepy

from helpers.upload import get_tweet
from settings import mongo_connections, twitter_credentials
from queries import queries


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.

    returns
        tweepy.Api instance

    """

    # Authentication and access using keys:
    auth = tweepy.AppAuthHandler(
        twitter_credentials["CONSUMER_KEY"],
        twitter_credentials["CONSUMER_SECRET"]
    )
    auth.secure = True
    api = tweepy.API(auth,
                     wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True
                     )

    return api


def upload_tweets(api, searchQuery: str, ) -> None:
    ''' Connects uploads the tweets to mongodb give query

    args
        str - searchQuery: search parameter    
    '''

    # Initialize
    retweet_filter: str = '-filter:retweets'
    q = searchQuery+retweet_filter
    tweetsPerQry: int = 100
    tweetCount: int = 0
    max_id = -1
    maxTweets: int = 5000
    sinceId = None
    conn = mongo_connections[searchQuery]

    while tweetCount < maxTweets:
        try:
            if max_id <= 0:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                # Upload to MongoDB collection
                conn.insert_one({'text': get_tweet(tweet._json)})
            tweetCount += len(new_tweets)
            print(f"Downloaded {tweetCount} tweets")
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break


def main():
    api = twitter_setup()

    # Upload tweets
    print('Beginning Upload')
    for searchQuery in queries:
        print(f'Tweets for {searchQuery}')
        upload_tweets(api, searchQuery)
    print('Upload Complete')


# Run program
if __name__ == '__main__':
    main()
