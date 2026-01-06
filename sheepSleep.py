#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 19:46:46 2025

@author: rupertjwebb
"""

def solve(n):
  if n == 0:
    return -1
  current_number = n
  digits_seen = set()
  while True:
    for digit in str(current_number):
      digits_seen.add(digit)
    if len(digits_seen) == 10:
      return current_number
    current_number += n
n = int(input())
# fis = list(map(int, input().strip()))
print(solve(n))