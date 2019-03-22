'''
make-dataframe.py : this is the script that
                    constructs a dataframe from whatever script(s) is(are) called.
'''

import tweepy
import config
import pandas
import click
import csv

twitter_emoji = config.twitter_emoji
