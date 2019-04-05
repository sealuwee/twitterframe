'''
	Was going to add this to the twitter_methods.py but this will just be cleaner.
	Might make it more efficient...
	From what I know about this StreamListener class is that it is required that
	create a subclass that inherits the methods from tweepy.StreamListener.
	The source code for StreamListener can be found here:
	https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py#L31
	From there we make our actual methods that route to our commands with
	the class Stream() that has a ton of stuff in the init...
	https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py#L190
'''

from . import twitter_methods
from . import utils
import tweepy
import os
import pathlib as Path
import json
import csv
import sqlite3

class StreamListener(tweepy.StreamListener):
	'''
		Stream Listener class.
	'''
	def __init__(self):
		super(tweepy.StreamListener, self).__init__()

	def on_status(self, status):
      print(status.text)

        def on_error(self, status_code):

       	 if status_code == 420:
       		return False

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

# global variables
stream_listener = StreamListener()
TwitterMethods = twitter_methods.TwitterMethods()

class TwitterListener(StreamListener, TwitterMethods):
    '''
        Create a class that inherits StreamListener from tweepy.
        Create a Stream object
        Use api = self.setup() to set up authentication.
        I guess the goal will be to also dump the tweets from each listening session
        into an SQL database...
        example code can be found here:
        https://github.com/dataquestio/twitter-scrape/blob/master/scraper.py
    '''
    def __init__(self,api):

    	super(StreamListener, self).__init__()
    	super(TwitterMethods, self).__init__()

    	self.api = api

    def set_endpoint(self, endpoint):
    	'''
    		Sets endpoints
    	'''
    	self.endpoint = endpoint


   	def use_filter(self, trackers=list():
   		'''
   			Filter to track what you want to stream.
   		'''
   		api = self.setup()

   		stream = tweepy.Stream(auth=api, listener=StreamListener())
   		stream.filter(track=trackers)


