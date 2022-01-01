#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:09:07 2021

@author: abinesh

this example is sourced from http://puzzles.bostonpython.com/minigolf.html
"""
import math

def hole0(your_name):
    # your_name should be a string of at least 3 letters
    # create a function that divides it into 3 strings of equal size (smallest parts first if not divisible by 3)
    # hint: check out the built-in len() function
    name_len = len(your_name)
    char_per_string = math.ceil(name_len/3)
    if name_len%3 == 0:        
        your_name_parts = [your_name[char_per_string*i:char_per_string*(i+1)] for i in range(3)]
    else:
        your_name = your_name[::-1]        
        your_name_parts_reversed = [your_name[char_per_string*i:char_per_string*(i+1)][::-1] for i in range(2)]
        your_name_parts_reversed.append(your_name[char_per_string*2:])
        your_name_parts = your_name_parts_reversed[::-1]
    return your_name_parts

def hole1(your_name_parts):
    # this function takes as input the output of the hole0() function
    # convert those 3 strings into 3 lists of their letters
    # hint: check out the builtin list() function
    letters = [list(parts) for parts in your_name_parts]
    return letters

def hole2(letters):
    # sort each of the 3 lists of letters alphabetically
    # hint: check out sorted() function and also the list.sort() method, and learn what "sorting in place" means!
    sorted_letters = [sorted(i) for i in letters]
    return sorted_letters

def hole3(sorted_letters):
    # convert each letter list into list of ASCII codes
    # hint: ord()
    ASCII = [[ord(j) for j in list_inner] for list_inner in sorted_letters]
    return ASCII

def hole4(ASCII):
    # convert these ASCII integers into strings
    # hint: str()
    ASCII_str = [[str(ascii_code) for ascii_code in list_inner] for list_inner in ASCII]
    return ASCII_str

def hole5(ASCII_str):
    # join each ASCII_str as a single string
    # hint:  look up the join() method
    joined_number_strings = [''.join(list_inner) for list_inner in ASCII_str]
    return joined_number_strings

def hole6(joined_number_strings):
    # add a decimal point to the beginning of each of the 3 strings
    # hint:  check out the builtin string operations (like '+')
    point_stuff = ''
    for joined_number in joined_number_strings:
        point_stuff += '.' + joined_number
    return point_stuff