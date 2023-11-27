#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:24:19 2023

@author: tallulah
"""
import random
import math
from calculator import *


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
        num = random.randint(0, 10000)
        decimal = random.randint(0, 1)
        if decimal:
            decimal = random.randint(0, 10000)
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
        operators = ["+", "-", "*", "/"]
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


num_loop = input("How many expressions would you like to compute? ")

for i in range(int(num_loop)):
    equation_to_eval = expression(10)
    calculate(equation_to_eval.get_expr())
    try:
        print("=" + str(eval(equation_to_eval.get_expr())))
    except Exception as e:
        print(e)
        print("Error")
'''
equation_to_eval = expression(25)
expr = equation_to_eval.get_expr()
print(expr)
print("=" + str(eval(expr)))
'''
