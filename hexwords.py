#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:25:09 2022

@author: abinesh

Hex words puzzle sourced from : http://puzzles.bostonpython.com/hexwords.html
"""
import re
#dictionary_loc = "/usr/share/dict/words"
dictionary_loc = "/home/abinesh/work/python_exercises/PythonPuzzles/words_alpha.txt"
fid_dict = open(dictionary_loc,'r')
dictionary_data = re.split('[\n\s]', fid_dict.read())
dictionary_data_processed = set(map(lambda x: str.lower(re.sub("[\s'']","",x)),dictionary_data))
#working with sets because they easily handle intersection operations
hex_letters = set(['a','b','c','d','e','f'])

final_list = dict()
for text_iter in dictionary_data_processed:
    set_of_text_iter = set(text_iter)
    if set_of_text_iter.issubset(hex_letters):
        final_list[text_iter] = len(text_iter)
        
#to print the text of longest length
print(max(final_list,key=lambda x: final_list[x]))
