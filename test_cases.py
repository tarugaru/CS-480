#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:24:19 2023

@author: tallulah
"""
import random
import math
from calculator import calculate

class typo_expression:
    expr = ""
    typo_flag = False
    def __init__(self, expr):
        self.expr = expr.get_expr()
        self.typo()
        
    def typo(self):
        #print(self.expr)
        i = random.randint(1,3)
        if i == 1:
            self.add_char()
        elif i==2:
            self.remove_char()
        elif self.typo_flag == True:
            #print(self.expr)
            return            
        #print(self.expr)
    
    def add_char(self):
        i = self.char()
        l = random.randint(0,len(self.expr)-1)
        expr = self.expr 
        expr = expr[:l]+str(i)+expr[l:]
        self.expr = expr
        self.typo_flag = True
        self.typo()
        #self.expr.insert(len(self.expr-1), i)
        
    def remove_char(self):
        i = random.randint(0,len(self.expr)-1)
        expr = self.expr
        expr = expr[:i] + expr[i+1:]
        self.expr = expr
        self.typo_flag = True
        self.typo()
        
    def get_expr(self):
        return self.expr
     
    def __str__(self):
        string = self.expr
        string = string.replace("math.sin", "sin")
        string = string.replace("math.cos","cos")
        string = string.replace("math.tan", "tan")
        string = string.replace("math.log10", "log")
        string = string.replace("math.log", "ln")
        return str(string)
    
    def char(self):
        chars = [random.randint(0,9), 'x', '(',')']
        return random.choice(chars)
class expression:
    expr = ""
    open_par = 0

    def __init__(self, length):
        self.length = length
        self.start_expr()

    def get_expr(self):
        return self.expr

    def start_expr(self):
        # an expression can start with a number, an open parenthesis, or a function call
        i = random.randint(1, 3)
        if i == 1:
            self.add_num()
        elif i == 2:
            self.add_open_par()
        else:
            self.add_func()
        # print(i)
        '''
        functions = [self.add_num(), self.add_open_par(), self.add_func()]
        rand_func = random.choice(functions)
        print(str(rand_func))
        rand_func()
        #print(str(rand_func))
        '''

    def add_num(self):
        num = random.randint(0, 100)
        decimal = random.randint(0, 1)
        if decimal:
            decimal = random.randint(0, 100)
            num = str(num) + "." + str(decimal)
        neg = random.randint(0, 1)
        if neg:
            self.expr += "-"
        self.expr = self.expr + str(num)
        # print(self.expr)
        # ADD THE GO TO ADD_OP OR ADD_CLOSED_PAR IF OPEN_PAR>0 LATER
        if (self.open_par > 0):
            i = random.randint(0, 1)
            if i:
                self.add_closed_par()
            else:
                self.add_op()
        else:
            self.add_op()

    def add_open_par(self):
        self.expr = self.expr + "("
        self.open_par += 1
        # print(self.expr)
        self.start_expr()

    def add_func(self):
        functions = ["math.cos(", "math.tan(", "math.sin(",
                     "math.log10(", "math.log("]
        rand_func = random.choice(functions)
        self.expr += rand_func
        self.open_par += 1
        # print(self.expr)
        self.start_expr()

    def add_op(self):
        operators = ["+", "-", "*", "/","^"]
        rand_op = random.choice(operators)
        self.expr += rand_op
        # print(self.expr)
        self.start_expr()

    def add_closed_par(self):
        if len(self.expr) > self.length:
            # print("entered finished")
            self.finish_expr()
        else:
            # print("entered closed")
            self.expr += ")"
            self.open_par -= 1
            # print(self.expr)
            self.add_op()

    def finish_expr(self):
        while self.open_par > 0:
            self.expr += ")"
            self.open_par -= 1
            # print(self.expr)
    def __str__(self):
        string = self.expr
        string = string.replace("math.sin", "sin")
        string = string.replace("math.cos","cos")
        string = string.replace("math.tan", "tan")
        string = string.replace("math.log10", "log")
        string = string.replace("math.log", "ln")
        return str(string)
        
def compare(equation_to_eval_str, num_correct):
    calculator_ans = None
    try:
        calculator_ans = calculate(equation_to_eval_str)
    except Exception as e:
        calculator_ans = "e"
    eval_ans = None
    try:
        eval_ans = eval(equation_to_eval_str)
    except Exception as e:
        eval_ans = "e"
    if eval_ans==calculator_ans:
        num_correct += 1
        print("PASSED\n")
    else: print("FAILED\n")
    return num_correct
        
expr = expression(25)
typo = typo_expression(expr)
num_loop = input("How many expressions would you like to compute? ")
num_loop_correct = int(num_loop)
if num_loop_correct%2 != 0:
    num_loop_correct -= 1
num_loop_correct = num_loop_correct/2
num_loop_incorrect = int(num_loop) - num_loop_correct
'''
print("will eval " + str(num_loop_correct) +" correct expressions")
print("will eval " + str(num_loop_incorrect) +" incorrect expressions")
'''
num_correct = 0
print("\n///////////////////")
print("CORRECT TEST CASES")
print("///////////////////\n")
for i in range(int(num_loop_correct)):
    equation_to_eval = expression(25)
    equation_to_eval_str = equation_to_eval.get_expr()
    print("Test Case #" + str(i+1) + ": ")
    print(equation_to_eval)
    num_correct = compare(equation_to_eval_str,num_correct)
print("\n///////////////////")
print("INCORRECT TEST CASES")
print("///////////////////\n")
for i in range(int(num_loop_incorrect)):
    expr = expression(25)
    equation_to_eval = typo_expression(expr)
    equation_to_eval_str = equation_to_eval.get_expr()
    print("Test Case #" + str(int(i+num_loop_correct+1)) + ": ")
    print(equation_to_eval)
    num_correct = compare(equation_to_eval_str, num_correct)
success_rate = (num_correct / int(num_loop)) * 100
print("\nTEST CASES DONE:")
print(str(num_correct) + " PASSED")
print(str(success_rate) + "% success rate")
'''
equation_to_eval = expression(25)
expr = equation_to_eval.get_expr()
print(expr)
print("=" + str(eval(expr)))
'''
