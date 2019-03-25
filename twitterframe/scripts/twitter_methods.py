'''
twitter-trends.py : uh
'''
#

from . import utils
import tweepy
import json
import csv
import os
from pathlib import Path

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark

config_path = utils.config_path

class TwitterWrapper(object):
    '''
    subclass of SetupAPI
    TwitterTrends class.
    Methods that I want to use:
    Get Twitter Trends by location
    Get top 10 Twitter Trends
    I guess just the get methods from the API, just as methods from this class...
    '''

    def __init__(self,
                 access_token,
                 access_secret,
                 consumer_key,
                 consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def setup(self):

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth)

        return api

    def get_timeline(self):
        '''
        https://tweepy.readthedocs.io/en/v3.5.0/api.html#API.home_timeline
        '''
        return [tweet.text for tweet in self.setup().home_timeline()]

    def get_tweets(self, username):

        '''
            Code redesigned from yanofsky:
            https://gist.github.com/yanofsky/5436496
            and the Python 3.x version:
            https://gist.github.com/gabrielsoule/638201ac0cc12828d3cde69035a25336
        '''

        api = self.setup()

        tweets = []

        new_tweets = api.user_timeline(sceen_name=username, count=200)

        tweets.extend(new_tweets)

        oldest_tweets = tweets[-1].id - 1

        while len(new_tweets) > 0:

            print(pidgeon, 'Getting tweets before {}'.format(oldest_tweets))

            new_tweets = api.user_timeline(screen_name=username, count=200,
                                           max_id=oldest_tweets)

            tweets.extend(new_tweets)

            oldest_tweets = tweets[-1].id - 1

            print(pidgeon, '... {} Amount of tweets downloaded so far...'.format(len(tweets)))

            print(pidgeon, 'Getting more tweets before {}'.format(oldest_tweets))

        output_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

        print(check,pidgeon, '{} Tweets have been downloaded! '.format(len(output_tweets)))

        return output_tweets


