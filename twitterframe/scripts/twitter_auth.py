'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

# TODOs: SHOUTOUT TO COLE<3
# update twitter emoji

from scripts.utils import *
import tweepy
import json
from pathlib import Path

b = baby_chick
p = party
pidgeon = pidgeon
h = hatching_chick

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

    def to_json(self, filename=''):

        keys = {
            'access_token': self.access_token,
            'access_secret': self.access_secret,
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        }

        filename = Path(filename)
        if '.json' not in filename.parts[-1]:
            print(b, 'Made file path as .json')
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
    print(h, '-------------------------')
    print(h, 'Step 1: Create account on https://developer.twitter.com')
    print(h, '-------------------------')
    print(h, 'Step 2: What is the name of your app?: ', end=' ')
    app_name = input()
    print(h, '-------------------------')
    print(h, 'Step 3: Twitter API Access Token: ', end=' ')
    access_token = input()
    print(h, '-------------------------')
    print(h, 'Step 4: Secret Access Token: ', end=' ')
    access_secret = input()
    print(h, '-------------------------')
    print(h, 'Step 5: Consumer Key: ', end=' ')
    consumer_key = input()
    print(h, '-------------------------')
    print(h, 'Step 6: Secret Consumer Key: ', end=' ')
    consumer_secret = input()

    return SetupAPI(app_name, access_token, access_secret, consumer_key, consumer_secret)
