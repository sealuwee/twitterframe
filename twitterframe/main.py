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

from scripts.twitter_auth import *
from scripts.twitter_trends import *
from scripts.utils import *

h = hatching_chick
b = baby_chick


print(h)
print(b)

def main():

    try:
        print(h,'Setting up API')
        SetupAPI().check_auth()

    except ValueError:

        print('Error has been raised.')

    try:

        assert len(config.access_token) == 20
        assert len(config.access_secret) == 42
        assert len(config.consumer_key) == 50
        assert len(config.consumer_secret) == 39

    except ValueError:

        print('Please sign up for a Twitter developer account.')

