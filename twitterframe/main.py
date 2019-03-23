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

import scripts.twitter_auth as auth 
import scripts.utils as utils

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party

print(h)
print(b)

def main():

    try:
        print(h,'Setting up API...',h)
        auth.check_auth()
        print(p*20)
        print(b,'API is almost setup',b)
        print(b,'JSON file needs to be created to store your API keys', b)
        print(b,'When prompted to, please specify a filename.',b)
        #add so
        print(p*20)
        #After this line, we can either print all of the helper methods
        #Or we can show an example of how to get started with using
        #twitterframe from the commandline.
    except ValueError:

        print('Error has been raised.')

    try:

        assert len(config.access_token) == 20
        assert len(config.access_secret) == 42
        assert len(config.consumer_key) == 50
        assert len(config.consumer_secret) == 39

    except ValueError:

        print('Please sign up for a Twitter developer account.')

