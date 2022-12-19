#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:36:16 2022

This file serves to hold all the constants needed for the game of checkers.
That includes, colors for boards, dimensions and  pictures.

@author: elenasanchez
"""
import pygame

WIDTH, HEIGHT = 800,800

ROWS, COLS = 8, 8 # standard board
SQUARE_SIZE = WIDTH // COLS

# Colors for board in rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0, 255)
GREY = (128, 128, 128)

# Crown picture for kings pieces
CROWN = pygame.transform.scale(pygame.image.load('crown.png'),(60,30))
