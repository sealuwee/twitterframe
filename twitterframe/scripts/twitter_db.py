'''
twitter_db file to house the class method for working with
tweepy._json files and adding them to a database of choice.

twitter_db will be the first script I use with the new shell in twitter_cmd
and will only be accessible from the shell environment.
'''

from . import utils
import tweepy
import json
import csv
import os
from pathlib import Path
import time
from tqdm import tqdm
import psychopg2 as pg
import crayons
import SQLAlchemy
from SQLAlchemy import create_engine



