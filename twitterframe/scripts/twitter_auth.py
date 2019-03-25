'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

# TODOs: SHOUTOUT TO COLE<3
# update twitter emoji

from twitterframe.scripts.utils import *
import tweepy
import json
import click
from pathlib import Path

b = baby_chick
p = party
pidgeon = pidgeon
h = hatching_chick
check = checkmark

class SetupAPI(object):

    def __init__(self,
                 access_token='',
                 access_secret='',
                 consumer_key='',
                 consumer_secret=''):
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
            print(check, 'Made file path as .json',check)
            filename = filename.joinpath(filename.parts[-1]+'.json')
        tw = open(filename.name, 'w+')
        tw.write(json.dumps(keys))
        tw.close()
        print(check,'Keys have been stored in: ',filename.resolve(),check)

        # testing this where to_json also returns the relative path and stores it as
        # a variable to the json file created

def check_auth():
    '''
    I hope this works
    '''
    # store OAuth credentials from input in command line.
    print(h, '-------------------------')
    print(h, '[Step 1: Create an account on https://developer.twitter.com]')
    print(h, '-------------------------')
    # print(h, 'Step 2: Twitter API Access Token: ', end=' ')
    access_token = click.prompt(h, 'Step 2: Twitter API Access Token: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 3: Secret Access Token: ', end=' ')
    access_secret = click.prompt(h, 'Step 3: Secret Access Token: ',
                                 hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 4: Consumer Key: ', end=' ')
    consumer_key = click.prompt(h, 'Step 4: Consumer Key: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 5: Secret Consumer Key: ', end=' ')
    consumer_secret = click.prompt(h, 'Step 5: Secret Consumer Key: ',
                                   hide_input=False, prompt_suffix=' ')

    return SetupAPI(access_token, access_secret, consumer_key, consumer_secret)
