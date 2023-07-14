import tweepy
from textblob import TextBlob
def set_api():

    consumer_key = "xHMCRCOhn1L8EeLNHMGMk9tg0"
    consumer_secret = "ff6zup7w69uxckNjpWGuei2pYFkP3RCmuh4Z3dgryTd046qsPE"
    access_token = "3555959242-TsdvfJ2YQumaVgisN8QuvOLm6FLletJGjY14sck"
    access_token_secret = "lBedDSZ6b4prmJ6k9llTVHYF4zox9cf7Vn2r8J8K9LwQJ"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def get_tweets(hashtag, n):
    api = set_api()
    tweets = tweepy.Cursor(api.search_tweets, hashtag, lang="en").items(n)
    return tweets


