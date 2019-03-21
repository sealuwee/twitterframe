'''
cli.py

Stores all command line arguments.

More to be added later.

'''

####
####
## TODOS:
## Create functions that just work.
## Functional functions that work.
## Revisit this CLI.py for command line functionality
####

import click

@click.group()

@click.command()
@click.help_option('-h','--help')

def main():
    pass

if __name__ == '__main__':
    main()