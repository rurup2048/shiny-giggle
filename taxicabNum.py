#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:43:11 2024

@author: webbkids
"""
listsss = []
listss = []
lists = []
num = 100
for i in range(num):
    lists.append(i)
for j in range(num):
    listss.append(j ** 3)
for k in range(len(lists)):
    for l in lists:
        if l ** 3 == listss[k]:
            listsss.append(listss[l])
print(listsss)
            