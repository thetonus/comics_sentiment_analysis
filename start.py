# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

from settings import twitter_credentials


# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(twitter_credentials["CONSUMER_KEY"], twitter_credentials["CONSUMER_SECRET"])
    auth.set_access_token(twitter_credentials["ACCESS_TOKEN"], twitter_credentials["ACCESS_SECRET"])

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# ------------------------------------
# We create an extractor object:
extractor = twitter_setup()
count = 10^4
# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="Ssnyder1835", count=count)

# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
# We add relevant data:
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Author']   = np.array([tweet.author.screen_name for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])



# We display the first 10 elements of the dataframe:
test = data.loc[data['Author'] != 'Ssnyder1835']
print(test.head(10))

######################
# We extract the mean of lenghts:
# mean = np.mean(data['len'])

# print("The lenght's average in tweets: {}".format(mean))


# # We extract the tweet with more FAVs and more RTs:

# fav_max = np.max(data['Likes'])
# rt_max  = np.max(data['RTs'])

# fav = data[data.Likes == fav_max].index[0]
# rt  = data[data.RTs == rt_max].index[0]

# # Max FAVs:
# print("The tweet with more likes is: \n{}".format(data['Tweets'][fav]))
# print("Number of likes: {}".format(fav_max))
# print("{} characters.\n".format(data['len'][fav]))

# # Max RTs:
# print("The tweet with more retweets is: \n{}".format(data['Tweets'][rt]))
# print("Number of retweets: {}".format(rt_max))
# print("{} characters.\n".format(data['len'][rt]))


# # --------------------------------
# from textblob import TextBlob
# import re

# def clean_tweet(tweet):
#     '''
#     Utility function to clean the text in a tweet by removing 
#     links and special characters using regex.
#     '''
#     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# def analize_sentiment(tweet):
#     '''
#     Utility function to classify the polarity of a tweet
#     using textblob.
#     '''
#     analysis = TextBlob(clean_tweet(tweet))
#     if analysis.sentiment.polarity > 0:
#         return 1
#     elif analysis.sentiment.polarity == 0:
#         return 0
#     else:
#         return -1

# # We create a column with the result of the analysis:
# data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])
# # We display the first 10 elements of the dataframe:
# print(data.head(10))

# # We construct lists with classified tweets:

# pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
# neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
# neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]


# # We print percentages:

# print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['Tweets'])))
# print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['Tweets'])))
# print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['Tweets'])))

# print(data['Author'][:10])