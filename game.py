#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:41:48 2022

@author: elenasanchez & trecr
"""
import pygame
from pygame import mixer
from constants import RED, WHITE, BLUE, SQUARE_SIZE
from board import Board

mixer.init()
select_fx = pygame.mixer.Sound("sounds/select_piece.wav")
select_fx.set_volume(0.75)
place_fx = pygame.mixer.Sound("sounds/place_piece.wav")
place_fx.set_volume(0.75)
wrong_select_fx = pygame.mixer.Sound("sounds/wrong_click.wav")
wrong_select_fx.set_volume(0.75)
jumped_fx = pygame.mixer.Sound("sounds/jumped.wav")
jumped_fx.set_volume(0.75)

class Game:
    '''
    This class encompasses all of the game driven attributes. This includes
    rules such as changing turns and slecting only on piece per turn. This
    class also includes the removal of pieces after they have been jumped
    and the calling of the appropiate sounds for all actions.
    '''
    def __init__(self, win, mode, color1, color2):
        self.selected_piece = None
        self.board = Board(color1, color2)
        self.turn = RED
        self.valid_moves = {}
        self.win = win
        self.mode = mode

    def update(self):
        '''
        This fucntion updates the board every single move or time that
        something has been drawn from the Board class.

        Returns
        -------
        None.

        '''
        self.board.draw(self.win)
        self.draw_pos_moves(self.valid_moves)
        pygame.display.update()

    def reset(self, color1, color2):
        '''
        This allows the board to be reset it to initial values as needed.

        Returns
        -------
        None.

        '''
        self.selected_piece = None
        self.board = Board(color1, color2)
        self.turn = RED
        self.valid_moves = {}

    def change_turn(self):
        '''
        This function keeps up with the rule of alternating turns.

        Returns
        -------
        None.

        '''
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def select(self, row, col):
        '''
        This function determines if chosen piece can move or not.

        Parameters
        ----------
        row : Int
            Row location of chosen piece.
        col : Int
            Column location of chose piece.

        Returns
        -------
        Bool
            True or False regarding if chosen piece can move or not.
        '''
        if self.selected_piece:
            nxt_move = self.move(row, col)
            if not nxt_move: # if selected move is not valid, reselect piece
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get_piece(row,col)

        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_pos_moves(piece)
            select_fx.play()
            return True

        return False

    def move(self, row, col):
        '''
        This fucntion shows if chosen location presents a valid move or not.

        Parameters
        ----------
        row : Int
            Row location of chosen move.
        col : Int
            Column location of chose move.

        Returns
        -------
        bool
            Returninf if chosen move is valid or not.

        '''
        place = self.board.get_piece(row, col)

        # This series of if statements create our criteria to move
        # 1. There is a selected piece
        # 2. Place is 0 (empty)
        # 3. Place to move is in valid moves

        if self.selected_piece and place == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                jumped_fx.play()
            place_fx.play()
            self.change_turn() # making the other player turn

        else:
            return False

        return True

    def draw_pos_moves(self, moves):
        '''
        This fucntion draws a circle in all possible moves for the instructional
        mode (1) of the game. See in UI. Users will see a blue circle in all
        the paces they are allowed to move the piece they have chosen.

        Parameters
        ----------
        moves : Dictionary
            Valid moves for given piece.

        Returns
        -------
        None.

        '''
        if self.mode == 1:
            for move in moves:
                row, col = move
                pygame.draw.circle(self.win, BLUE,
                                   (col *SQUARE_SIZE + SQUARE_SIZE // 2,
                                    row*SQUARE_SIZE + SQUARE_SIZE // 2), 15)
        else:
            pass

    def winner(self):
        '''
        This shows if a player has won by checking if they have any pieces left.

        Returns
        -------
        bool
            True or False if red player has won.

        '''
        if self.board.red_left == 0:
            return True
        elif self.board.white_left == 0:
            return False
        else:
            return None
