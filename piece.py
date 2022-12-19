#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:34:48 2022

This file holds all information regarding the checkers pieces.

@author: elenasanchez & trecr
"""
import pygame
from constants import SQUARE_SIZE, GREY, CROWN

class Piece:
    '''
    This class encompasses all attributes of the checkers pieces. This includes
    their positioning within a square, color and if they are kings. This class
    also draws each piece onto the board and moves them to appropiate location
    within the square.
    '''
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
        '''
        This fucntion calculate piece positioning (center) within a square.

        Returns
        -------
        None.

        '''
        # This is to get the center of square and be able to draw the piece from the center
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king (self):
        '''
        This fucntion turns feature as True when the piece is made king.

        Returns
        -------
        None.

        '''
        self.king = True

    def draw(self, win):
        '''
        This function draws each piece at a particualr pixel location within
        pygame window.

        Parameters
        ----------
        win : Object
            Pygame window where Checkers game exists.

        Returns
        -------
        None.

        '''
        radius = SQUARE_SIZE // 2 - self.PADDING

        # first draw "outline" as big circle and then do the smaller circle on top of it
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win,self.color, (self.x, self.y),radius)

        # adding the crown to center of king pieces
        if self.king:
            win.blit(CROWN,(self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move (self, row, col):
        '''
        Calculates where the picece should be drawn given row and column.

        Parameters
        ----------
        row : Int
            Row where piece is intending to move.
        col : Int
            Column where piece is intending to move..

        Returns
        -------
        None.

        '''
        self.row = row
        self.col = col
        self.calc_pos()
