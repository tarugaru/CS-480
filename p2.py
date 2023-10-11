# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:40:08 2023

@author: tallu
"""
#def in_parentheses(string):   
user_input = input("evaluate:")
string = "(" + user_input + ")"
print(string)
iterator = 0
while "(" in string:
    iterator = 0
    cp = 0
    for element in string:
        if element == "(":
            cp = iterator
        if element == ")":
            eval_expression = string[cp+1:iterator]
            print(eval_expression)
            string = string.replace(string[cp:iterator+1],"eval")
            print(string)
            break
        iterator +=1