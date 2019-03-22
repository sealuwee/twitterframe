'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

# TODOs: SHOUTOUT TO COLE<3

import config
import tweepy
import time
import json
import os
from pathlib import Path

twitter_emoji = config.twitter_emoji

class SetupAPI(object):

    def __init__(self,
                 app_name='',
                 access_token='',
                 access_secret='',
                 consumer_key='',
                 consumer_secret=''):
        self.app_name = app_name
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def to_json(self,filename):

        keys = {
            'access_token': self.access_token,
            'access_secret': self.access_secret,
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        }
        filename = Path(filename)
        if '.json' not in filename.parts[-1]:
            print('its working')
            filename = filename.joinpath(filename.parts[-1]+'.json')
        tw = open(filename.name, 'w+')
        tw.write(json.dumps(keys))
        tw.close()

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

def check_auth():

    # store OAuth credentials from input in command line.

    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 1: Create account on https://developer.twitter.com')
    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 2: What is the name of your app?: ', end=' ')
    app_name = input()
    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 3: Twitter API Access Token: ', end=' ')
    access_token = input()
    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 4: Secret Access Token: ', end=' ')
    access_secret = input()
    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 5: Consumer Key: ', end=' ')
    consumer_key = input()
    print(twitter_emoji, '-------------------------')
    print(twitter_emoji, 'Step 6: Secret Consumer Key: ', end=' ')
    consumer_secret = input()

    return SetupAPI(app_name, access_token, access_secret, consumer_key, consumer_secret)
