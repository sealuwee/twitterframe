'''
	Was going to add this to the twitter_methods.py but this will just be cleaner.
	Might make it more efficient, who knows!
'''

import tweepy
import os
import pathlib as Path 
import json
import csv
import sqlite3


class TwitterListener(tweepy.StreamListener):
    '''
        Create a class that inherits StreamListener from tweepy.
        Create a Stream object
        Use api = self.setup() to set up authentication.
    '''
    def on_status(self, status):

        print(status.text)