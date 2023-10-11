# -*- coding: utf-8 -*-
"""
# Tallulah Cook
# CS 480
# Calculator Application:
    # objective: implement a simple calculator that takes in user input (Strings)
# 10/2/23 -  10/11/23
# calculator.py

#commits can be found on github: https://github.com/tarugaru/CS-480
"""
import math

ex_list = []
postfix = []
operators = []

def evalExp(ex_list):
    #print(ex_list)
    validExp = True
    if ex_list[0] == "-":
        element = ex_list.pop(0)
        validExp = getNumVal(element)
    while len(ex_list)>0 and validExp:
        element = ex_list.pop(0)
        if element.isdigit() or element == ".":
            validExp = getNumVal(element)
        elif element == "+" or element == "-" or element == "*" or element == "/":
            validExp = opVal(element)
        else:
            validExp = eval_func(element)
    if validExp:
        #print(postfix)
        #print(operators)
        num = shunting_algo()
        #print("eval expr now")
        return num;
    else:
        #print(postfix)
        #print(operators)
        #print ("function terminated")
        return "x"
    #print(postfix)
    #print(operators)
    '''
    is_float func from:
        https://pythonhow.com/how/check-if-a-string-is-a-float/#:~:text=To%20check%20if%20a%20string%20is%20a%20number%20(float)%20in,casted%20to%20float%20or%20not.
    '''
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
def shunting_algo():
    #print("here")
    '''
    while len(operators)>0:
        postfix.append(operators.pop(0))
    '''
    #print(postfix)
    while len(operators)>0:
        num_2 = postfix.pop()
        num_1 = postfix.pop()
        num = evaluate(num_1,num_2,operators.pop())
        postfix.append(num)
    #print("done w algo")
    #print(stack)
    return postfix.pop()
def evaluate(n1,n2,element):
     if element == "+":
         return n1+n2
     elif element == "-":
         return n1-n2
     elif element == "*":
         return n1*n2
     elif element == "/":
         return n1/n2
def eval_func(element):
    #print("reached")
    if element == "c":
        element = ex_list.pop(0)
        flag = True
        if element.isdigit():
            flag = getNumVal(element)
        if flag:
            element = postfix.pop()
            element = math.cos(element)
            postfix.append(element)
        #print("cosine")
        return flag
    elif element == "s":
        element = ex_list.pop(0)
        flag = True
        if element.isdigit():
            flag = getNumVal(element)
        if flag:
            element = postfix.pop()
            element = math.sin(element)
            postfix.append(element)
        #print("sin")
        return flag
    if element == "t":
        element = ex_list.pop(0)
        flag = True
        if element.isdigit():
            flag = getNumVal(element)
        if flag:
            element = postfix.pop()
            element = math.tan(element)
            postfix.append(element)
        #print("cosine")
        return flag
    elif element == "l":
        element = ex_list.pop(0)
        flag = True
        if element.isdigit():
            flag = getNumVal(element)
        if flag:
            element = postfix.pop()
            element = math.log10(element)
            postfix.append(element)
        #print("log")
        return flag
    elif element == "n":
        element = ex_list.pop(0)
        flag = True
        if element.isdigit():
            flag = getNumVal(element)
        if flag:
            element = postfix.pop()
            element = math.log(element)
            postfix.append(element)
        #print("natural log")
        return flag
    else:
        #print("invalid character")
        return False
def opVal(element):
    flag = True
    if len(operators)>0:
        prevOp = operators[len(operators)-1]
        if (prevOp == "*" or prevOp == "/") and (element == "+" or element == "-"):
            postfix.append(prevOp)
            operators.pop()
            operators.append(element)
        else:
            operators.append(element)
    else:
        operators.append(element)
    if len(ex_list) > 0 and ex_list[0] == "-":
        flag = getNumVal(ex_list.pop(0))
    return flag
def getNumVal(element):    
    #parse through ex_list to get the number together
    char = None
    expFlag = 0
    decFlag = 0
    if len(ex_list)>0:
        char = ex_list[0]
        #print("char: " + char)
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
        elif char == "-" and element[-1]=="-":
            print("too many minus signs")
            return False
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
string = string.replace(" ","")
string = string.replace("{","(")
stirng = string.replace("}",")")
string = string.replace("sin", "s")
string = string.replace("cos","c")
string = string.replace("tan", "t")
string = string.replace("log", "l")
string = string.replace("ln", "n")

numOP = 0
numCP = 0
flag = True
for element in string:
    if element == "(":
        numOP+=1
    elif element == ")":
        numCP +=1
print(string)
iterator = 0
if numOP==numCP:
    flag = True
else:
    flag = False
    print("parenthesis error")

while "(" in string and flag:
    iterator = 0
    cp = 0
    for element in string:
        if element == "(":
            cp = iterator
        elif element == ")":
            eval_expression = string[cp+1:iterator]
            print(eval_expression)
            ex_list = list(eval_expression)
            number = evalExp(ex_list)
            string = string.replace(string[cp:iterator+1],str(number))
            print(string)
            break
        iterator +=1
if string == "x":
    print("try again")
elif flag:
    print("final answer: " + str(string))

