#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 11:58:44 2022

@author: abinesh

source of this puzzle: http://puzzles.bostonpython.com/pigolf.html
"""
import re

#reading the text file which contains the first billion digits for pi
fid= open('/home/abinesh/work/python_exercises/PythonPuzzles/pi-billion.txt','r')
text_pi = fid.read()
text_pi = text_pi[:100000] # remove the slicing if enough memory is available
text_pi = text_pi.replace('.','')

fid = open("/usr/share/dict/words",'r')
all_of_it = fid.read()
text_in_file = re.split('[^a-zA-Z0-9_\']',all_of_it)
dict_words = {}

def update_dict(dict_word, text, key):
#create the necessary dictionary key and update the values
    if key in dict_word.keys():
        dict_word[key].append(text)
    else:
        dict_word[key] = []
    return dict_word
#create a dictionary with all possible English words    
for text in text_in_file:
    #text = str.lower(re.sub("'","",text))
    text = str.lower(text)
    if len(text) == 3:
        dict_words = update_dict(dict_words, text, '3letter')
    elif len(text) == 4:
        dict_words = update_dict(dict_words, text, '4letter')
    elif len(text) == 5:
        dict_words = update_dict(dict_words, text, '5letter')
    elif len(text) == 6:
        dict_words = update_dict(dict_words, text, '6letter')
    elif len(text) == 7:
        dict_words = update_dict(dict_words, text, '7letter')
    else:
        dict_words = update_dict(dict_words, text, 'extra')

output_list = [int(text_pi[2*i]+text_pi[2*i+1]) for i in range(int(len(text_pi)/2)-1)]        
def is_valid_word(input_text, num_letters, dict_words):
    lower_lim = ord('A')
    upper_lim = ord('Z')
    words_found = {}
    for i in range(len(input_text)-num_letters+1): 
        #store each word of length num_letters         
        interm_result = input_text[i:num_letters+i]
        #the if condition will be true only if the all the ascii codes in the 3
        #letter word correspond to UPPER case
        if all(list(map(lambda x: x>=lower_lim and x<=upper_lim,interm_result))):
            word = ''.join(map(chr, interm_result))                
            if str.lower(word) in dict_words[str(num_letters)+'letter']:
                if word not in words_found.keys():
                    words_found[word] =  i*2+1
    return words_found

#highly resource intensive
#if __name__ == '__main__':
    #three_letter_words = is_valid_word(output_list, 3, dict_words) -->UMB
    #four_letter_words = is_valid_word(output_list, 4, dict_words) -->RUTS
    #five_letter_words = is_valid_word(output_list, 5, dict_words) -->TAGUS
    #six_letter_words = is_valid_word(output_list, 6, dict_words) -->CHOCKS
    #seven_letter_words = is_valid_word(output_list, 7, dict_words)