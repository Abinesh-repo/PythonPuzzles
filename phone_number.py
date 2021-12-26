#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:58:58 2021

@author: abinesh

this python code is sourced from http://puzzles.bostonpython.com/phonenumbers.html

"""

lookup_table = {"2": "abc", 
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"}

#question 1 
# phone number to be of the form 1-617-XXX-XXXX
lookup_dict = {}
for key, value in lookup_table.items():
    lookup_dict[key] = list(value)

name = 'Mahershalalhashbaz'
vowels = list('aeiou')
name = str.lower(name)

phone_num = "1-617-"
def convert_name_to_num(lookup_dict, name):
    name = list(name)
    phone=''
    if len(name) == 7:
        for text in name:
            phone+=[key for key,value in lookup_dict.items() if text in value][0]
        print('inside len=7')
    if len(name) <7 :
        len_shortage = 7-len(name)
        phone+='r'*len_shortage
        phone+=''.join(name)
        phone = convert_name_to_num(lookup_dict, phone)
        #for text in name:
        #   phone+=[key for key,value in lookup_dict.items() if text in value][0]
    if len(name) > 7 and len(name)<15:
        index_vowels = [ind for ind, val in enumerate(name) if val in vowels]
        index_vowels = index_vowels[::-1]
        for i in index_vowels:
            name.pop(i)
            phone = convert_name_to_num(lookup_dict, name)
            print("name longer than 7 characters", name)
            if len(name)<=7:
                break   
    if len(name) > 15:
        first4 = name[:4]
        last3 = name[-3:]
        name = ''.join(first4+last3)
        print('the shortened name is ', name)
        phone = convert_name_to_num(lookup_dict, name)
    return phone

phone_num += convert_name_to_num(lookup_dict, name)
phone_num = phone_num[:-4] + '-' + phone_num[-4:]


#question 2