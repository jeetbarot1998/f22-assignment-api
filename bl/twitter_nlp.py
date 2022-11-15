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
def main_func(keyword):
    print("Authenticating starts here..............")
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    print("Setting Access token here...............")
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Connection to Twitter established.")
    except:
        print("Failed to connect to Twitter.")

    tweets = api.search_tweets(q=keyword, lang="en", count=100)  ## keyword
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0

    print("Iterating over tweets............")
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        comp = score['compound']
        polarity += analysis.sentiment.polarity

        if neg > pos:
            negative += 1

        elif pos > neg:
            positive += 1

        elif pos == neg:
            neutral += 1

    # print("Finalizing DataFrames............")
    # output = pd.DataFrame(
    #     data={'Sentiments': ['negative', 'positive', 'neutral'], '# tweets': [negative, positive, neutral]})
    # output['% tweets'] = round(output['# tweets'] / 100, 2)

    res = {
        'keyword' : keyword,
        'negative' : negative,
        'positive': positive,
        'neutral' : neutral
    }

    return res
