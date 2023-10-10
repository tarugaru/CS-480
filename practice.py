# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:10:58 2023

@author: tallu
"""
def evalExp(expr):
    postfix = []
    operators = []
    print(expr)
    ex_list = list(expr)
    validExp = True
    '''
    if ex_list[0]=="-":
        getNumVal(ex_list.pop(0))
    while len(ex_list)>0 and validExp:
        element = expression.pop(0)
        if element.isdigit() or element == ".":
            validExp = getNumVal(element)
        elif element == "c":
            validExp = evalCos(element)
        elif element == "s":
            evalSin(element)
        elif element == "l":
            evalLog(element)
        elif element == "n":
            evalLn(element)
        elif element == "+" or element =="*" or element=="-":
            print("made it")
            evalOp(element)
        '''
    print(postfix)
    print(operators)
        
    #here is where we evaluate what is going on inside this particular parenthesis
    #lets create the shunting yard algo here, with the num queue and op stack
    return 0
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
#at this point all the parentheses should be paired up from most inside to least
iterator = 0
while iterator < len(par_pairs):
    pair = par_pairs.pop(0)
    op = pair.getOP()
    cp = pair.getCP()
    expr = string[op+1:cp]
    print(expr)
    number = evalExp(expr)
    iterator+=1

