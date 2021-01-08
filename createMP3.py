#!/usr/bin/env python3

"""createMP3.py: Create a random MP3 based on other MP3s."""

__author__ = "Robin Van der Gucht"

import configparser
import os, sys
import random
import string

config = configparser.ConfigParser()
config.read('settings.ini')
directory_mp3 = config['DEFAULT']['directory_mp3']
time = config['DEFAULT']['time']
length = int(config['DEFAULT']['length'])


def get_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def give_random_name():
   raise NotImplementedError("doesn't work yet")


give_random_name()
