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
    for i in range(7): # creates the header
        print(i,end=' ')
    print('\n-------------')
    num = 0
    for piece in board: # creates the rest of the board
        print(piece, end=' ')
        num += 1
        if num == 7:
            num = 0
            print('')
        
            
def whoWins(board, player):
    '''whoWins(list, str) -> str
    returns the winner'''
    wins = [[0,1,2,3], [7,8,9,10], [14,15,16,17], [21,22,23,24], # all the ways to win horizontaly
            [0,7,14,21],[1,8,15,22], [2,9,16,23], [3,10,17,24], # all the ways to win verticaly
            [0,8,16,24],[3,9,15,21]] # all the ways to win diagonaly
    for col in range(3):
        for row in range(4):
            for win in wins:
                winner = True
                for place in win:
                    pos = place+row+(col*7)
                    if not board[pos] == players[player]:
                        winner = False
                        break
                if winner:
                    return player +' playing ' + players[player] + ' wins!'
                
def placePiece(piece, board):
    '''placePiece(piece, board) -> none
    plays a turn of connect4'''
    while True:
        place = ''
        while not place.isdigit():
            place = input(player +", you're " + players[player] + ". What column do you want to play in? ")
        if int(place) < 7:
            break
    place = int(place)
    collum = []
    for thing in range(0,41,7): # puts a collum of board in a list
        collum.append(thing + place)
    collum.reverse()
    for place in collum:
        if board[place] == '*': # 
            board[place] = players[player]
            break


board = makeBoard()
players = setup()
winner = False
printBoard(board)
while not winner:
    for player in players: # players take turns
        placePiece(players[player], board)
        printBoard(board) # prints the board
        if not whoWins(board, player) == None:
            print(whoWins(board, player))
            winner = True
            break
print('GAME OVER')        
        