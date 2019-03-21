'''
    twitterAPI_auth_input :

    Script allows user to input their access tokens, and consumer API keys
    from the command line.
    Used as a first step to creating pandas dataframes from twitter things!

'''

# store OAuth credentials from input in command line.

# we want the goal to be to rewrite this config.py file from the command line.
# where we can call config.access_token anywhere in the package.
# and we want to write a script that writes these keys if there are no keys in this file.
# Now how do we do that? LOL

import tweepy

twitter_emoji = bytes.decode(b'\xF0\x9F\x90\xA3','utf-8')

access_token = "XxXxXxxXXXxxxxXXXxXX"
access_token_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
consumer_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
consumer_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# class Configuration(object):

#     def __init__(self):

#         self.temp_folder_path = None
#         self.username = ""
#         self.app_name = ""
#         self.access_token = {}
#         self.access_token_secret = {}
#         self.consumer_key = {}
#         self.consumer_secret = {}

#     def get_access_token(self):

#         return

#     def get_access_token_secret(self):

#         return

#     def get_consumer_key(self):

#         return

#     def get_consumer_secret(self):

#         return

#     def auth_settings(self):
#         '''
#         return: Auth settings information dictionary.
#         '''
#         return {

#             'OAuthKeys':
#                 {
#                     'access_token': self.access_token,
#                     'access_token_secret': self.access_token_secret,
#                     'consumer_key': self.consumer_key,
#                     'consumer_secret': self.consumer_secret,
#                 }
#         }