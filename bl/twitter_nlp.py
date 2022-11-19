from textblob import TextBlob
import sys
import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from utilities.cache import cache
import os

consumerKey = os.environ['consumerKey']  ## API Key
consumerSecret = os.environ['consumerSecret']  ## API Key Secret
accessToken = os.environ['accessToken']  ## Access Token
accessTokenSecret = os.environ['accessTokenSecret']  ## Access Token Secret



# @cache.cached(timeout=3600)
def fetch_tweets_analysis(keyword, n_tweets):
    n_tweets = min(100,n_tweets)
    print("Authentication starts here..............")
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    print("Setting Access token here...............")
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("Connection to Twitter established!")
    except:
        print("Failed to connect to Twitter!")

    tweets = api.search_tweets(q=keyword, lang="en", count=100, tweet_mode = "extended")  ## keyword, count
    # positive = 0
    # negative = 0
    # neutral = 0
    # polarity = 0
    tweet_list = []
    sentiment_list = []

    print("Iterating over tweets............")
    for tweet in tweets:
        # analysis = TextBlob(tweet.text)
        tweet_list.append(tweet.full_text)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.full_text)
        neg = score['neg']
        # neu = score['neu']
        pos = score['pos']
        # comp = score['compound']
        # polarity += analysis.sentiment.polarity

        if neg > pos:
            sentiment_list.append('Negative')
            # negative += 1

        elif pos > neg:
            sentiment_list.append('Positive')
            # positive += 1

        elif pos == neg:
            sentiment_list.append('Neutral')
            # neutral += 1

        if len(tweet_list) == n_tweets:
            break

    # res = {
    #     'keyword' : keyword,
    #     'negative' : negative,
    #     'positive': positive,
    #     'neutral' : neutral
    # }

    res = {
        'tweets' : tweet_list,
        'sentiments': sentiment_list
    }

    return res
