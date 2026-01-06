#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 18:20:47 2025

@author: rupertjwebb
"""

n = int(input())
fis = list(map(int, input().split()))
fis.sort()
i = 0
while i < n and fis[i] <= i:
    i += 1
print(i)
# def solve(n, fis):
#   num_standing = 0
#   is_standing = [False] * n
#   changed = False
#   while num_standing < n:
#     for i in range(n):
#       if (not is_standing[i]) and (fis[i] <= num_standing):
#         is_standing[i] = True
#         num_standing += 1
#         changed = True
#       if not changed:
#         break
#   return num_standing
# n = input()
# fis = list(map(int, input().strip()))
# print(solve(n, fis))

# def solve(n, fis):
#   num_standing = 0
#   is_standing = [False] * n
#   changed = False
#   while num_standing < n:
#     for i in range(n):
#       if (not is_standing[i]) and (fis[i] <= num_standing):
#         is_standing[i] = True
#         num_standing += 1
#         changed = True
#       if not changed:
#         break
#   return num_standing
# n = int(input())
# fis = list(input().strip().split())
# print(solve(n, fis))