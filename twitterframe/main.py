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

# replace all click.echo in EVERY SCRIPT that uses CLICK with click.echo


import scripts.twitter_auth as auth
import scripts.utils as utils
import click

h = utils.hatching_chick
b = utils.baby_chick
p = utils.party
pidgeon = utils.pidgeon

#create SetupAPI object to pass for commands?

api = auth.SetupAPI()


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
@click.argument('filename', type=click.Path('w'),
                default='twitter_credentials.json',
                required=False, help='Specify a filename for your Twitter credentials.')
def auth(setup):
    auth.check_auth()

def main():


    click.echo(b, 'Setting up API...',b)
    auth.check_auth()
    click.echo(b, 'API is almost setup',b)
    click.echo(b, 'JSON file needs to be created to store your API keys', b)
    click.echo(b, 'When prompted to, please specify a filename.', b)
    #add input for filename...
    click.echo(b, 'Filename to store Twitter credentials: ', end=' ')
    filename=input()

    if filename == None:
        click.echo(b, 'Please specify a valid name for the keys file. ')
        click.echo(b,'Filename to store Twitter credentials: ', end=' ')
        filename=input()

    else:
        pass

    api.to_json(filename)
    click.echo(p*25)
    click.echo(pidgeon,'API Keys have been stored!',pidgeon)
    click.echo(pidgeon,'API is ready to be used!',pidgeon)
    click.echo(pidgeon,'twitterframe -h to see all commands and arguments.',pidgeon)
    click.echo(pidgeon,'Thank you for using twitterframe, and big thanks to my contributors',pidgeon)
    click.echo(h,'--->',b,'--->',pidgeon)
    click.echo(p*25)

    #After this line, we can either click.echo all of the helper methods
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

        click.echo('Please sign up for a Twitter developer account.')

