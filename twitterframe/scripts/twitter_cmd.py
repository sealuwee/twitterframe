from cmd import Cmd
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

class TwitterFrame(Cmd):
    '''
      will basically be like SQL queries
      with some added stuff like creating databases,tables, etc.
    '''
    def do_createdb(self, args):
        '''
          CREATE DATABASE name;
        '''
        pass
