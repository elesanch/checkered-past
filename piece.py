#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:34:48 2022

@author: elenasanchez
"""
import pygame
from constants import SQUARE_SIZE, GREY, CROWN

class Piece: 
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color): 
        self.row = row
        self.col = col 
        self.color = color 
        self.king = False  
        self.x = 0 
        self.y = 0 
        self.calc_pos()

    def calc_pos(self): 
        # this is to get the center of square and be able to draw the piece from the center 
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king (self): 
        self.king = True
    
    def draw(self, win): 
        radius = SQUARE_SIZE // 2 - self.PADDING
        
        # first draw "outline" as big circle and then do the smaller circle on top of it 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win,self.color, (self.x, self.y),radius)
        
        # adding the crown to center of king pieces
        if self.king: 
            win.blit(CROWN,(self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
            
    def move (self, row, col):
        self.row = row 
        self.col = col
        self.calc_pos()
        
