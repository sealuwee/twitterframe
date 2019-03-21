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

twitter_emoji = bytes.decode(b'\xF0\x9F\x90\xA3','utf-8')

access_token = "XxXxXxxXXXxxxxXXXxXX"
access_token_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
consumer_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
consumer_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"
