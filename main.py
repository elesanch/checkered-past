#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:07:02 2022

@author: elenasanchez
"""
import pygame
import sys 
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board 
from game import Game
from button import Button

FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def get_pos_mouse(position): 
    x, y = position
    row = y // SQUARE_SIZE # given current size
    col = x // SQUARE_SIZE
    
    return row, col

def main_menu():
    pygame.display.set_caption("Main Menu")
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (400, 150))
    run = True 
    clock = pygame.time.Clock()
    WIN.fill("black")
    
    while run: 
        clock.tick(FPS)
        board = Board()
        menu_mouse_pos = pygame.mouse.get_pos()
        play_button = Button(button_face, pos=(400, 150), text_input = "PLAY", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        mode_button = Button(button_face, pos=(400, 300), text_input = "GAME MODE", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        options_button = Button(button_face, pos=(400, 450), text_input = "OPTIONS", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        exit_button = Button(button_face, pos=(400, 600), text_input = "EXIT", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        
        for selection in [play_button, mode_button, options_button, exit_button]:
            selection.color_change(menu_mouse_pos)
            selection.update(WIN)
            
        if board.winner() != None: 
            print(board.winner())
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.user_input(menu_mouse_pos):
                    play(mode = 0)
                if mode_button.user_input(menu_mouse_pos):
                    game_mode()
                if options_button.user_input(menu_mouse_pos):
                    options()
                if exit_button.user_input(menu_mouse_pos):
                    run = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
def play(mode):
    pygame.display.set_caption ('Normal Mode - Press Space Bar for Main Menu')
    run = True 
    clock = pygame.time.Clock()
    game = Game(WIN, mode)
    board = Board()
    
    while run: 
        clock.tick(FPS)
        WIN.fill("black")
        
        if board.winner() != None: 
            print(board.winner())
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                row, col = get_pos_mouse(pos)
                game.select(row,col)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()
        
        game.update()
    
    pygame.quit()

def game_mode():
    pygame.display.set_caption('Game Mode - Press Space Bar for Main Menu')
    run = True 
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))  
    
    while run: 
        clock.tick(FPS)
        WIN.fill("black")
        mode_mouse_pos = pygame.mouse.get_pos()
        instr_button = Button(button_face, pos=(400, 150), text_input = "INSTRUCTION MODE", font = pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        norm_button = Button(button_face, pos=(400, 300), text_input = "NORMAL MODE", font = pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        timed_button = Button(button_face, pos=(400, 450), text_input = "TIMED MODE", font = pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
           
        for selection in [instr_button, norm_button, timed_button]:
            selection.color_change(mode_mouse_pos)
            selection.update(WIN)
        
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instr_button.user_input(mode_mouse_pos):
                    play(mode = 1)
                if norm_button.user_input(mode_mouse_pos):
                    play(mode = 0)
                if timed_button.user_input(mode_mouse_pos):
                    play(mode = 0)
                    
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()

def options():
    pygame.display.set_caption('Settings - Press Space Bar for Main Menu')
    run = True 
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))  
    
    while run: 
        clock.tick(FPS)
        WIN.fill("black")
        opt_mouse_pos = pygame.mouse.get_pos()
        music_button = Button(button_face, pos=(400, 300), text_input = "MUSIC VOLUME", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
        board_button = Button(button_face, pos=(400, 500), text_input = "BOARD COLOR", font=pygame.font.SysFont("couriernew", 50), base_color="black", hovering_color="red")
           
        for selection in [music_button, board_button]:
            selection.color_change(opt_mouse_pos)
            selection.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()
            
        pygame.display.update()
 
##############################################################################
main_menu()
