# _*_ coding: utf-8 _*_

"""This module provides hello_world_function."""

import time

def hello_world_function(string):
    for character in string:
        print(character, end='')
        time.sleep(0.50)
