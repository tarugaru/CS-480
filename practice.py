# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:10:58 2023

@author: tallu
"""
def evalExp(op,cp):
    print(str(op) + " " + str(cp))
    #here is where we evaluate what is going on inside this particular parenthesis
    #lets create the shunting yard algo here, with the num queue and op stack
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
expression = (list)("(" + user_input + ")")
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
    evalExp(op,cp)
