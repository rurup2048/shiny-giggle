#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:51:13 2024

@author: webbkids
"""

def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    mongoDaysTotal = ((currentYear - birthYear) * 390) + ((currentMonth - birthMonth) * 26) + (currentDay - birthDay)
    print(mongoDaysTotal)
    return  mongoDaysTotal / 390

print(compute_mongo_age(2879,8,11,2892,2,21))