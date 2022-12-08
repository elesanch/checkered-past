#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:07:02 2022

@author: elenasanchez
"""
mport pygame 
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board 
from game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ('Checkers - Game')

def get_pos_mouse(position): 
    x, y = position
    row = y // SQUARE_SIZE # given current size
    col = x // SQUARE_SIZE
    
    return row, col

def main():
    run = True 
    clock = pygame.time.Clock()
    game = Game(WIN)
    board = Board()
    while run : 
        clock.tick(FPS)
        
        if board.winner() != None: 
            print(board.winner())
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                row, col = get_pos_mouse(pos)
                game.select(row,col)
                
        game.update()
    
    pygame.quit()

main()
