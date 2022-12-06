#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:07:02 2022

@author: elenasanchez
"""
import pygame 
from constants import WIDTH, HEIGHT 
from board import Board 


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ('Checkers game')

def main():
    run = True 
    clock = pygame.time.Clock()
    board = Board()
    while run : 
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pass # for now but will be what to do when perssing
        
        board.draw(WIN)
        pygame.display.update()
    
    pygame.quit()

main()