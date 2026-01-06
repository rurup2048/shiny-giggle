#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:15:49 2024

@author: webbkids
"""
def setup():
    '''setup() -> dict
    gets the players names 
    and puts them in a dict'''
    players = {}
    for player in ['X', 'O']:
        getPlayer = input('whats your name player ' + player + ': ')
        players[getPlayer] = player
    return players

def makeBoard():
    '''makeBoard() -> list
    creates a blank board'''
    board = []
    for i in range(42):
        board.append('*')
    return board

def printBoard(board):
    '''rintBoard(list) -> none
    prints a board'''
    for i in range(7):
        print(i,end=' ')
    print('\n-------------')
    num = 0
    for piece in board:
        print(piece, end=' ')
        num += 1
        if num == 7:
            num = 0
            print('\n')
        
    
def whoWins(board):
    '''whoWins(list) -> str
    returns who wins'''
    row = ''
    for i in range(0,36,7):
        for j in range(7):
            row += board[i + j] 
        if 'XXXX' in row:
            return 'X wins'
        elif 'OOOO' in row:
            return 'Y wins'
        row = ''
gameBoard = makeBoard()
# players = setup()
players = {'we': 'X', 'ds': 'O'}
printBoard(gameBoard)
winner = False
while True:
    for player in players:
        #print(len(gameBoard))
        printBoard(gameBoard)
        place = int(input(player +", you're " + players[player] + ". What column do you want to play in? "))
        places = []
        for thing in range(0,41,7):
            print(thing + place)
            places.append(thing + place)
        places.reverse()
        print(places)
        for place in places:
            if gameBoard[place] == '*':
                print('got throuth')
                gameBoard[places[place]] = players[player]
            elif place == places[-1]:
                print('blank')
                gameBoard[0] = players[player]
                    
    
    if not whoWins(gameBoard) == None:
        print(whoWins(gameBoard))
        winner = True
        break
  
    
# place = int(input(player +", you're " + players[player] + ". What column do you want to play in? "))
# for i in range(place +1, 42, 7):
#     if not i == 35 + place + 1:
#         print('in loop: ' + str(i) + ' looking at ' + str(i + 7) + ' which is ' + gameBoard[i + 7])
#         if gameBoard[i + 7] in ['X', 'O']:
#             print(-i)
#             gameBoard[i + 1] = players[player]
#             break
#     else:
#         gameBoard[i] = players[player]
#         print(gameBoard[i].index(players[player]))
# printBoard(gameBoard)
    