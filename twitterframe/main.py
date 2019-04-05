'''
All of the commands will be stored here.
The code will look pretty messy, since we're storing all of the commands in
this main.py file until we learn how to deploy on Flask.
'''

from .scripts.twitter_methods import TwitterWrapper
from .scripts import utils
import click
import os
from pathlib import Path
import json
import csv
import time

# global variables
# emojis go here
h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark
egg = utils.egg
sheep = utils.sheep

config_path = utils.config_path

@click.group()
@click.help_option(help='Call if you need help.')
@click.version_option()
def cli():
    '''
    Twitterframe. All the things about twitter's API that we know and love,
    packaged nicely into a command line application at the user's convenience.
    Please use this application to your liking, and leave any comments or issues
    in a pull request on GitHub.

    Documentation coming soon! Along with more commands and options!
    '''
    pass

@cli.command('setup')
def setup():
    '''
    Prompt to add Twitter API credentials into a JSON file.
    '''
    print(b, 'Setting up API...',b)

    home = Path(config_path)
    if home.exists():
        print(w*3, 'Credentials file already exists.',w*3)
        return

    print(h, '-------------------------')
    print(h, '[Step 1: Create an account on https://developer.twitter.com]')
    print(h, '-------------------------')
    access_token = click.prompt(h, 'Step 2: Twitter API Access Token: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    access_secret = click.prompt(h, 'Step 3: Secret Access Token: ',
                                 hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    consumer_key = click.prompt(h, 'Step 4: Consumer Key: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    consumer_secret = click.prompt(h, 'Step 5: Secret Consumer Key: ',
                                   hide_input=False, prompt_suffix=' ')

    print(b, 'API is almost setup',b)
    print(b, 'Just running through a quick check...', b)
    print(b, 'JSON file needs to be created to store your API keys', b)
    print(b, 'When prompted to, please specify a filename.', b)
    print(b, 'Specififying a filename creates a JSON file, if you did not create one already.', b)

    keys = {
            'access_token': access_token,
            'access_secret': access_secret,
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret
        }

    filename = Path(config_path)

    tw = open(filename, 'w+')
    tw.write(json.dumps(keys))
    tw.close()
    print(check, 'Keys have been stored in: ', filename.resolve(), check)
    print(p*25)
    print(pidgeon,'API Keys have been stored!',pidgeon)
    print(pidgeon,'API is ready to be used!',pidgeon)
    print(pidgeon,'twitterframe -h to see all commands and arguments.',pidgeon)
    print(pidgeon,'Thank you for using twitterframe, and big thanks to my contributors',pidgeon)
    print(h, '--->', b, '--->', pidgeon)
    print(p*25)

# might move this to utils.
@cli.command('reset')
def reset_creds():
    '''
    Reset your TwitterAPI credentials for easy re-use.
    '''
    home = Path(config_path)
    if home.exists():
        print(w*3, 'Attempting to reset Twitter credentials...')
        click.confirm(w*3, 'Are you sure you want to do this?',
                      abort=True)
        # after this prompt, we want to remove the file in the home directory.
        # not sure how to do that.
        home.unlink()
        print(check, 'Twitter credentials have been removed.')
        print(pidgeon, 'Please update credentials with $ twitterframe setup.')

    else:
        print('You have not setup twitterframe with your Twitter credentials.')

def reconfigure():
    '''
    reconfig: opens path to config where keys are stored.
    '''
    print(egg, 'Checking credentials for API...', egg)

    home = Path(config_path)
    if not home.exists():
        print(w*3, 'Credentials file does not exist.', w*3)
        return {}

    with open(config_path) as creds:
        credentials = json.loads(creds.read())

    print(b, 'Credentials are good to go!', b)
    return credentials

@cli.command('verify')
@click.help_option(help='Verify whether keys exist in the home directory.')
def verify():
    '''
    Verify whether keys exist in the home directory.
    '''
    home = Path(config_path).resolve()
    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    print(egg, 'Verifying TwitterAPI credentials at : {}'.format(home))

    api.verify_creds()

@cli.command('scrapelite')
# @click.option('--user', default='',
#               help='Specify a user to scrape.')
# @click.option('--out', default='tweets.csv',
#               help='Specify filename for csv.')
# @click.argument('username', required=True)
def scrapelite():
    '''
    Scrape tweets from a specified user and dump into a .csv file.
    The file will be formatted as: 'username_lite_tweets.csv'.
    '''

    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    username = click.prompt(egg, 'Input Username ', prompt_suffix=': @')

    if username == None:
        print(w*3,'Must specify a username from twitter.com')
        return

    print(check, 'Beginning to scrape user: {}'.format(username))
    output_tweets = api.get_user_tweets(username)
    time.sleep(1)
    out = '{}_lite_tweets.csv'.format(username)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text_of_tweet'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

@cli.command('scrape')
def scrape():
    '''
    DO NOT USE ! Scrape tweets and more with the full scrape function.
    '''
    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    username = click.prompt(egg, 'Input Username ', prompt_suffix=': @')

    if username == None:
        print(w*3,'Must specify a username from twitter.com')
        return

    print(check, 'Beginning to scrape user: {}'.format(username))
    output_tweets = api.get_status_objects(username)
    time.sleep(1)
    out = '{}_tweets.csv'.format(username)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text_of_tweet', 'is_quote',
                         'favorite_count', 'favorited', 'retweet_count', 'retweeted',
                         'possibly_sensitive', 'filter_level',
                         'entities_hashtags_text', 'entities_urls_expanded_url',
                         'entities_urls_description', 'entities_urls_title',
                         'entities_media_expanded_url', 'entities_media_media_type',
                         'entities_user_mentions_name', 'entities_user_mentions_screen_name',
                         'entities_user_mentions_id', 'entities_symbols_text',
                         'user_id', 'user_name', 'user_screen_name', 'user_location',
                         'user_description', 'user_verified', 'user_protected',
                         'user_followers_count', 'user_friends_count', 'user_listed_count',
                         'user_favourites_count', 'user_statuses_count', 'user_created_at',
                         'user_geo_enabled', 'user_default_profile', 'user_default_profile_image'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

@cli.command('crawl')
@click.argument('count', default=int(100), required=False)
@click.help_option(help='Count is used as an argument to pass how many ')
def crawl(count):
    '''
    Crawl tweets by specified hashtag and dump into a .csv file.
    The file will be formatted as: 'hashtag_tweets.csv'.
    '''

    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    hashtag = click.prompt(egg, 'Input Hashtag ', prompt_suffix=': #')

    if hashtag == None:
        print(w*3, 'Must specify a hashtag from twitter.com.')
        print(egg, 'Some common hashtags include #fintech, #womenintech, #metoo, etc.', pidgeon)
        return

    output_tweets = api.crawl(hashtag,count)
    time.sleep(1)
    out = '{}_hashtags.csv'.format(hashtag)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text_of_tweet'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

@cli.command('corral')
def corral():
    '''
    Corral the sheep by the user of choice.
    Corral is meant to gather data from each user object in a list of twitter users
    who follow one particular user.
    '''

    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    username = click.prompt(sheep*3, 'Whose sheep would you like to corral? ', prompt_suffix=': #')

    if username == None:
        print(w,sheep, 'You can\'t corral any sheep without providing a name for the herder...')
        print(w,sheep, 'If you need some help, just type any valid username on Twitter.')

    output_followers = api.get_followers(username)
    time.sleep(1)
    out = '{}_followers.csv'.format(username)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['user_id', 'user_name', 'user_screen_name',
                         'user_location', 'user_created_at', 'user_followers_count',
                         'user_friends_count', 'user_verified', 'user_protected',
                         'user_statuses_count'])

        writer.writerows(output_followers)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

# @cli.command('listener')
# @click.option('--hashtag',
#               help='Option to track by hashtag.')
# @click.option('--user',
#               help='Option ot track by user.')
# def listener(hashtag,user):
#     '''
#     Starts the Stream Listener used with Twitter API.
#     https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data.html#
#     DOES NOT WORK YET.
#     '''

#     credentials = reconfigure()
#     api = TwitterWrapper(*credential.values())
#     listener = TwitterListener(api=api)




