'''
    twitterAPI_auth_input :

    Script allows user to input their access tokens, and consumer API keys
    from the command line.
    Used as a first step to creating pandas dataframes from twitter things!

'''

import tweepy

# store OAuth credentials from input in command line.

twitter_emoji = bytes.decode(b'\xF0\x9F\x90\xA3','utf-8')

access_token = "XxXxXxxXXXxxxxXXXxXX"
access_token_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
consumer_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
consumer_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"
