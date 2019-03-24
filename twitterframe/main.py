'''
I believe I will be storing all of my commands here, and will be used to initialize the
package.
'''
# TODOS: start importing scripts
# create new classes for things i guess
# go to bed early haha jk
# don't play videogames
# use twitter more often lol
# start working on click commands and groups
# add asserts trys and exceptions to this file

# TODOs for the MVP?
# start with basic click commands
# click is the argparser making command line
# interactions very easy to understand.
# so basically we want to be making commands now.

# replace all print in EVERY SCRIPT that uses CLICK with print
# TODOs...
# click.echo does not work.
# Add progress bar to places.
# make scripts for 'create_csv'
# make scritps for basic twitter API usage, users, friends, etc.


import twitterframe.scripts.twitter_auth as auth
import twitterframe.scripts.utils as utils
import click

# emojis go here
h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon
w = utils.warning
check = utils.checkmark

# create variable to store SetupAPI object

api = auth.SetupAPI()

# first time using click
@click.group()
def cli():
    '''
    Making this the main group function for simplicity sake to see how easy
    it is to make this kind of application.
    '''
    pass

@cli.command()
@click.option('-edit', default=None,
              help='Option to edit the keys in your file.')
@click.argument('file')
def setup(edit, file):

    print(b, 'Setting up API...',b)
    auth.check_auth()
    print(b, 'API is almost setup',b)
    print(b, 'Just running through a quick check...', b)
    try:

        assert len(api.access_token) != None
        assert len(api.access_secret) != None
        assert len(api.consumer_key) != None
        assert len(api.consumer_secret) != None
        # assert len(api.access_token) == 20
        # assert len(api.access_secret) == 42
        # assert len(api.consumer_key) == 50
        # assert len(api.consumer_secret) == 39

    except ValueError:
        print(w*3, 'You did not enter valid keys.', w*3)
        print('Please sign up for a Twitter developer account.')

    print(b, 'JSON file needs to be created to store your API keys', b)
    print(b, 'When prompted to, please specify a filename.', b)
    print(b, 'Type the following command in the command line if a prompt does not show up.', b)
    print(b, '>>> twitterframe -n creds <<<', b)
    print(b, 'sans the emojis.', b)
    print(b, 'Specififying a filename creates a JSON file, if you did not create one already.', b)

    filename=click.prompt(b, 'Filename for Twitter Credentials: ', b)

    if filename == None:
        print(w*3, 'Please specify a valid name for the keys file. ',w*3)
        filename=click.prompt(w*3,'Filename to store Twitter credentials: ', w*3)

    api.to_json(filename)

    print(p*25)
    print(pidgeon,'API Keys have been stored!',pidgeon)
    print(pidgeon,'API is ready to be used!',pidgeon)
    print(pidgeon,'twitterframe -h to see all commands and arguments.',pidgeon)
    print(pidgeon,'Thank you for using twitterframe, and big thanks to my contributors',pidgeon)
    print(h,'--->',b,'--->',pidgeon)
    print(p*25)

# def main():


#     print(b, 'Setting up API...',b)
#     auth.check_auth()
#     print(b, 'API is almost setup',b)
#     print(b, 'JSON file needs to be created to store your API keys', b)
#     print(b, 'When prompted to, please specify a filename.', b)
#     #add input for filename...
#     print(b, 'Filename to store Twitter credentials: ', end=' ')
#     filename=input()

#     if filename == None:
#         print(b, 'Please specify a valid name for the keys file. ')
#         print(b,'Filename to store Twitter credentials: ', end=' ')
#         filename=input()

#     else:
#         pass

#     api.to_json(filename)
#     print(p*25)
#     print(pidgeon,'API Keys have been stored!',pidgeon)
#     print(pidgeon,'API is ready to be used!',pidgeon)
#     print(pidgeon,'twitterframe -h to see all commands and arguments.',pidgeon)
#     print(pidgeon,'Thank you for using twitterframe, and big thanks to my contributors',pidgeon)
#     print(h,'--->',b,'--->',pidgeon)
#     print(p*25)

#     After this line, we can either print all of the helper methods
#     Or we can show an example of how to get started with using
#     twitterframe from the commandline.

#     try:

#         assert len(api.access_token) != None
#         assert len(api.access_secret) != None
#         assert len(api.consumer_key) != None
#         assert len(api.consumer_secret) != None
#         # assert len(api.access_token) == 20
#         # assert len(api.access_secret) == 42
#         # assert len(api.consumer_key) == 50
#         # assert len(api.consumer_secret) == 39

#     except ValueError:

#         print('Please sign up for a Twitter developer account.')
