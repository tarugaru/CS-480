#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:24:19 2023

@author: tallulah
"""
import random

class expression:
    def __init__(self, length):
        self.length = length
        self.start_expr()
    
    def start_expr(self):
        #an expression can start with a number, an open parenthesis, or a function call
        i = random.randint(1,3)
        match i:
            case 1:
                self.addNum()
            case 2:
                self.add_open_par()
            case 3:
                self.add_func()
                
                
        print(i)
    
expression(5)