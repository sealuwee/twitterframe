'''

	The beginnings of a a basic twitter bot to just follow and unfollow people.
	For testing purposes, and some machine learning in the future.

'''

from . import twitter_methods
from . import twitter_listener
from . import utils
import tweepy
import os
import pathlib as Path 

class RobotActions:

	'''
		Some simple actions to made with Twitter.
	'''

	def __init__(self, api):

		self.api = api
		self.followers = self.get_followers(self.api.me().screen_name)

	def get_api(self):

		return self.api

	def get_followers(self, account_name):
        """Return a list of all the followers of an account"""
        followers = []
        for page in tweepy.Cursor(self.api.followers_ids, screen_name=str(account_name)).pages():
            followers.extend(page)
        return followers

    def get_user_from_tweet(self, tweet_id):
        """Return an User object from a given tweet"""
        tweet = self.get_tweet(tweet_id)
        return tweet.user

    def get_tweet(self, tweet_id):
        """Return a Status object from a tweet ID"""
        return self.api.get_status(tweet_id)

	def new_tweets(self, tweet):
		'''
			Publish a new tweet
		'''
		self.api.update_status(str(tweet))

	def follow_account(self, user_id):

		if not self.api.get_user(user_id) in self.followers:
			self.api.create_friendship(user_id)

	