#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01 02 03 04 05
16 17 18 19 06
15 24 25 20 07
14 23 22 21 08
13 12 11 10 09
--------------
1 2 3 4 5 6 7 8 9
==============
1 2 3
8 9 4
7 6 5
==============
[[0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0], 
 [0, 8, 7, 0, 6], 
 [0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0]]
"""
def getCount(b):
    output = 0
    for i in b:
        output += i.count(0)
    return output
#1 1 2 2 3 3 4 4 4
board = []
boardSize = int(input())+2
pos = [boardSize//2,boardSize//2]
#board.append([])
board.append(list(map(int,('0 '*(boardSize)).split())))
for i in range(1,boardSize-1):
    board.append([0])
    for j in range(boardSize-2):
        board[i].append(0)
    board[i].append(0)
board.append(list(map(int,('0 '*(boardSize)).split())))
dirNum = 0
dist = 1
amount = 0
# dirs = [[0,-1],[1,0],[0,1],[-1,0]]
dirs = [[-1,0],[0,1],[1,0],[0,-1]]
print(getCount(board))
while amount != ((boardSize-2)**2):
    for i in range(2):
        for j in range(dist):
            x, y = pos
            print(pos)
            board[x][y] = ((boardSize-2)**2)-(amount)
            print(board)
            amount += 1
            pos = [pos[1]+(dirs[dirNum%4][1]*dist),pos[0]+(dirs[dirNum%4][0]*dist)]
        dirNum += 1
    dist += 1