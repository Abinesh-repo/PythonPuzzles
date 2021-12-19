#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:11:39 2021

@author: abinesh
"""
import re
poem='''a narrow fellow in the grass
    occasionally rides;
    you may have met him, did you not,
    his notice sudden is.
    
    the grass divides as with a comb,
    a spotted shaft is seen;
    and then it closes at your feet
    and opens further on.
    
    he likes a boggy acre,
    a floor too cool for corn.
    yet when a child, and barefoot,
    i more than once, at morn,
    
    have passed, i thought, a whip-lash
    unbraiding in the sun,
    when, stooping to secure it,
    it wrinkled, and was gone.
    
    several of nature's people
    i know, and they know me;
    i feel for them a transport
    of cordiality;
    
    but never met this fellow,
    attended or alone,
    without a tighter breathing,
    and zero at the bone.'''
def bostonpython_peotry(riddle, text): 
    dict_words = {}
    for vals_words in re.split('\W+',text):
     for vals in vals_words:
        if dict_words.get(vals) is None:
            dict_words[vals] = 1
        else:
            dict_words[vals] += 1
    print("The letters available in the poem and their number of occurences are :", dict_words)
    rev_dict_words = {}
    for keys, values in dict_words.items():
        rev_dict_words[values] = keys   
    answer = ''
    for num in riddle:
        answer += rev_dict_words[num]    
    return answer, dict_words, rev_dict_words

def find_all_riddles(dict_words, text):
    riddle_4_word = []
    for t in text:
        if t not in dict_words.keys():
            return None
        else:
            riddle_4_word.append(dict_words[t])
    return riddle_4_word

answer, dict_words, rev_dict_words = bostonpython_peotry([1,56,7,29,42], poem)
fid = open("/usr/share/dict/words",'r')
all_of_it = fid.read()
text_in_file = re.split('[^a-zA-Z0-9_\']',all_of_it)
longest_word = ''
for text in text_in_file:
    if find_all_riddles(dict_words, text) is not None:
        if len(text)>len(longest_word):
            longest_word = text
    
            
    
    