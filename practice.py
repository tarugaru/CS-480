# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:10:58 2023

@author: tallu
"""
ex_list = []
postfix = []
operators = []

def evalExp(ex_list):
    print(ex_list)
    validExp = True
    if ex_list[0] == "-":
        element = ex_list.pop(0)
        validExp = getNumVal(element)
    while len(ex_list)>0 and validExp:
        element = ex_list.pop(0)
        if element.isdigit():
            validExp = getNumVal(element)
    print(postfix)
    print(operators)

def getNumVal(element):    
    #parse through ex_list to get the number together
    char = None
    expFlag = 0
    decFlag = 0
    if len(ex_list)>0:
        char = ex_list[0]
        print("char: " + char)
    while char != None:
        if char.isdigit() or char=="." or char=="^":
            if char == "^":
                expFlag += 1
            element = element + char
            ex_list.pop(0)
            if char == ".":
                decFlag +=1
            if len(ex_list)> 0:
                char = ex_list[0]
            else:
                char = None
        else:
            char = None
    if expFlag == 1  and decFlag<2:
        num =element.split("^")
        base = (float)(num[0])
        exp = (float)(num[1])
        element = base**exp
        postfix.append(element)
        return True
    elif expFlag == 0 and decFlag <2: 
        element = (float)(element)
        postfix.append(element)
        return True
    else:
        print("numerical error")
        return False


class point(object):
    def __init__(self,open_par,close_par):
        self.OP = open_par
        self.CP = close_par
    def getOP(self):
        return self.OP
    def getCP(self):
        return self.CP
    def __str__(self):
        return "( is " + str(self.OP) +"\n) is " + str(self.CP)
        
user_input = input("Evaluate: ")
string = "(" + user_input + ")"
print(string)
expression = (list)(string)
print(expression)
open_pars = []
close_pars = []
par_pairs = []
iterator = 0
flag = True
while iterator < len(expression):
    if expression[iterator] == "(":
        open_pars.append(iterator)
    elif expression[iterator] == ")":
        close_pars.append(iterator)
    iterator+=1
if len(close_pars) == len(open_pars):
    while len(close_pars) > 0:
        par_pairs.append(point(open_pars.pop(), close_pars.pop(0)))
else:
    print("parenthesis error")
    flag = False
#at this point all the parentheses should be paired up from most inside to least
iterator = 0
while iterator < len(par_pairs) and flag:
    pair = par_pairs.pop(0)
    op = pair.getOP()
    cp = pair.getCP()
    expr = string[op+1:cp]
    ex_list = list(expr)
    number = evalExp(ex_list)
    iterator+=1

