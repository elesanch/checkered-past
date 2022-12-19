#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:01:32 2022

This file contains all information in relation to the Board in a checkers game.

@author: elenasanchez & trecr
"""
import pygame
from pygame import mixer
from constants import ROWS, COLS, RED, SQUARE_SIZE, WHITE
from piece import Piece

mixer.init()
king_fx = pygame.mixer.Sound("sounds/king.wav")
king_fx.set_volume(0.75)

class Board:
    '''
    This class contains all information pertaining to the board of the checkers
    game. This includes the moves certain pieces have made, drawing the board
    and removing pieces from the board itself. This class also keeps tracks of
    how many kings each player has.

    '''
    def __init__(self, color1, color2):
        self.board = [] # list of lists of pieces on the board (8 by 8)
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.color1 = color1
        self.color2 = color2
        self.create_board()

    def draw_squares(self, win, color1, color2):
        '''
        Funtion draws the squares needed to make the checkers board.

        Parameters
        ----------
        win : Object
            Window of pygame where game is happening.
        color1 : Str
            First color for board.
        color2 : Str
            Second color for board.

        Returns
        -------
        None.

        '''
        win.fill(color1)
        for row in range(ROWS):
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(win, color2, (col*SQUARE_SIZE, row*SQUARE_SIZE,
                                SQUARE_SIZE, SQUARE_SIZE)) # rectangle draw func
    def create_board(self):
        '''
        Creates board for checkers game.

        Returns
        -------
        Object
            Checkers board window on pygame.

        '''
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
        '''
        Draws piece on a speific location on the board.

        Parameters
        ----------
        win : Object
            Pygame window with board.

        Returns
        -------
        None.

        '''
        self.draw_squares(win, self.color1, self.color2)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        '''
        To be called when a piece needs to move. This deals with changing
        the index of an existing piece as well making a piece king when it
        reaches the end.

        Parameters
        ----------
        piece : Class
            Piece for checkers game.
        row : Int
            Row location for piece movement.
        col : Int
            Column location for piece movement.

        Returns
        -------
        None.

        '''
        # This moves the value from where the piece is to where the piece wants to be
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
        '''
        Helper function to find location of given piece.

        Parameters
        ----------
        row : Int
            Row location of piece.
        col : Int
            Column location of piece.

        Returns
        -------
        List
            Location of given piece as row, col.

        '''
        return self.board[row][col]

    def get_pos_moves (self, piece):
        '''
        Obtaining all possible moves for a chosen piece.

        Parameters
        ----------
        piece : TYPE
            DESCRIPTION.

        Returns
        -------
        moves : Dictionary
            With all the possible moves chosen piece has.

        '''
        moves = {} # valid move key = position of the pieces chosen piece has jumped
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
        '''
        This is the main function of the algorithim that decides allows
        the game to know what option the chosen piece has on the left. If
        the space diagonal on the left is empty,, it can move there. If is not
        empty, it checks to see if the piece can be jumped. If so, it checks
        the next possibility to see if a double/triple jump is possible.

        Parameters
        ----------
        start : Int
            Space we are currently on.
        stop : Int
            Last space to check.
        step : Int
            Will be positive or negative depending if we are going up or down.
        color : Str
            Color of piece to see if we can jump a piece or not.
        left : Int
            Keeps track of direction moved.
        skipped : TYPE, optional
            Keeping track if something is jumped. The default is [].

        Returns
        -------
        moves : Dictionary
            All moves the piece has made on the left.

        '''
        moves = {}
        last = []
        for ind in range(start, stop, step):
            if left < 0: # looking outside the board
                break

            current = self.board[ind][left]
            if current == 0: # means empty square
                if skipped and not last: # if next square is blank then
                    break
                elif skipped:
                    moves[(ind,left)]= last + skipped
                else: # if is empty and last move existed
                    moves[(ind,left)] = last

                if last: # this runs if we skipped over something previously
                    if step == -1:
                        row = max(ind - 3, 0)

                    else:
                        row = min(ind + 3, ROWS)

                    moves.update(self.look_left(ind + step, row, step, color,
                                                left-1 , skipped = last))
                    moves.update(self.look_right(ind + step, row, step, color, left+1 ,
                                                 skipped = last))
                break

            elif current.color == color: # cannot move to our same color piece
                break
            else: # if we can jump will iterate through the code again
                last = [current]


            left -= 1
        return moves

    def look_right(self, start, stop, step, color, right, skipped = []):
        '''
        This is the main function of the algorithim that decides allows
        the game to know what option the chosen piece has on the right. If
        the space diagonal on the left is empty,, it can move there. If is not
        empty, it checks to see if the piece can be jumped. If so, it checks
        the next possibility to see if a double/triple jump is possible.

        Parameters
        ----------
        start : Int
            Space we are currently on.
        stop : Int
            Last space to check.
        step : Int
            Will be positive or negative depending if we are going up or down.
        color : Str
            Color of piece to see if we can jump a piece or not.
        right : Int
            Keeps track of direction moved.
        skipped : TYPE, optional
            Keeping track if something is jumped. The default is [].

        Returns
        -------
        moves : Dictionary
            All moves the piece has made on the right.
        '''

        moves = {}
        last = []
        for ind in range(start, stop, step):
            if right >= COLS: # looking outside the board
                break

            current = self.board[ind][right]

            if current == 0: # means empty square
                if skipped and not last: # if next square is blank then
                    break
                elif skipped:
                    moves[(ind,right)]= last + skipped
                else: # if is empty and last move existed
                    moves[(ind, right)] = last

                if last: # this runs if we skipped over something previously
                    if step == -1:
                        row = max(ind - 3, 0)

                    else:
                        row = min(ind + 3, ROWS)

                    moves.update(self.look_left(ind + step, row, step, color,
                                                right-1 , skipped = last))
                    moves.update(self.look_right(ind + step, row, step, color,
                                                 right+1 , skipped = last))
                break

            elif current.color == color: # cannot move to our same color piece
                break
            else: # if we can jump will iterate through the code again
                last = [current]

            right += 1
        return moves

    def remove(self, pieces):
        '''
        Takes pieces that have been eaten form the board and frees the space.

        Parameters
        ----------
        pieces : Class
            Information on the checkers piece.

        Returns
        -------
        None.

        '''
        for piece in pieces:
            self.board[piece.row][piece.col]= 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
