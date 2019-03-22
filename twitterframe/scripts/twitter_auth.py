'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

##TODOs: Create some type of if statement that checks whether or not there is
##       and valid keys in the config.py file
##       We can try doing it by import config
##       and call each key with config.consumer_key
##       config.access_token, etc.
##       AND if they are valid, **Meaning** they are actually strings
##       Pass and move on to actually using twitterframe.
##       I feel like this step is going to be the one step that defines
##       The whole process of the project and the flow of how it will work.
##       So MAKE IT WORK <3


import config
import tweepy
import time
import json
import os
import os.path
import re
from pathlib import Path

# Regular expression for comments in config file
comment_re = re.compile(
    '(^)[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)

twitter_emoji = config.twitter_emoji

# app_name, access_token, access_secret, consumer_key, consumer_secret = check_auth()

# pass OAuth details to tweepy handler.

class Authentication(object):

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

def check_auth():

    # store OAuth credentials from input in command line.
    print(twitter_emoji, '-------------------------')
    print('Step 1: Create account on https://developer.twitter.com')
    print(twitter_emoji, '-------------------------')
    print('Step 2: What is the name of your app?: ', end=' ')
    app_name = input(twitter_emoji, "App Name : ")
    print(twitter_emoji, '-------------------------')
    print('Step 3: Twitter API Access Token: ', end=' ')
    access_token = input(twitter_emoji, "Twitter API Access Token : ")
    print(twitter_emoji, '-------------------------')
    print('Step 4: Secret Access Token: ', end=' ')
    access_secret = input(twitter_emoji, "Secret Access Token : ")
    print(twitter_emoji, '-------------------------')
    print('Step 5: Consumer Key: ', end=' ')
    consumer_key = input(twitter_emoji, "Consumer Key : ")
    print(twitter_emoji, '-------------------------')
    print('Step 6: Secret Consumer Key: ', end=' ')
    consumer_secret = input(twitter_emoji, "Secret Consumer Key : ")

    return Authentication(app_name, access_token, access_secret, consumer_key, consumer_secret)

# tokens = [access_token, access_secret, consumer_key, consumer_secret]

# path = Path("./twitter_credentials.json")
# with path.open('w+') as tw:
#     for i in tokens:
#         tw.write('i\n')

# config = json.loads(open(path).read())
# os.environ['ACCESS_TOKEN'] = config['access_token']
# os.environ['ACCESS_SECRET'] = config['access_secret']
# os.environ['CONSUMER_KEY'] = config['consumer_key']
# os.environ['CONSUMER_SECRET'] = config['consumer_secret']

def authen():
    '''
    Authenticate Twitter OAuth tokens.
    '''
    twitter_creds = os.environ.get(
        'HOME',
        os.environ.get(
            'USERPROFILE',
            '')) + os.sep + '.exit'


def main():

    try:

        assert len(config.access_token) == 20
        assert len(config.access_secret) == 42
        assert len(config.consumer_key) == 50
        assert len(config.consumer_secret) == 39

    except ValueError:

        print('Please sign up for an')

# time.sleep(2)
