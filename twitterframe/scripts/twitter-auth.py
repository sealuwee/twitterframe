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

# Regular expression for comments in config file
comment_re = re.compile(
    '(^)[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)

twitter_emoji = config.twitter_emoji

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

    return app_name, access_token, access_secret, consumer_key, consumer_secret

# app_name, access_token, access_secret, consumer_key, consumer_secret = check_auth()

# pass OAuth details to tweepy handler.

path = "./twitter_credentials.json"
kaggle_config = json.loads(open(path).read())
os.environ['KAGGLE_USERNAME'] = kaggle_config['username']
os.environ['KAGGLE_KEY'] = kaggle_config['key']

def init_config():
    '''
    Initialize config.
    '''

    config = os.path.dirname(__file__)
    pass

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

init_config()