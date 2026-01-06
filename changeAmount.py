#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:44:08 2025

@author: webbkids
"""
totals = []
coins = [25,10,1]
for changeAmount in range(101):
    change = changeAmount
    for coin in coins:
        numCoins = 0
        while change - coin >= 0:
            change -= coin
            numCoins += coin
    totals.append(numCoins)
        
            
            
    
    