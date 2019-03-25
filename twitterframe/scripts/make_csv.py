'''
make_csv.py : this is the script that
                    constructs a dataframe from whatever script(s) is(are) called.
'''

import twitterframe.scripts.twitter_auth as auth
import twitterframe.scripts.utils as utils
import tweepy
import config
import csv

twitter_emoji = config.twitter_emoji