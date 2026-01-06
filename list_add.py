#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:20:09 2024

@author: webbkids
"""

def list_add(list1,list2):
    '''list_add(list1,list2) -> list
    returns the lists whose entries are sums of the
    corresponding entries from list1 and list2.'''
    endList = []
    for i in list1:
        endList.append(i + list2[i-1])
    return endList

# test cases
print(list_add([1,2,3],[5,8,11]))
print(list_add([1,2],[4,5,6]))  # lists of different sizes