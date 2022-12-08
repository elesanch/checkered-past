#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:41:48 2022

@author: elenasanchez
"""
import pygame
from constants import RED, WHITE, BLUE, SQUARE_SIZE
from board import Board

class Game: 
    def __init__(self, win):
        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.win = win 
    
    def update(self): 
        self.board.draw(self.win)
        self.draw_pos_moves(self.valid_moves)
        pygame.display.update()
    
    def reset(self):
       self.selected_piece = None
       self.board = Board()
       self.turn = RED
       self.valid_moves = {}
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED: 
            self.turn = WHITE
        else: 
            self.turn = RED
            
    def select(self, row, col): #will determine if we can move or not 
        if self.selected_piece:
            nxt_move = self.move(row, col)
            if not nxt_move: # if selected move is not valid, reselect piece
                self.selected_piece = None
                self.select(row, col)
       
        piece = self.board.get_piece(row,col)
        
        if piece != 0 and piece.color == self.turn: 
            self.selected_piece = piece
            self.valid_moves = self.board.get_pos_moves(piece)
            return True 
            
        return False 
    
    def move(self, row, col):
        place = self.board.get_piece(row, col)
        # this creates our criteria to move, 1. There is a selected piece
        # 2. place is 0 (empty) and 3. the place to move is valid
        
        if self.selected_piece and place == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped: 
                self.board.remove(skipped)
            
            self.change_turn() # making the other player turn
        else: 
            return False 
        
        return True 
    
    def draw_pos_moves(self, moves):
        for move in moves: 
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col *SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 15)
    