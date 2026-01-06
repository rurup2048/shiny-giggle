#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 18:14:23 2025

@author: rupertjwebb
"""
def find_num_min(xlst):
    smallest = None
    count = 0
    for elt in xlst:
        if not count or elt < smallest:
            smallest = elt
            count = 1
        elif elt == smallest:
            count += 1
    return (count, smallest)

import random
import statistics
# num_rounds = random.randint(1, 100)
def bessy1(n,num_rounds):
    for i in range(num_rounds):
        n_ave = statistics.mean(n)
        n.append(int(n_ave))
        smallest_n = find_num_min(n)
        n.remove(smallest_n[1])
    return n

def bessy2(n,num_rounds):
    s = sum(n)
    for i in range(num_rounds):
        n.append(int(s/len(n)))
        smallest_n = find_num_min(n)
        s = s - smallest_n[0]
        n.remove(smallest_n[1])
    return n

for i in range(10):
    for j in range(10):
        for k in range(10):
            b1 = bessy1([i,j,k],1000)
            b2 = bessy2([i,j,k],1000)
            
            # b1 = bessy1([i],1000)
            # b2 = bessy2([i],1000)
            
            if b1 == b2:
                print('passsed',end=' ')
            else:
                print('failed',end=' ')
            print([i,j,k])
            
            # print('b1:' + str(bessy1([i,j,k],1000)))
            # print('b2:' + str(bessy2([i,j,k],1000)))

        
        