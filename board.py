#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:01:32 2022

@author: elenasanchez
"""
import pygame 
from constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from piece import Piece
from pygame import mixer

mixer.init()
king_fx = pygame.mixer.Sound("sounds/king.wav")
king_fx.set_volume(0.75)

class Board: 
    def __init__(self, color1, color2): 
        self.board = [] # list of lists of pieces on the board (8 by 8)
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.color1 = color1
        self.color2 = color2
        self.create_board()
        
    def draw_squares(self, win, color1, color2):
        win.fill(color1)
        for row in range(ROWS): 
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(win, color2, (col*SQUARE_SIZE, row*SQUARE_SIZE, 
                                            SQUARE_SIZE, SQUARE_SIZE) ) # rectangle draw func 
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        return self.board
    
    def draw(self, win):
        self.draw_squares(win, self.color1, self.color2)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    def move(self, piece, row, col):
        
        # This moves the value from where the piece is to where the piece wanst to be
        # by reversing the index
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)
        
        # This makes kings if the piece touches the first or last row AFTER a move
        if row == ROWS - 1 or row == 0: 
            piece.make_king()
            king_fx.play()
            if piece.color == WHITE: 
                self.white_kings += 1 
            elif piece.color == RED: 
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def get_pos_moves (self, piece):
        moves = {} # valid move key = pos of pieces it jumped
        left = piece.col - 1 
        right = piece.col + 1 
        row = piece.row
        
        if piece.color == RED or piece.king: 
            moves.update(self.look_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.look_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        
        if piece.color == WHITE or piece.king: 
            moves.update(self.look_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.look_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        
        return moves
    
    def look_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = [] 
        for m in range(start, stop, step):
            if left < 0: # looking outside the board
                break 
            
            current = self.board[m][left]
            if current == 0: # means empty square
                if skipped and not last: # f next square is blank then
                    break
                elif skipped:
                    moves[(m,left)]= last + skipped
                else: # if is empty and last move existed 
                    moves[(m,left)] = last
                
                if last: # this runs if we skipped over something previously 
                    if step == -1: 
                        row = max(m - 3, 0)
                    
                    else: 
                        row = min(m + 3, ROWS)
                    
                    moves.update(self.look_left(m + step, row, step, color, left-1 , skipped = last))
                    moves.update(self.look_right(m + step, row, step, color, left+1 , skipped = last))
                break 
                
            elif current.color == color: #cannot move to our same color piece
                break
            else: # is we can jump will iterate through the code again
                last = [current]
                
            
            left -= 1
        return moves
            
    def look_right(self, start, stop, step, color, right, skipped = []): 
        moves = {}
        last = [] 
        for m in range(start, stop, step):
            if right >= COLS: # looking outside the board
                break 
            
            current = self.board[m][right]
                                           
            if current == 0: # means empty square
                if skipped and not last: # f next square is blank then
                    break
                elif skipped:
                    moves[(m,right)]= last + skipped
                else: # if is empty and last move existed 
                    moves[(m, right)] = last
                
                if last: # this runs if we skipped over something previously 
                    if step == -1: 
                        row = max(m - 3, 0)
                    
                    else: 
                        row = min(m + 3, ROWS)
                    
                    moves.update(self.look_left(m + step, row, step, color, right-1 , skipped = last))
                    moves.update(self.look_right(m + step, row, step, color, right+1 , skipped = last))
                break 
                
            elif current.color == color: #cannot move to our same color piece
                break
            else: # is we can jump will iterate through the code again
                last = [current]
                
            right += 1
        return moves

    def remove(self, pieces): 
       for piece in pieces: 
           self.board[piece.row][piece.col]= 0
           if piece != 0: 
               if piece.color == RED: 
                   self.red_left -= 1
               else: 
                   self.white_left -= 1
