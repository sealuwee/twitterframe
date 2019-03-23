'''
make-dataframe.py : this is the script that
                    constructs a dataframe from whatever script(s) is(are) called.
'''

#
#
#
# ADD THIS FUNCTION TO TWITTER AUTH CLASS
#
#
#

import tweepy
import config
import pandas
import click
import csv

twitter_emoji = config.twitter_emoji

def get_tweets(username):

    '''
        Code redesigned from yanofsky:
        https://gist.github.com/yanofsky/5436496
        and the Python 3.x version:
        https://gist.github.com/gabrielsoule/638201ac0cc12828d3cde69035a25336
    '''

    api = config.api

    tweets = []

    new_tweets = api.user_timeline(sceen_name=username, count=200)

    tweets.extend(new_tweets)

    oldest_tweets = tweets[-1].id - 1

    while len(new_tweets) > 0:

        print(twitter_emoji, 'Getting tweets before {}'.format(oldest_tweets))

        new_tweets = api.user_timeline(screen_name=username, count=200,max_id=oldest_tweets)

        tweets.extend(new_tweets)

        oldest_tweets = tweets[-1].id - 1

        print(twitter_emoji, '... {} Amount of tweets downloaded so far'.format(len(tweets)))

    output_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    with open('{}_tweets.csv'.format(username), 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(output_tweets)

    pass

