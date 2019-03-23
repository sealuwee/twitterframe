'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

# TODOs: SHOUTOUT TO COLE<3
# update twitter emoji

import utils
import tweepy
import json
from pathlib import Path

b = utils.baby_chick
p = utils.party
wj = utils.will_jarvis
h = utils.hatching_chick

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
        print(wj,'What would you like your filename to be to store your Twitter credentials?',wj)
        filename=input()

        if filename == None:
            try:
                print('Please specify a valid name for the keys file.')
                filename=input()
            except:
                print('So what about the last message did you not understand.')

        elif:
            continue

        
        filename = Path(filename)
        if '.json' not in filename.parts[-1]:
            print('Made file path as .json')
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
    print(b, '-------------------------')
    print(b, 'Step 1: Create account on https://developer.twitter.com')
    print(b, '-------------------------')
    print(b, 'Step 2: What is the name of your app?: ', end=' ')
    app_name = input()
    print(b, '-------------------------')
    print(b, 'Step 3: Twitter API Access Token: ', end=' ')
    access_token = input()
    print(b, '-------------------------')
    print(b, 'Step 4: Secret Access Token: ', end=' ')
    access_secret = input()
    print(b, '-------------------------')
    print(b, 'Step 5: Consumer Key: ', end=' ')
    consumer_key = input()
    print(b, '-------------------------')
    print(b, 'Step 6: Secret Consumer Key: ', end=' ')
    consumer_secret = input()

    return SetupAPI(app_name, access_token, access_secret, consumer_key, consumer_secret)
