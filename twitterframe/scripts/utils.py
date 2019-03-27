'''
utils.py: used to store 'global' but not so global variables.

honestly there are just a bunch of variables for emojis.
'''
import os
from pathlib import Path

baby_chick = bytes.decode(b'\xF0\x9F\x90\xA5', 'utf-8')
hatching_chick = bytes.decode(b'\xF0\x9F\x90\xA3', 'utf-8')
pidgeon = bytes.decode(b'\xF0\x9F\x90\xA6', 'utf-8')
rocket = bytes.decode(b'\xF0\x9F\x9A\x80', 'utf-8')
star = bytes.decode(b'\xF0\x9F\x8C\x9F', 'utf-8')
bread = bytes.decode(b'\xF0\x9F\x8D\x9E', 'utf-8')
party = bytes.decode(b'\xF0\x9F\x8E\x89', 'utf-8')
dash = bytes.decode(b'\xF0\x9F\x92\xA8', 'utf-8')
checkmark = bytes.decode(b'\xE2\x9C\x85 ', 'utf-8')
warning = bytes.decode(b'\xE2\x9D\x97', 'utf-8')
item = u"\U0001F95A"
egg_encode = item.encode('utf-8')
egg = bytes.decode(egg_encode, 'utf-8')

config_path = Path(os.environ['HOME']+'/.twitterframe')
