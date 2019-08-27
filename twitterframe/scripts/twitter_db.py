'''
twitter_db file to house the class method for working with
tweepy._json files and adding them to a database of choice.

twitter_db will be the first script I use with the new shell in twitter_cmd
and will only be accessible from the shell environment.
'''

from . import utils
import tweepy
import json
import csv
import os
from pathlib import Path
import time
from tqdm import tqdm
import psychopg2 as pg
import crayons
import SQLAlchemy
from SQLAlchemy import create_engine

class TwitterDB(object):
    '''
      DB Class
    '''
    def __init__(self,
                 access_token,
                 access_secret,
                 consumer_key,
                 consumer_secret,
                 dbname,
                 user,
                 password,
                 host,
                 port):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def setup(self):
        '''
          setup method from twitter_methods
        '''
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth)

        return api

