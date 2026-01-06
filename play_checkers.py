#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 15:00:09 2025

@author: rupertjwebb
"""

from tkinter import *
from tkinter import filedialog 

class CheckersSquare(Canvas):
    '''displays a square in the checkers game'''

    def __init__(self, master, r, c):
        '''checkersSquare(master, r, c)
        creates a new blank checkers square at coordinate (r, c)'''
        # create and place the widget
        Canvas.__init__(self, master, width=40, height=40, bg='white', highlightbackground='black')
        self.grid(row=r, column=c)
        self.position = (r, c)
        self.bg = ''
        self.bgColors = ['green', 'light blue']
        self.tileColors = ['red', 'white']
        self.config(t=str(self.position))
        self.text = self.create_text(25, 25, text='', font=("Arial", 10, "bold"), fill='black')
        self.isPiece = False
        self.isKing = False
        self.isHighlighted = False
        self.tilePlayer = -1
        # set the attributes
        if c%2==0:
            if r%2==0:
                self.config(bg=self.bgColors[0])
                self.bg = self.bgColors[0]
            else:
                self.config(bg=self.bgColors[1])
                self.bg = self.bgColors[1]
        else:
            if r%2==1:
                self.config(bg=self.bgColors[0])
                self.bg = self.bgColors[0]
            else:
                self.config(bg=self.bgColors[1])
                self.bg = self.bgColors[1]  
        # bind button click to placing a piece
        self.bind('<Button-1>', self.get_click)
        
    def get_click(self, event):
        highlightedPiece = self.master.highlightedPiece
        if self.isPiece and (self.can_move() or self.can_jump()):
            if highlightedPiece == None or highlightedPiece == self:
                if self.is_turn():
                    self.toggle_highlight()
                 
        elif not self.isPiece and highlightedPiece != None:
            if highlightedPiece.can_move_to(self.position):
                highlightedPiece.toggle_highlight()
                highlightedPiece.move(self.position)
                
            if highlightedPiece.can_jump_to(self.position):
                highlightedPiece.toggle_highlight()
                highlightedPiece.jump(self.position)
    def __str__(self):
        output = ''
        output += 'a tile at '+str(self.position)
        output += ', and isPiece: '+str(self.isPiece)
        return output
    
    def get_position(self):
        '''checkersSquare.get_position() -> (int, int)
        returns (row, column) of square'''
        return self.position
    
    def set_tilePlayer(self, player):
        self.tilePlayer = player
    
    def get_bg_color(self):
        return self.bg
    
    def clear(self):
        ovalList = self.find_all()  # remove existing piece
        for oval in ovalList:
            self.delete(oval)
        self.isPiece = False
        self.isKing = False
    
    def make_color(self, color):
        '''checkersSquare.make_color(color)
        changes color of piece on square to specified color'''
        ovalList = self.find_all()  # remove existing piece
        for oval in ovalList:
            self.delete(oval)
        self.piece = self.create_oval(10, 10, 34, 34, fill=color)
        self.itemconfig(self.piece, outline=color) 
    
    def toggle_tile(self, player):
        self.isPiece = not self.isPiece
        self.tilePlayer = player
        if self.isPiece:
            if self.tilePlayer != -1:
                self.make_color(self.tileColors[player])
                self.tilePlayer = player
            
    def move_Locs(self):
        '''move_Locs() -> list'''
        board = self.master.board
        if not self.isPiece:
            return []
        moveDir = self.get_moveDir()
        row, col = self.position
        output = []
        if self.isKing:
            for pieceRow in range(-1,2,2):
                for pieceCol in range(-1,2,2):
                    try:
                        piece = board[row + pieceRow][col + pieceCol]
                        if not piece.isPiece:
                            targetRow, targetCol = piece.position
                            if abs(targetCol - col) == 1:
                                output.append(piece)
                    except:
                        continue
        else:
            for i in range(-1,2,2):
                try:
                    piece = board[row + moveDir][col + i]
                    if not piece.isPiece:
                        targetRow, targetCol = piece.position
                        if abs(targetCol - col) == 1:
                            output.append(piece)
                except:
                    continue
        return output
    
    def can_move(self):
        return len(self.move_Locs()) != 0
    
    def can_move_to(self,coords):
        canMove = False
        board = self.master.board
        row, col = coords
        targetPiece = board[row][col]
        for piece in self.move_Locs():
            if piece == targetPiece:
                canMove = True
        return canMove
    
    def toggle_king(self):
        self.isKing = not self.isKing
        print(self.isKing)
        if self.isKing:
            print('qwerty')
            self.create_text(25, 25, text='', font=("Arial", 10, "bold"), fill='black')
            self.update
            
    def get_surounding_tiles(self):
        board = self.master.board
        output = []
        for row in range(-1,2,2):
            for col in range(-1,2,2):
                piece = board[row][col]
                output.append(piece)
        return output
                
    
    def get_moveDir(self):
        moveDir = 0
        if self.tilePlayer == 0:
            moveDir = 1
        else:
            moveDir = -1
        return moveDir
    
    def toggle_highlight(self):
        self.isHighlighted = not self.isHighlighted
        highlight = self.master.highlightedPiece
        if self.isHighlighted:
            if highlight == None:
                self.config(highlightbackground='blue')
                self.master.highlightedPiece = self
        else:
            self.config(highlightbackground='black')
            if self == highlight:
                self.master.highlightedPiece = None
    
    def move(self, coords):
        board = self.master.board
        targetRow, targetCol = coords
        target = board[targetRow][targetCol]
        if targetRow in [0,7]:
            target.toggle_king()
        target.toggle_tile(self.tilePlayer)
        target.isKing = self.isKing
        target.isKing = False
        self.clear()
        self.master.pass_turn()
    
    def jump_Locs(self):
        board = self.master.board
        if not self.isPiece:
            return []
        moveDir = self.get_moveDir()
        row, col = self.position
        output = []
        if self.isKing:
            for pieceRow in range(-1,2,2):
                for pieceCol in range(-1,2,2):
                    try:
                        middlePiece = board[row + pieceRow][col + pieceCol] 
                        targetPiece = board[row + (pieceRow*2)][col + (pieceCol*2)]
                        if not targetPiece.isPiece and middlePiece.isPiece:
                            if middlePiece.tilePlayer != self.tilePlayer:
                                targetRow, targetCol = targetPiece.position
                                if abs(targetCol - col) == 2:
                                    # print(piece)
                                    output.append(targetPiece)
                    except:
                        continue
        else:            
            for i in range(-1,2,2):
                try:
                    middlePiece = board[row + moveDir][col + i] 
                    targetPiece = board[row + (moveDir*2)][col + (i*2)]
                    if not targetPiece.isPiece and middlePiece.isPiece:
                        if middlePiece.tilePlayer != self.tilePlayer:
                            targetRow, targetCol = targetPiece.position
                            if abs(targetCol - col) == 2:
                                # print(piece)
                                output.append(targetPiece)
                except:
                    continue
        return output
    
    def can_jump(self):
        return len(self.jump_Locs()) != 0
    
    def can_jump_to(self, coords):
        canMove = False
        board = self.master.board
        row, col = coords
        targetPiece = board[row][col]
        for piece in self.jump_Locs():
            if piece == targetPiece:
                canMove = True
        return canMove
        
    def jump(self, coords):
        board = self.master.board
        targetRow, targetCol = coords
        targetPiece = board[targetRow][targetCol]
        row, col = self.position
        midRow = (row + targetRow)//2 
        midCol = (col + targetCol)//2
        
        jumpPath = [self ,board[midRow][midCol] ,targetPiece]
        for move in range(2):
            jumpPath[move].move(jumpPath[move+1].position)
        if not self.can_jump():
            self.master.pass_turn()
        
    def is_turn(self):
        turn = self.master.currTurn
        return turn == self.tilePlayer
            

class CheckersGame(Frame):
    '''represents a game of checkers
    player 1: red: 0
    player 2: white: 1'''

    def __init__(self, master):
        '''checkersGame(master)
        creates a new checkers game'''
        # initialize the Frame
        self.tileColors = ['red', 'white']
        Frame.__init__(self, master, bg='white')
        self.grid()
        # set up game data
        # create board in starting position, player 0 going first
        self.turnLabel = Label(self, text='turn')
        self.turnLabel.grid(row=8, column=3)
        self.turnCount = 0
        self.currTurn = 0
        self.highlightedPiece = None
        self.board = []
        self.turnCount = 0
        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(CheckersSquare(self, row, col))
                if row <= 2 and self.board[row][col].bg == 'light blue':
                    self.board[row][col].toggle_tile(0)
                if row >= 5 and self.board[row][col].bg == 'light blue':
                    self.board[row][col].toggle_tile(1)
        
        self.turnTile = CheckersSquare(self, 8, 4)
        self.pass_turn()
        self.pass_turn()
        
    
    def pass_turn(self):
        self.turnCount += 1
        self.currTurn = self.turnCount % 2
        self.turnTile.make_color(self.tileColors[self.currTurn])
        winCon = [0,0]
        for row in self.board:
            for piece in row:
                winCon[piece.tilePlayer] += 1
        if winCon == [0,0]:
            messagebox.showinfo('checkers',"it's a tie!",parent=self)
        elif winCon[1] == 0:
            messagebox.showinfo('checkers','red wins!',parent=self)
        elif winCon[0] == 0:
            messagebox.showinfo('checkers','white wins!',parent=self)                

def play_checkers():
    '''play_checkers()
    starts a new game of checkers'''
    root = Tk()
    root.title('checkers')
    RG = CheckersGame(root)
    RG.mainloop()

play_checkers()