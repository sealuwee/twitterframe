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

	def new_tweets(self, tweet):
		'''
			Publish a new tweet
		'''

		self.api.update_status(str(tweet))