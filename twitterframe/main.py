'''
I believe I will be storing all of my commands here, and will be used to initialize the
package.
'''

# replace all print in EVERY SCRIPT that uses CLICK with print
# TODOs...
# click.echo does not work.
# Add progress bar to places.
# make scripts for 'create_csv'
# make scritps for basic twitter API usage, users, friends, etc.


from .scripts.twitter_methods import TwitterWrapper
from .scripts import utils
import click
import os
from pathlib import Path
import json
import csv

# emojis go here
h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark

# global variables
# default place to store keys ;)

config_path = utils.config_path
# create variable to store SetupAPI object

# first time using click
@click.group()
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
     # or Path('twitterframe.json').exists()
    if home.exists():
        print(w*3, 'Credentials file already exists.',w*3)
        return

    print(h, '-------------------------')
    print(h, '[Step 1: Create an account on https://developer.twitter.com]')
    print(h, '-------------------------')
    # print(h, 'Step 2: Twitter API Access Token: ', end=' ')
    access_token = click.prompt(h, 'Step 2: Twitter API Access Token: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 3: Secret Access Token: ', end=' ')
    access_secret = click.prompt(h, 'Step 3: Secret Access Token: ',
                                 hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 4: Consumer Key: ', end=' ')
    consumer_key = click.prompt(h, 'Step 4: Consumer Key: ',
                                hide_input=False, prompt_suffix=' ')
    print(h, '-------------------------')
    # print(h, 'Step 5: Secret Consumer Key: ', end=' ')
    consumer_secret = click.prompt(h, 'Step 5: Secret Consumer Key: ',
                                   hide_input=False, prompt_suffix=' ')

    # api = TwitterWrapper(access_token, access_secret, consumer_key, consumer_secret)

    print(b, 'API is almost setup',b)
    print(b, 'Just running through a quick check...', b)

    print(b, 'JSON file needs to be created to store your API keys', b)
    print(b, 'When prompted to, please specify a filename.', b)
    print(b, 'Specififying a filename creates a JSON file, if you did not create one already.', b)

    # filename = click.prompt(b, 'Filename for Twitter Credentials: ',
    #                         default=config_path, hide_input=False,)
    keys = {
            'access_token': access_token,
            'access_secret': access_secret,
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret
        }

    filename = Path(config_path)
    print(filename)
    # if '.json' not in filename.parts[-1]:
    #     print(check, 'Made file extension as .json',check)
    #     filename = filename.joinpath(filename.parts[-1]+'.json')
    tw = open(filename, 'w+')
    tw.write(json.dumps(keys))
    tw.close()
    print(check, 'Keys have been stored in: ', filename.resolve(), check)
    print(p*25)
    print(pidgeon,'API Keys have been stored!',pidgeon)
    print(pidgeon,'API is ready to be used!',pidgeon)
    print(pidgeon,'twitterframe -h to see all commands and arguments.',pidgeon)
    print(pidgeon,'Thank you for using twitterframe, and big thanks to my contributors',pidgeon)
    print(h,'--->',b,'--->',pidgeon)
    print(p*25)

# might move this to utils.
def reconfigure():
    '''
    reconfig: opens path to config where keys are stored.
    '''
    print(b, 'Reconfiguring API...',b)

    home = Path(config_path)
    # or Path('twitterframe.json').exists()
    if not home.exists():
        print(w*3, 'Credentials file does not exist.', w*3)
        return {}

    with open(config_path) as creds:
        credentials = json.loads(creds.read())

    return credentials

@cli.command('scrape')
@click.option('--user', default='',
              help='Specify a user to scrape.')
@click.option('--out', default='tweets.csv',
              help='Specify filename for csv.')
@click.argument('username', required=True,
                )
def scrape(user, out, username):
    '''
    Scrape tweets from a specified user and dump into a .csv file.
    The file will be formatted as: 'username_tweets.csv'.
    Default username is ThePSF (Python Software Foundation).
    '''
    credentials = reconfigure()
    api = TwitterWrapper(*credentials.values())

    output_tweets = api.get_tweets(username)

    with open(out, 'w') as tw:

        writer = csv.writer(tw)
        writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(output_tweets)

    out_path = Path(out).resolve()
    print(pidgeon, check, 'CSV created at {}'.format(out_path))
