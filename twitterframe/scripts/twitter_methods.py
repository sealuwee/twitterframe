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
egg = utils.egg
sheep = utils.sheep

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
            p_bar = tqdm(user_tweets, ascii=False, total=limit, desc='Harvesting Tweets from user: {}'.format(username),
                         unit=' tweets')

            for i, tweet in enumerate(p_bar):
                p_bar.update(1)
                if i > limit:
                    break

                tweets.append([username, tweet.id_str, tweet.created_at,
                               tweet.text.encode('utf-8')
                               ])
                # tweet.is_quote_status,
                # tweet.is_quote_status,
                # tweet.favorite_count, tweet.favorited,
                # tweet.retweet_count, tweet.retweeted,
                # tweet.possibly_sensitive

            print(pidgeon, 'Downloaded {} tweets from user: {}'.format(len(tweets), username))

        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Ending loop.")
            print(w, twrle)

        return tweets

    def get_status_objects(self, username):
        '''
        Highly recommended to use this if you want to pull ALL objects,
        including entities.
        '''
        api = self.setup()

        try:
            tweets = []
            statuses = tweepy.Cursor(api.user_statuses, id=username,
                                     include_entites=True).items()
            p_bar = tqdm(statuses, ascii=False, desc='Harvesting Data from user: {}'.format(username))

            for i, tweet in enumerate(p_bar):
                p_bar.update(1)

                tweets.append([username, tweet.id_str, tweet.create_at, tweet.text.encode('utf-8'),
                               tweet.entities.hashtags.text.encode('utf-8'), tweet.entities.urls.expanded_url,
                               tweet.entities.urls.description, tweet.entities.urls.title,
                               tweet.entities.media.expanded_url, tweet.entities.media.media_type,
                               tweet.entities.user_mentions.name, tweet.entities.user_mentions.screen_name,
                               tweet.entities.user_mentions.id_str, tweet.entities.symbols.text.encode('utf-8'),
                               tweet.user.id_str, tweet.user.name, tweet.user.screen_name,
                               tweet.user.location, tweet.user.description,
                               tweet.user.verified, tweet.user.protected,
                               tweet.user.followers_count, tweet.user.friends_count,
                               tweet.user.listed_count, tweet.user.favourites_count,
                               tweet.user.statuses_count, tweet.user.created_at,
                               tweet.user.geo_enabled, tweet.user.default_profile,
                               tweet.user.default_profile_image])

            print(pidgeon, 'Downloaded {} tweets from {} during this request.'.format(len(tweets),username))
        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Ending loop.")
            print(w, twrle)

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
                                       lang='en',
                                       ).items(limit)

            print(h, 'Collecting tweets from #{}'.format(hashtag), pidgeon)

            p_bar = tqdm(hashtag_tweets, ascii=False, total=limit, desc='Harvesting Tweets from hashtag: {}'.format(hashtag),
                         unit=' tweets')

            for count, tweet in hashtag_tweets:
                p_bar.update(1)
                if count > limit:
                    break

                tweets.append([ hashtag, tweet.id_str, tweet.created_at,
                                tweet.text.encode('utf-8')
                               ])

            print(pidgeon, '{} Downloaded tweets, with the hashtag {} !'.format(len(tweets),hashtag))

        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Enjoyding loop.")
            print(w, twrle)

        return tweets

    def get_followers(self, username):
        '''
            Gather a list of followers for a specified user..
            :username: input username from command line.

            returns: data from each user that followers :username:.
        '''

        api = self.setup()

        try:
            #something I don't have many of.. :(
            followers = []
            print(egg, 'Collecting list of followers...')

            find_followers = tweepy.Cursor(api.followers, id=username, cursor=-1).items()

            p_bar = tqdm(find_followers, ascii=False, desc='Harvesting the IDs of who {} follows!'.format(username))

            for follower in enumerate(p_bar):

                p_bar.update(1)

                followers.append([follower.user.id_str, follower.user.name, follower.user.screen_name,
                                follower.user.location, follower.user.created_at, follower.user.followers_count,
                                follower.user.friends_count, follower.user.verified, follower.user.protected,
                                follower.user.statuses_count])

        except tweepy.error.TweepError as twerp:
            print(w,twerp)

        except tweepy.error.RateLimitError as twrle:
            print(w, "Reached Twitter rate limit. Enjoyding loop.")
            print(w, twrle)

        print(pidgeon, '{} people and robots are following {} !'.format(len(followers), username))

        #something I wish I could do.
        return followers

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



