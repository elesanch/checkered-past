#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:34:48 2022

@author: elenasanchez
"""
import pygame
from constants import WHITE, RED, SQUARE_SIZE, GREY

class Piece: 
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color): 
        self.row = row
        self.col = col 
        self.color = color 
        self.king = False 
        # if self.color == RED:
        #     self.direction = -1 # going up
        # else: 
        #     self.direction = 1 # moving down    
        
        self.x = 0 
        self.y = 0 
        
        self.calc_pos()
    def calc_pos(self): 
        # this is to ge the center of square and be able to draw the piece from the center 
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king (self): 
        self.king = True
    
    def draw(self, win): 
        radius = SQUARE_SIZE //2 - self.PADDING
        
        # first draw "outline" as big circle and then do the smaller circle on top of it 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win,self.color, (self.x, self.y),radius)
    
    # def __repr__(self):
    #     return str(self.color)