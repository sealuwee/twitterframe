'''
twitter-trends.py : uh
'''
#

import twitterframe.scripts.utils as utils
import tweepy
import json
import csv
from pathlib import Path

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark

class TwitterMethods(object):
    '''
    subclass of SetupAPI
    TwitterTrends class.
    Methods that I want to use:
    Get Twitter Trends by location
    Get top 10 Twitter Trends
    I guess just the get methods from the API, just as methods from this class...
    '''

    def __init__(self,
                 access_token,
                 access_secret,
                 consumer_key,
                 consumer_secret):

        cwd = Path().cwd()
        parent_path = cwd.parents[1]

        for file in parent_path.glob('*.json'):
            if file.exists() is True:
                creds_path = file

        with open(creds_path, encoding='utf-8') as creds:
            credentials = json.loads(creds.read())

        self.access_token = credentials['access_token']
        self.access_secret = credentials['access_secret']
        self.consumer_key = credentials['consumer_key']
        self.consumer_secret = credentials['consumer_secret']

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

    def get_tweets(self, username=''):

        '''
            Code redesigned from yanofsky:
            https://gist.github.com/yanofsky/5436496
            and the Python 3.x version:
            https://gist.github.com/gabrielsoule/638201ac0cc12828d3cde69035a25336
        '''

        api = self.setup()

        tweets = []

        new_tweets = api.user_timeline(sceen_name=username, count=200)

        tweets.extend(new_tweets)

        oldest_tweets = tweets[-1].id - 1

        while len(new_tweets) > 0:

            print(pidgeon, 'Getting tweets before {}'.format(oldest_tweets))

            new_tweets = api.user_timeline(screen_name=username, count=200,max_id=oldest_tweets)

            tweets.extend(new_tweets)

            oldest_tweets = tweets[-1].id - 1

            print(pidgeon, '... {} Amount of tweets downloaded so far'.format(len(tweets)))

        output_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

        with open('{}_tweets.csv'.format(username), 'w') as tw:

            writer = csv.writer(tw)
            writer.writerow(['id', 'created_at', 'text'])
            writer.writerows(output_tweets)

        pass



