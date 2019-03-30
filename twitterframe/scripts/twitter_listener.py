'''
	Was going to add this to the twitter_methods.py but this will just be cleaner.
	Might make it more efficient, who knows!
'''

from . import twitter_methods
from . import utils
import tweepy
import os
import pathlib as Path 
import json
import csv
import sqlite3

TwitterMethods = twitter_methods.TwitterMethods()

class StreamListener(tweepy.StreamListener):
	'''
		Stream Listener class. 
	'''
	def __init__(self):
		super(tweepy.StreamListener, self).__init__()
		pass

	def on_status(self, status):
		pass

class TwitterListener(StreamListener, TwitterMethods):
    '''
        Create a class that inherits StreamListener from tweepy.
        Create a Stream object
        Use api = self.setup() to set up authentication.
    '''
    def __init__(self):

    	super(StreamListener, self).__init__()
    	super(TwitterMethods, self).__init__()

    	pass

    def on_status(self, status):

        print(status.text)

        	def on_error(self, status_code):

        if status_code == 420:

        	return False

    def set_endpoint(self, endpoint):
    	'''
    		Sets endpoints
    	'''
    	self.endpoint = endpoint

   	def on_data(self, raw_data):
   		'''
   			When data arrives to a method that dispatches the event to the right person.
   		'''
   		data = json.loads(raw_data)

   		if 'direct_message' in data:
   			direct_message = data['direct_message']
   			if direct_message['sender']['id'] != self.endpoint._api.me().id:
   				return self.endpoint.process_new_direct_message(direct_message)

   		elif data.get('event','') == 'follow':
   			return self.endpoint.process_new_follower(data['source'])

   	def use_filter(self, tracker):
   		'''
   			Filter to track what you want to stream.
   		'''
   		api = self.setup()

   		stream = tweepy.Stream(auth=api, listener=)
