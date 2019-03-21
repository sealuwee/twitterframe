'''
Authorize your twitter credentials with this script

Only runs if you credentials were not initialized on setup.
'''

##TODOs: Create some type of if statement that checks whether or not there is
##       and valid keys in the config.py file
##       We can try doing it by import config
##       and call each key with config.consumer_key
##       config.access_token, etc.
##       AND if they are valid, **Meaning** they are actually strings
##       Pass and move on to actually using twitterframe.
##       I feel like this step is going to be the one step that defines
##       The whole process of the project and the flow of how it will work.
##       So MAKE IT WORK <3


import config
import tweepy
import time

def check_auth():

    # store OAuth credentials from input in command line.

    twitter_emoji = bytes.decode(b'\xF0\x9F\x90\xA3','utf-8')

    print(twitter_emoji, '-------------------------')
    print('Step 1: Create account on https://developer.twitter.com')
    print(twitter_emoji, '-------------------------')
    print('Step 2: What is the name of your app?: ', end=' ')
    app_name = input()
    print(twitter_emoji, '-------------------------')
    print('Step 3: Twitter API Access Token: ', end=' ')
    access_token = input(twitter_emoji, "Twitter API Access Token : ")
    print(twitter_emoji, '-------------------------')
    print('Step 4: Secret Access Token: ', end=' ')
    access_token_secret = input(twitter_emoji, "Secret Access Token : ")
    print(twitter_emoji, '-------------------------')
    print('Step 5: Consumer Key: ', end=' ')
    consumer_key = input(twitter_emoji, "Consumer Key : ")
    print(twitter_emoji, '-------------------------')
    print('Step 6: Secret Consumer Key: ', end=' ')
    consumer_secret = input(twitter_emoji, "Secret Consumer Key : ")

    return app_name, access_token, access_token_secret, consumer_key, consumer_secret

app_name, access_token, access_token_secret, consumer_key, consumer_secret = check_auth()

# pass OAuth details to tweepy handler.
time.sleep(2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)
