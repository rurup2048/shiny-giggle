#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:10:36 2024

@author: webbkids
"""

def dict_reverse(inputDict):
    '''dict_reverse(inputDict) -> dict
    returns dict with keys/values of inputDict swapped'''
    # add your code here

testDict = {'adam':80,'betty':60,'charles':50}
reversedDict = dict_reverse(testDict)
print(reversedDict)
# should be {80:'adam',60:'betty',50:'charles'} in some order