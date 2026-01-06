#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:44:20 2025

@author: webbkids
"""
import math


def Catalan_Numbers(num):
    '''Catalan_Numbers(int num) -> num
    returns Catalan_Numbers to num
    Cn = (2n)! / ((n + 1)! n!). 
    '''
    catalan = math.factorial(2*num)
    number = (math.factorial(num + 1) * math.factorial(num))
    return int(catalan / number)
    
print('1: '+str(Catalan_Numbers(1)))# 1
print('2: '+str(Catalan_Numbers(2)))# 2
print('3: '+str(Catalan_Numbers(3)))# 5
print('4: '+str(Catalan_Numbers(4)))# 14
print('30: '+str(Catalan_Numbers(30)))# 3814986502092304
