'''
I believe I will be storing all of my commands here, and will be used to initialize the
package.
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
    print(b, 'Checking credentials for API...', b)

    home = Path(config_path)
    if not home.exists():
        print(w*3, 'Credentials file does not exist.', w*3)
        return {}

    with open(config_path) as creds:
        credentials = json.loads(creds.read())

    return credentials

@cli.command('verify')
def verify():

    home = Path(config_path).resolve()
    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    print(egg, 'Verifying TwitterAPI credentials at : {}'.format(home))

    api.verify_creds()

@cli.command('scrape')
# @click.option('--user', default='',
#               help='Specify a user to scrape.')
# @click.option('--out', default='tweets.csv',
#               help='Specify filename for csv.')
# @click.argument('username', required=True)
def scrape():
    '''
    Scrape tweets from a specified user and dump into a .csv file.
    The file will be formatted as: 'username_tweets.csv'.
    '''

    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    username = click.prompt(egg, 'Input Username ', prompt_suffix=': ')

    if username == None:
        print(w*3,'Must specify a username from twitter.com')
        return

    print(check, 'Beginning to scrape user: {}'.format(username))
    output_tweets = api.get_user_tweets(username)
    time.sleep(1)
    out = '{}_tweets.csv'.format(username)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

@cli.command('crawl')
@click.argument('hashtag', required=True)
def crawl(hashtag):
    '''
    Crawl tweets by specified hashtag and dump into a .csv file.
    The file will be formatted as: 'hashtag_tweets.csv'.
    '''
    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    output_tweets = api.crawl(hashtag)
    time.sleep(1)
    out = '{}_hashtags.csv'.format(hashtag)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['created_at', 'text'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))

