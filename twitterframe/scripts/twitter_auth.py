'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

# TODOs: SHOUTOUT TO COLE<3
# update twitter emoji

from scripts.utils import *
import tweepy
import json
import click
from pathlib import Path

b = baby_chick
p = party
pidgeon = pidgeon
h = hatching_chick

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
            click.echo(b, 'Made file path as .json')
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
    '''
    I hope this works
    '''
    # store OAuth credentials from input in command line.
    click.echo(h, '-------------------------')
    click.echo(h, 'Step 1: Create an account on https://developer.twitter.com')
    click.echo(h, '-------------------------')
    click.echo(h, 'Step 2: Twitter API Access Token: ', end=' ')
    access_token = click.prompt(hide_input=True, prompt_suffix=' ')
    click.echo(h, '-------------------------')
    click.echo(h, 'Step 3: Secret Access Token: ', end=' ')
    access_secret = click.prompt(hide_input=True, prompt_suffix=' ')
    click.echo(h, '-------------------------')
    click.echo(h, 'Step 4: Consumer Key: ', end=' ')
    consumer_key = click.prompt(hide_input=True, prompt_suffix=' ')
    click.echo(h, '-------------------------')
    click.echo(h, 'Step 5: Secret Consumer Key: ', end=' ')
    consumer_secret = click.prompt(hide_input=True, prompt_suffix=' ')

    return SetupAPI(access_token, access_secret, consumer_key, consumer_secret)
