'''
twitter-trends.py : uh
'''
#

from . import utils
import tweepy
import json
import csv
import os
from pathlib import Path
import logging
import time
from tqdm import tqdm

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark

config_path = utils.config_path

class TwitterWrapper(object):
    '''
    subclass of SetupAPI
    TwitterTrends class.
    Methods that I want to make in the future...:
    Get Twitter Trends by location
    Get top 10 Twitter Trends
    I guess just the get methods from the API, just as methods from this class...
    '''

    def __init__(self,
                 access_token,
                 access_secret,
                 consumer_key,
                 consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def setup(self):

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth)

        return api

    def verify_creds(self):

        api = self.setup()

        try:
            api.verify_credentials()
            print(check, 'Credentials have been verified!')
            print(pidgeon, 'Enjoy using twitterframe.')

        except:
            print(w*3, 'Credentials are not valid.')

    def get_timeline(self):
        '''
        https://tweepy.readthedocs.io/en/v3.5.0/api.html#API.home_timeline
        '''
        return [tweet.text for tweet in self.setup().home_timeline()]

    def get_user_tweets(self, username, limit=50000):
        '''
           Get tweets by username with the tweepy.API method --> user_timeline.
           This works.
        '''
        api = self.setup()

        try: 
            tweets = []
            user_tweets = tweepy.Cursor(api.user_timeline, id=username,
                                   ).items(limit)
            p_bar = tqdm(user_tweets, ascii=True, total=limit, desc='Harvesting Tweets from user: {}'.format(username))

            for i, tweet in enumerate(p_bar):
                p_bar.update(1)
                if i > limit:
                    break

                tweets.append([username, tweet.id_str, tweet.created_at,
                               tweet.text.encode('utf-8')])

            print(pidgeon, 'Downloaded {} tweets from user: {}'.format(len(tweets), username))

        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Ending loop.")
            print(w, twrle)

        print(pidgeon, '{} Downloaded tweets from user: {} !'.format(len(tweets),username))
 
        return tweets

    def crawl(self, hashtag, count, limit=50000):
        '''
            Crawl method for hashtags.
            :hashtag: we want to be able to pass a list of hashtags here.
            :count: count is the passed parameter for the amount of tweets collected.
            This may not work yet lol.
            Will push to pypi.org when this is done.
            since='{}'.format(time) <-- removed this from api.search.
        '''
        api = self.setup()

        try:
            tweets = []
            hashtag_tweets = tweepy.Cursor(api.search, q=hashtag,
                                       rpp=count, result_type='recent',
                                       include_entities=True, 
                                       exclude_replies=True,
                                       lang='en',
                                       ).items(limit)

            print(h, 'Collecting tweets from #{}'.format(hashtag), pidgeon)
            
            p_bar = tqdm(hashtag_tweets, ascii=True, total=limit, desc='Harvesting Tweets from user: {}'.format(hashtag))

            for count, tweet in hashtag_tweets:
                p_bar.update(1)
                if count > limit:
                    break

                tweets.append([hashtag, tweet.id_str, tweet.created_at,
                               tweet.text.encode('utf-8')])

        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Ending loop.")
            print(w, twrle)

        print(pidgeon, '{} Downloaded tweets, with the hashtag {} !'.format(len(tweets),hashtag))

        return tweets

    def limit_handle(self):
        '''
        Test for RateLimitError. Will remove in later version
        TO BE DEPRECATED!
        '''
        api = self.setup()
        while True:
            try:
                yield tweepy.Cursor().next()
            except tweepy.RateLimitError:
                n = 15
                print('Sleeping for {} minutes.'.format(n))
                time.sleep(n*60)



