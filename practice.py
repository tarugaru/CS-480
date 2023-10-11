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
        if element.isdigit() or element == ".":
            validExp = getNumVal(element)
        elif element == "+" or element == "-" or element == "*" or element == "/":
            validExp = opVal(element)
        else:
            eval_func(element)
    if validExp:
        print(postfix)
        print(operators)
        num = shunting_algo()
        print("eval expr now")
        return num;
    else:
        print(postfix)
        print(operators)
        print ("function terminated")
        return "x"
    print(postfix)
    print(operators)
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
    print("here")
    while len(operators)>0:
        postfix.append(operators.pop(0))
    print(postfix)
    stack = []
    while len(postfix)>0:
        print("postfix: ")
        print(postfix)
        element = postfix.pop(0)
        if is_float(element):
            stack.append(element)
            print("stack ")
            print(stack)
        else:
            num_1 = stack.pop(0)
            num_2 = stack.pop(0)
            num = evaluate(num_1, num_2, element)
            print(str(num))
            stack[:0] = [num]
    print("done w algo")
    print(stack)
    return stack.pop()
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
    print("reached")
    if element == "c":
        print("cosine")
    elif element == "s":
        print("sin")
    elif element == "l":
        print("log")
    elif element == "n":
        print("natural log")
    else:
        print("invalid character")
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
string = string.replace(" ","")
string = string.replace("sin", "s")
string = string.replace("cos","c")
string = string.replace("log", "l")
string = string.replace("ln", "n")
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
            ex_list = list(eval_expression)
            number = evalExp(ex_list)
            string = string.replace(string[cp:iterator+1],str(number))
            print(string)
            break
        iterator +=1
#expression = (list)(string)
#print(expression)

'''
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
    operators = None
    postfix = None
    pair = par_pairs.pop(0)
    op = pair.getOP()
    cp = pair.getCP()
    expr = string[op+1:cp]
    ex_list = list(expr)
    number = evalExp(ex_list)
    print(str(number))
    if is_float(number):
        #we need to add this number back into our original expression,
        #replacing the () we just evaluated. 
        print("hi")
    else:
        print("system terminated")
        flag = False
    iterator+=1
'''