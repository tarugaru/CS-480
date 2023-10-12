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
        num = shunting_algo()
        return num;
    else:
        return "x"
    
def shunting_algo():
    while len(operators)>0:
        element = operators.pop(0)
        postfix.append(element)
    stack = []
    while len(postfix)>0:
        if is_float(postfix[0]):
            stack.append(postfix.pop(0))
        else:
            n1 = stack.pop(0)
            n2 = stack.pop(0)
            result = evaluate(n1,n2,postfix.pop(0))
            stack.insert(0,result)
    return stack.pop()

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
    
def evaluate(n1,n2,element):
     if element == "+":
         return n1+n2
     elif element == "-":
         return n1-n2
     elif element == "*":
         return n1*n2
     elif element == "/":
         if n2==0:
             print("ERROR: DIVIDING BY 0")
             return "x"
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
        try:
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
        except Exception as e:
            print("Invalid log")
            return False
    elif element == "n":
        try:
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
        except Exception as e:
            print("Invalid natural log")
            return False
    else:
        print("ERROR: INVALID CHARACTER")
        return False
def opVal(element):
    flag = True
    opPrec = True
    while len(operators)>0 and opPrec:
        prevOp = operators[len(operators)-1]
        if (prevOp == "*" or prevOp == "/") and (element == "+" or element == "-"):
            postfix.append(prevOp)
            operators.pop()
        else:
            opPrec = False
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
            print("ERROR:MINUS SIGNS \n")
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
        print("ERROR: NUMERICAL \n")
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

print("Welcome to the python calculator app. Please follow the instructions in the READ" +
      "ME!\n***Remember: If you want to exit the program, input 'x' when it prompts you" +
      "for an expression to evaluate!\n\n")
user_flag = True
while(user_flag):
    user_input = input("Evaluate: ")
    user_input = user_input.lower()
    if(user_input == "x"):
        print("Thank you for using the python calculator app! \n**user terminated**")
        break
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
    #print(string)
    iterator = 0
    if numOP==numCP:
        flag = True
    else:
        flag = False
        print("ERROR: PARENTHESIS\nTry Again")
    
    while "(" in string and flag:
        iterator = 0
        cp = 0
        for element in string:
            if element == "(":
                cp = iterator
            elif element == ")":
                try:
                    eval_expression = string[cp+1:iterator]
                    #print(eval_expression)
                    ex_list = list(eval_expression)
                    number = evalExp(ex_list)
                    string = string.replace(string[cp:iterator+1],str(number))
                    #print(string)
                    break
                except Exception as e:
                    print("ERROR")
                    string = "x"
                    break
            iterator +=1
    if string == "x":
        print("Try Again\n")
    elif flag:
        print("Answer: " + str(string) +"\n")

