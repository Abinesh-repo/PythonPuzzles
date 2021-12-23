#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:29:56 2021

@author: abinesh

This is a puzzle sourced from http://puzzles.bostonpython.com/hotdate.html
"""

from itertools import zip_longest
import itertools
import operator
import copy
def output_gen(output,combination_num, num_string, null_string):
    #create a list of tuples containing possible indices to apply \s
    iteration_index = list(itertools.combinations(range(len(null_string)),
                                                  combination_num))
    for i_tuple in iteration_index:
        null_string_w_none = copy.copy(null_string)
        for k in i_tuple:
            null_string_w_none[k] = '' #replace space
        #combine both the num_string and null_string_w_none lists to create a list of tuples
        data_tuple = list(zip_longest(num_string,null_string_w_none,fillvalue=''))
        #concatenate the tuple into a list of strings
        data_tuple_map = list(itertools.starmap(operator.concat,data_tuple))
        #combine the list of strings to give a single string
        final_string = ''.join(map(str,data_tuple_map))
        output.append(final_string)
    return output

num_string = list(str(123456789)) #converting to a list of characters
emp_string = list(' '*(len(num_string)-1)) #because there are a total of 8 locations where
                          # spaces can be added and removed
#generates all the expressions with spaces between them
puzzle1 = []
for combination_num in range(0,len(emp_string)):
    puzzle1 = output_gen(puzzle1, combination_num, num_string, emp_string)


all_expressions = []
#create a default list of + which could be replaced with - at specific location
operator_string = list('+'*(len(num_string)-1))
operator_list = []
output=[]
#generates all possible expressions with operators +/- between them
for combination_num_operator in range(0, len(operator_string)):
    #create a list of permutations as ordering of operator is important
    iteration_operator = list(itertools.permutations(range(len(operator_string)), combination_num_operator))
    for o_tuple in iteration_operator:
        operator_string_w_minus = copy.copy(operator_string)
        for k_op in o_tuple:
            #apply - operator only at specific index locations
            operator_string_w_minus[k_op] = '-'   
        operator_list.append(operator_string_w_minus)
#saving as a set so that the operators do not repeat multiple times
operator_set = set(tuple(l) for l in operator_list)
#gather all the possible expressions
for operator_string_w_minus in operator_set:
  operator_string_w_minus = list(operator_string_w_minus)
  for combination_num in range(0,len(operator_string)):
      all_expressions = output_gen(all_expressions, combination_num, num_string, operator_string_w_minus)

#this contains all the possible expressions and their sum
all_exp_dict = {} 
for iter_dict in all_expressions:
    all_exp_dict[iter_dict] = eval(iter_dict)
#evaluate the expressions and store them in a dictionary    
puzzle2 = {}
for op_st in all_exp_dict.keys():
    if eval(op_st) in puzzle2.keys():
        puzzle2[eval(op_st)].append(op_st)
    else:
        puzzle2[eval(op_st)] = [op_st]
#the expression that yield a sum of 100
sum_to_100 = puzzle2[100]

#generates a dictionary to store the data in a histogram format
puzzle3_histogram = {}
for summation in puzzle2.keys():
  puzzle3_histogram[summation] = len(puzzle2[summation])