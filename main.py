#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:07:02 2022

This is the main file for the checkers game. This fule contains all information
on the user interface (UI) design of this game. The file encompasses, the
differentscreens, modes of play, board and music options as well as exit
possibilities.

@author: elenasanchez & trecr
"""
import sys
import pygame
from pygame import mixer
from constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, RED, BLACK, GREY, BLUE
from game import Game
from button import Button

def get_pos_mouse(position):
    """
    This fucntion gets the position of the mouse the user is controlling.

    Parameters
    ----------
    position : Tuple
        DESCRIPTION.

    Returns
    -------
    row : Int
        Row location of mouse based on grid size.
    col : Int
        Column location of mouse based on grid size.

    """
    x, y = position
    row = y // SQUARE_SIZE # given current size
    col = x // SQUARE_SIZE

    return row, col

def main_menu():
    '''
    This function shows the main window of the pygame checkers game.

    Returns
    -------
    None.

    '''
    pygame.display.set_caption("Main Menu")
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (400, 150))
    run = True
    clock = pygame.time.Clock()
    WIN.fill("black")

    while run:
        clock.tick(FPS)
        menu_mouse_pos = pygame.mouse.get_pos()
        play_button = Button(button_face, pos = (400, 150), text_input = "QUICK PLAY",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black", hovering_color = "red")
        mode_button = Button(button_face, pos = (400, 300), text_input = "GAME MODE",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black",hovering_color = "red")
        options_button = Button(button_face, pos = (400, 450), text_input = "OPTIONS",
                                font = pygame.font.SysFont("couriernew", 50),
                                base_color = "black", hovering_color = "red")
        exit_button = Button(button_face, pos = (400, 600), text_input = "EXIT",
                             font=pygame.font.SysFont("couriernew", 50),
                             base_color = "black", hovering_color = "red")

        for selection in [play_button, mode_button, options_button, exit_button]:
            selection.color_change(menu_mouse_pos)
            selection.update(WIN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    instructions()
                if mode_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, RED)
                if options_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    options()
                if exit_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    run = False
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def end_game(winner):
    '''
    This fucntion takes declared winner and shows congratulatory message.

    Parameters
    ----------
    winner : Bool
        If True, red wins and if False white wins.

    Returns
    -------
    None.

    '''
    pygame.display.set_caption("Game Over")
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (400, 150))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("couriernew", 50)
    run = True
    WIN.fill("black")

    if winner is True:
        text = font.render("WHITE WINS!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        win_fx.play()

    if winner is False:
        text = font.render("RED WINS!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        win_fx.play()

    if winner is not True and winner is not False:
        text = font.render("YOU'RE OUT OF TIME!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        end_fx.play()

    while run:
        clock.tick(FPS)
        end_mouse_pos = pygame.mouse.get_pos()
        menu_button = Button(button_face, pos = (400, 300), text_input = "MAIN MENU",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black", hovering_color = "red")
        exit_button = Button(button_face, pos = (400, 450), text_input = "EXIT",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black",hovering_color = "red")

        for selection in [menu_button, exit_button]:
            selection.color_change(end_mouse_pos)
            selection.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.user_input(end_mouse_pos):
                    button_click_fx.play()
                    main_menu()
                if exit_button.user_input(end_mouse_pos):
                    button_click_fx.play()
                    run = False
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def instructions():
    '''
    This functions pulls up the intructions file and displays it if quick
    game is selected.

    Returns
    -------
    None.

    '''
    pygame.display.set_caption ('Press Enter to Continue')
    run = True
    clock = pygame.time.Clock()
    WIN.fill("black")
    instructions = [line.strip('\n')
                    for line in open('Instructions.txt', 'r').readlines()]

    font = pygame.font.Font("freesansbold.ttf", 16)
    for n, line in enumerate(instructions):
        text = font.render(line, 1, WHITE)
        text_rect = text.get_rect()
        text_rect.left = 100
        text_rect.centery = n * 50 + 50
        WIN.blit(text, text_rect)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()
                if event.key == pygame.K_RETURN:
                    button_click_fx.play()
                    play(mode = 0, color1 = BLACK, color2= RED)

        pygame.display.update()

def play(mode, color1, color2):
    '''
    This is the play fucntion which calls on to start the game.

    Parameters
    ----------
    mode : Int
        Showing what type of game is wanted: instructional, normal or timed.
    color1 : Str
        First color of the board.
    color2 : Str
        Second color of the board.

    Returns
    -------
    None.

    '''
    pygame.display.set_caption ('Game - Press Space Bar for Main Menu')
    run = True
    WIN.fill("black")
    clock = pygame.time.Clock()
    game = Game(WIN, mode, color1, color2)
    font_1 = pygame.font.SysFont("couriernew", 40)
    font_2 = pygame.font.SysFont("couriernew", 12)
    countdown = 0
    last_count = pygame.time.get_ticks()

    if mode == 0 or mode == 1:
        countdown = 0
        while run:
            clock.tick(FPS)
            if countdown == 0:
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
                            back_click_fx.play()
                            main_menu()

                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)
            game.update()

    if mode == 2:
        countdown = 60
        while run:
            clock.tick(FPS)
            if countdown > 0:
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

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
                            back_click_fx.play()
                            main_menu()

                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            if countdown == 0:
                draw_timer(str(0), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    if mode == 3:
        countdown = 120
        while run:
            clock.tick(FPS)
            if countdown > 0:
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

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
                            back_click_fx.play()
                            main_menu()

                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            if countdown == 0:
                draw_timer(str(0), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    if mode == 4:
        countdown = 3000
        while run:
            clock.tick(FPS)
            if countdown > 0:
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

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
                            back_click_fx.play()
                            main_menu()

                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)


            if countdown == 0:
                draw_timer(str(0), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    if mode == 5:
        countdown = 6000
        while run:
            clock.tick(FPS)
            if countdown > 0:
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

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
                            back_click_fx()
                            main_menu()

                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            if countdown == 0:
                draw_timer(str(0), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    pygame.quit()

def game_mode(inp1, inp2):
    '''
    This function allows for the user to select which type of game mode is wanted.
    The options are instructional (showing possible moves), normal or timed.
    There are also several options for timed modes.

    Parameters
    ----------
    inp1 : Str
        First color of the board.
    inp2 : Str
        Second color of the board.

    Returns
    -------
    None.

    '''
    pygame.display.set_caption('Game Mode - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    while run:
        clock.tick(FPS)
        WIN.fill("black")
        mode_mouse_pos = pygame.mouse.get_pos()
        instr_button = Button(button_face, pos=(400, 200), text_input = "INSTRUCTION MODE",
                              font = pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        norm_button = Button(button_face, pos=(400, 400), text_input = "NORMAL MODE",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color="black", hovering_color="red")
        timed_button = Button(button_face, pos=(400, 600), text_input = "TIMED MODE",
                              font = pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        for selection in [instr_button, norm_button, timed_button]:
            selection.color_change(mode_mouse_pos)
            selection.update(WIN)


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instr_button.user_input(mode_mouse_pos):
                    button_click_fx.play()
                    play(mode = 1, color1 = inp1, color2 = inp2)

                if norm_button.user_input(mode_mouse_pos):
                    button_click_fx.play()
                    play(mode = 0, color1 = BLACK, color2 = RED)

                if timed_button.user_input(mode_mouse_pos):
                    button_click_fx.play()
                    timer_selection(inp1, inp2)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def timer_selection(inp1, inp2):
    '''
    This fucntion allows fo rthe screen with the different games for the
    timed mode.

    Parameters
    ----------
    inp1 : Str
        First color of the board.
    inp2 : Str
        Second color of the board..

    Returns
    -------
    None.

    '''
    pygame.display.set_caption('Timer Selection - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    while run:
        clock.tick(FPS)
        WIN.fill("black")
        timed_mouse_pos = pygame.mouse.get_pos()
        min_button = Button(button_face, pos=(400, 150), text_input = "1-Minute",
                              font = pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        two_min_button = Button(button_face, pos=(400, 300), text_input = "2-Minutes",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color="black", hovering_color="red")
        five_min_button = Button(button_face, pos=(400, 450), text_input = "5-Minutes",
                              font = pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        ten_min_button = Button(button_face, pos=(400, 600), text_input = "10-Minutes",
                              font = pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        for selection in [min_button, two_min_button, five_min_button, ten_min_button]:
            selection.color_change(timed_mouse_pos)
            selection.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 2, color1 = inp1, color2 = inp2)
                if two_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 3, color1 = inp1, color2 = inp2)
                if five_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 4, color1 = inp1, color2 = inp2)
                if ten_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 5, color1 = inp1, color2 = inp2)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def draw_timer(text, font, color, x_pos, y_pos):
    """
    This fucntion draws the timer for the timed modes.

    Parameters
    ----------
    text : Str
        Time left.
    font : Object
        Type of font for text (pygame module).
    color : Str
        Color fo text.
    x_pos : Int
        Pixel for x position on the board.
    y_pos : Int
        Pixel for y position on the board.

    Returns
    -------
    None.

    """
    timer_image = font.render(text, True, color)
    timer_image_rect = timer_image.get_rect()
    timer_image_rect.centerx = x_pos
    timer_image_rect.centery = y_pos
    WIN.blit(timer_image, timer_image_rect)
    pygame.display.update()

def options():
    """
    This generates the options window where user can pick different board
    colors or decide to mute the sound.

    Returns
    -------
    None.

    """
    pygame.display.set_caption('Settings - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    while run:
        clock.tick(FPS)
        WIN.fill("black")
        opt_mouse_pos = pygame.mouse.get_pos()
        music_button = Button(button_face, pos=(400, 200), text_input = "MUSIC VOLUME",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        board_button = Button(button_face, pos=(400, 400), text_input = "BOARD COLOR",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        instruc_button = Button(button_face, pos=(400, 600), text_input = "INSTRUCTIONS",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        for selection in [music_button, board_button, instruc_button]:
            selection.color_change(opt_mouse_pos)
            selection.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    board_selection()

                if music_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    # need to define music function/screen
                    
                if instruc_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    instructions()
                    # need to define music function/screen

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def board_selection():
    """
    Function that allows user to pick the board color they want to play with.

    Returns
    -------
    None.

    """
    pygame.display.set_caption('Settings - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))
    while run:
        clock.tick(FPS)
        WIN.fill("black")
        opt_mouse_pos = pygame.mouse.get_pos()
        br_button = Button(button_face, pos=(400, 150), text_input = "Black/Red Board",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        bw_button = Button(button_face, pos=(400, 300), text_input = "Black/White Board",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        bg_button = Button(button_face, pos=(400, 450), text_input = "Black/Grey Board",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        bb_button = Button(button_face, pos=(400, 600), text_input = "Black/Blue Board",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        for selection in [br_button, bw_button, bg_button, bb_button]:
            selection.color_change(opt_mouse_pos)
            selection.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if br_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, RED)

                if bw_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, WHITE)

                if bg_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, GREY)

                if bb_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, BLUE)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

##############################################################################
FPS = 60
pygame.init()
mixer.init()
pygame.mixer.music.load('sounds/main_game2.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.10)
button_click_fx = pygame.mixer.Sound("sounds/button_click.wav")
button_click_fx.set_volume(0.75)
back_click_fx = pygame.mixer.Sound("sounds/back_to_menu.wav")
back_click_fx.set_volume(0.75)
win_fx = pygame.mixer.Sound("sounds/victory.wav")
win_fx.set_volume(0.75)
end_fx = pygame.mixer.Sound("sounds/times_up.wav")
end_fx.set_volume(0.75)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
main_menu()
