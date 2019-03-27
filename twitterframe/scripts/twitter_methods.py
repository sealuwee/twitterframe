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

    def get_user_tweets(self, username):
        '''
            Code redesigned from yanofsky:
            https://gist.github.com/yanofsky/5436496
            and the Python 3.x version:
            https://gist.github.com/gabrielsoule/638201ac0cc12828d3cde69035a25336

            Not functioning correctly.

            Removed the count paramter.
        '''
        api = self.setup()

        tweets = []

        for tweet in tweepy.Cursor(api.user_timeline, id=username,
                                   ).items():

            tweets.append([username, tweet.id_str, tweet.created_at,
                           tweet.text.encode('utf-8')])

        print(pidgeon, 'Downloading {} tweets ...'.format(len(tweets)))

        # new_tweets = api.user_timeline(screen_name=username,
        #                                count=count)

        # tweets.extend(new_tweets)

        # oldest_tweets = tweets[-1].id - 1

        # while len(tweets) > 0:

        #     print(pidgeon, 'Getting tweets before {}'.format(oldest_tweets))

        #     for tweet in tweepy.Cursor(api.user_timeline, screen_name=username,
        #                                count=200, max_id=oldest_tweets).items(count):

        #         tweets.append([username, tweet.id_str, tweet.created_at,
        #                        tweet.text.encode('utf-8')])

        #     oldest_tweets = tweets[-1].id - 1

        #     print(pidgeon, '... {} Amount of tweets downloaded so far...'.format(len(tweets)))

        # output_tweets = [[tweet.id_str, tweet.created_at,
        #                   tweet.text.encode("utf-8")] for tweet in tweets]

        # return output_tweets

        return tweets

    def crawl(self, hashtag):
        '''
            Crawl method for hashtags.
            This may not work yet lol.
            Will push to pypi.org when this is done.
            since='{}'.format(time) <-- removed this from api.search.
        '''
        api = self.setup()

        tweets = []

        for tweet in tweepy.Cursor(api.search, q='{}'.format(hashtag),
                                   rpp=100, page=10,
                                   lang='en',
                                   ).items():

            tweets.append([hashtag, tweet.id_str, tweet.created_at,
                           tweet.text.encode('utf-8')])

            print(pidgeon, '... {} Amout of tweets dowloaded so far...'.format(len(tweets)))

        output_tweets = [[tweet.id_str, tweet.created_at,
                          tweet.text.encode("utf-8")] for tweet in tweets]

        return output_tweets




