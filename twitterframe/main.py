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

import scripts.twitter_auth as auth
import scripts.utils as utils
import click

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
wj = utils.will_jarvis

def main():

    api = auth.SetupAPI()


    print(h,'Setting up API...',h)
    auth.check_auth()
    print(b,'API is almost setup',b)
    print(b,'JSON file needs to be created to store your API keys', b)
    print(b,'When prompted to, please specify a filename.',b)
    #add input for filename...
    print(wj,'Filename to store Twitter credentials: ', end=' ')
    filename=input()

    if filename == None:
        print(wj, 'Please specify a valid name for the keys file. ')
        print(wj,'Filename to store Twitter credentials: ', end=' ')
        filename=input()

    else:
        pass

    api.to_json(filename)
    print(p*20)
    print(b,'API Keys have been stored!',b)
    print(b,'API is ready to be used!',b)
    print(b,'twitterframe -h to see all commands and arguments.',b)
    print(b,'Thank you for using twitterframe, and big thanks to my contributors',b)
    print(h,'--->',b,'--->',wj)
    print(p*20)

    #After this line, we can either print all of the helper methods
    #Or we can show an example of how to get started with using
    #twitterframe from the commandline.

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

        print('Please sign up for a Twitter developer account.')

