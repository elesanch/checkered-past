"""
This is the main file for the checkers game. This fule contains all information
on the user interface (UI) design of this game. The file encompasses, the
different screens, modes of play, board and music options as well as exit
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
    x, y = position         # track mouse position on screen
    row = y // SQUARE_SIZE  # given current size
    col = x // SQUARE_SIZE  # given current size

    return row, col

def main_menu():
    '''
    This function shows the main window of the pygame checkers game.

    Returns
    -------
    None.

    '''
    # Primary settings for the main menu window and important variable creation
    pygame.display.set_caption("Main Menu")
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (400, 150))
    run = True
    clock = pygame.time.Clock()
    WIN.fill("black")

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems

        # Creation of buttons and mouse tracking to get user seletions
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

        # UI feedback to show user can select a button with cursor
        for selection in [play_button, mode_button, options_button, exit_button]:
            selection.color_change(menu_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Shuts down pygame if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Changes game screen based on use-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Brings users to instructions screen
                if play_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    instructions()

                # Brings users to mode selection screen
                if mode_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, RED)

                # Brings users to options selection screen
                if options_button.user_input(menu_mouse_pos):
                    button_click_fx.play()
                    options()

                # Shuts down the game if the exit button is selected
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
    # Primary settings for the winner window and important variable creation
    pygame.display.set_caption("Game Over")
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (400, 150))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("couriernew", 50)
    run = True
    WIN.fill("black")

    # True argument indicates that WHITE pieces win the game (see game.py)
    if winner is True:
        text = font.render("WHITE WINS!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        win_fx.play()               # Congratulatory sound

    # False argument indicates that RED pieces win the game (see game.py)
    if winner is False:
        text = font.render("RED WINS!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        win_fx.play()               # Congratulatory sound

    # Handles case of time running out and no-one winning
    if winner is not True and winner is not False:
        text = font.render("YOU'RE OUT OF TIME!", True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = 400
        text_rect.centery = 150
        WIN.blit(text, text_rect)
        end_fx.play()               # Halt noise indicating end of the game

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems

        # Creation of buttons and mouse tracking to get user seletions
        end_mouse_pos = pygame.mouse.get_pos()
        menu_button = Button(button_face, pos = (400, 300), text_input = "MAIN MENU",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black", hovering_color = "red")
        exit_button = Button(button_face, pos = (400, 450), text_input = "EXIT",
                             font = pygame.font.SysFont("couriernew", 50),
                             base_color = "black",hovering_color = "red")

        # UI feedback to show user can select a button with cursor
        for selection in [menu_button, exit_button]:
            selection.color_change(end_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on use-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Brings users back to the main menu
                if menu_button.user_input(end_mouse_pos):
                    button_click_fx.play()
                    main_menu()

                # Allows user to close out of the game with a button click
                if exit_button.user_input(end_mouse_pos):
                    button_click_fx.play()
                    run = False
                    pygame.quit()
                    sys.exit()

            # Shuts down pygame if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def instructions():
    '''
    This functions pulls up the intructions file and displays it if quick
    game is selected or if users need to review the ins and outs of the game.

    Returns
    -------
    None.

    '''
    # Primary settings for the instructions window and important variable creation
    pygame.display.set_caption ('Press Enter to Continue')
    run = True
    clock = pygame.time.Clock()
    WIN.fill("black")

    # Accesses the content in the instructions txt file
    instructions = [line.strip('\n')
                    for line in open('Instructions.txt', 'r').readlines()]

    # Sets font and size of text to be printed in the UI
    font = pygame.font.Font("freesansbold.ttf", 16)

    # Updates the instructions window with context read from the above txt file
    for n, line in enumerate(instructions):
        text = font.render(line, 1, WHITE)
        text_rect = text.get_rect()
        text_rect.left = 100
        text_rect.centery = n * 50 + 50
        WIN.blit(text, text_rect)

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Allows user to close out of the game with a button click
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

                # Advances users to gameplay upon press of the return/enter key
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
    # Primary settings for the game window and important variable creation
    pygame.display.set_caption ('Game - Press Space Bar for Main Menu')
    run = True
    WIN.fill("black")
    clock = pygame.time.Clock()
    game = Game(WIN, mode, color1, color2)
    font_1 = pygame.font.SysFont("couriernew", 40)
    font_2 = pygame.font.SysFont("couriernew", 12)
    countdown = 0                           # establishes game time limit
    last_count = pygame.time.get_ticks()    # gets last time for countdown

    # The following blocks of code establish times based on different game
    # modes selected by the user. Thse game modes are registered as integers
    # with the standard mode being mode 0.
    if mode == 0 or mode == 1:
        countdown = 0           # no time limit for the standard mode

        # Starts game loop
        while run:
            clock.tick(FPS)     # Used to standardize frame rate across systems

            # Countdown is 0 so the game will run as normal
            if countdown == 0:

                # Tracks game actions and adapts UI based on realized actions
                for event in pygame.event.get():
                    # Shuts down pygame if the exit button is selected
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    # Changes game screen based on user-input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_pos_mouse(pos)
                        game.select(row,col)

                    # Brings users back to the main menu if spacebar is clicked
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            back_click_fx.play()
                            main_menu()

                    # Sends winner message to players
                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)
            game.update()

    # 1-mintue game mode
    if mode == 2:
        countdown = 60          # Start game with 60 seconds

        # Starts game loop
        while run:
            clock.tick(FPS)     # Used to standardize frame rate across systems
            # Allows gameplay as long as there is time left
            if countdown > 0:
                # Shows timer of the screen
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()

                # Updates timer
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

                # Tracks game actions and adapts UI based on realized actions
                for event in pygame.event.get():
                    # Shuts down pygame if the exit button is selected
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    # Changes game screen based on user-input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_pos_mouse(pos)
                        game.select(row,col)

                    # Brings users back to the main menu if spacebar is clicked
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            back_click_fx.play()
                            main_menu()

                    # Sends winner message to players
                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            # Stops gameplay once time runs out
            if countdown == 0:
                draw_timer(countdown, font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)      # brief delay before screen switch
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    # 2-Minute game mode
    if mode == 3:
        countdown = 120         # Start game with 120 seconds

        # Starts game loop
        while run:
            clock.tick(FPS)     # Used to standardize frame rate across systems
            # Allows gameplay as long as there is time left
            if countdown > 0:
                # Shows timer of the screen
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()

                # Updates timer
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

                # Tracks game actions and adapts UI based on realized actions
                for event in pygame.event.get():
                    # Shuts down pygame if the exit button is selected
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    # Changes game screen based on user-input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_pos_mouse(pos)
                        game.select(row,col)

                    # Brings users back to the main menu if spacebar is clicked
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            back_click_fx.play()
                            main_menu()

                    # Sends winner message to players
                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            # Stops gameplay once time runs out
            if countdown == 0:
                draw_timer(countdown, font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)      # brief delay before screen switch
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    # 5-Minute game mode
    if mode == 4:
        countdown = 3000        # Start game with 3000 seconds

        # Starts game loop
        while run:
            clock.tick(FPS)     # Used to standardize frame rate across systems
            # Allows gameplay as long as there is time left
            if countdown > 0:
                # Shows timer of the screen
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()

                # Updates timer
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

                # Tracks game actions and adapts UI based on realized actions
                for event in pygame.event.get():
                    # Shuts down pygame if the exit button is selected
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    # Changes game screen based on user-input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_pos_mouse(pos)
                        game.select(row,col)

                    # Brings users back to the main menu if spacebar is clicked
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            back_click_fx.play()
                            main_menu()

                    # Sends winner message to players
                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            # Stops gameplay once time runs out
            if countdown == 0:
                draw_timer(countdown, font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)      # brief delay before screen switch
                WIN.fill(BLACK)
                end_game(game.winner())

            game.update()

    # 10-Minute game mode
    if mode == 5:
        countdown = 6000        # Start game with 6000 seconds

        # Starts game loop
        while run:
            clock.tick(FPS)     # Used to standardize frame rate across systems
            # Allows gameplay as long as there is time left
            if countdown > 0:
                # Shows timer of the screen
                draw_timer(str(countdown), font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                count_timer = pygame.time.get_ticks()

                # Updates timer
                if count_timer - last_count > 1000:
                    countdown -= 1
                    last_count = count_timer

                # Tracks game actions and adapts UI based on realized actions
                for event in pygame.event.get():
                    # Shuts down pygame if the exit button is selected
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        sys.exit()

                    # Changes game screen based on user-input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        row, col = get_pos_mouse(pos)
                        game.select(row,col)

                    # Brings users back to the main menu if spacebar is clicked
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            back_click_fx.play()
                            main_menu()

                    # Sends winner message to players
                    if game.winner() is True:
                        end_game(True)

                    if game.winner() is False:
                        end_game(False)

            # Stops gameplay once time runs out
            if countdown == 0:
                draw_timer(countdown, font_1, WHITE, 50, 33)
                draw_timer("Seconds Left", font_2, WHITE, 50, 66)
                pygame.time.delay(500)      # brief delay before screen switch
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
    # Primary settings for the game mode window and important variable creation
    pygame.display.set_caption('Game Mode - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems
        WIN.fill("black")

        # Creation of buttons and mouse tracking to get user seletions
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

        # UI feedback to show user can select a button with cursor
        for selection in [instr_button, norm_button, timed_button]:
            selection.color_change(mode_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on user-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Users will play a game that gives them a helping hand
                if instr_button.user_input(mode_mouse_pos):
                    button_click_fx.play()
                    play(mode = 1, color1 = inp1, color2 = inp2)

                # Users will play a standard game of checkers
                if norm_button.user_input(mode_mouse_pos):
                    button_click_fx.play()

                    # Tracks board color selection and updates game board
                    if inp1 == None or inp2 == None:
                        play(mode = 0, color1 = BLACK, color2 = RED)
                    else:
                        play(mode = 0, color1 = inp1, color2 = inp2)

                # Users will play a timed game of checkers
                if timed_button.user_input(mode_mouse_pos):
                    button_click_fx.play()
                    timer_selection(inp1, inp2)

            # Shuts down the game if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def timer_selection(inp1, inp2):
    '''
    This fucntion allows for the screen with the different games for the
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
    # Primary settings for the timer window and important variable creation
    pygame.display.set_caption('Timer Selection - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems
        WIN.fill("black")

        # Creation of buttons and mouse tracking to get user seletions
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

        # UI feedback to show user can select a button with cursor
        for selection in [min_button, two_min_button, five_min_button, ten_min_button]:
            selection.color_change(timed_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on user-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Users will play a 2-minute game on a board color they chose
                if min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 2, color1 = inp1, color2 = inp2)

                # Users will play a 2-minute game on a board color they chose
                if two_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 3, color1 = inp1, color2 = inp2)

                # Users will play a 5-minute game on a board color they chose
                if five_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 4, color1 = inp1, color2 = inp2)

                # Users will play a 10-minute game on a board color they chose
                if ten_min_button.user_input(timed_mouse_pos):
                    button_click_fx.play()
                    play(mode = 5, color1 = inp1, color2 = inp2)

            # Shuts down the game if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
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
    # Creates timer image and displays it in the top right corner of the board
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
    # Primary settings for the options window and important variable creation
    pygame.display.set_caption('Settings - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems
        WIN.fill("black")

        # Creation of buttons and mouse tracking to get user seletions
        opt_mouse_pos = pygame.mouse.get_pos()
        music_button = Button(button_face, pos=(400, 200), text_input = "MUSIC",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        board_button = Button(button_face, pos=(400, 400), text_input = "BOARD COLOR",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        instruc_button = Button(button_face, pos=(400, 600), text_input = "INSTRUCTIONS",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        # UI feedback to show user can select a button with cursor
        for selection in [music_button, board_button, instruc_button]:
            selection.color_change(opt_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on user-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Users will go to board selection by clicking this button
                if board_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    board_selection()

                # Users will go to sound selection by clicking this button
                if music_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    music_selection()

                # Users will get to read instructions by clicking this button
                if instruc_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    instructions()

            # Shuts down the game if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

def music_selection():
    """
    Function that allows user to pick sound settings they want to play with.

    Returns
    -------
    None.

    """
    # Primary settings for the music window and important variable creation
    pygame.display.set_caption('Music Settings - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 140))

    # Starts game loop
    while run:
        clock.tick(FPS)       # Used to standardize frame rate across systems
        WIN.fill("black")

        # Creation of buttons and mouse tracking to get user seletions
        music_mouse_pos = pygame.mouse.get_pos()
        song0_button = Button(button_face, pos=(400, 100), text_input = "Music Option 0",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        song1_button = Button(button_face, pos=(400, 240), text_input = "Music Option 1",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        song2_button = Button(button_face, pos=(400, 380), text_input = "Music Option 2",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        song3_button = Button(button_face, pos=(400, 520), text_input = "Music Option 3",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")
        mute_button = Button(button_face, pos=(400, 660), text_input = "Mute",
                              font=pygame.font.SysFont("couriernew", 50),
                              base_color="black", hovering_color="red")

        # UI feedback to show user can select a button with cursor
        for selection in [song0_button, song1_button, song2_button, song3_button, mute_button]:
            selection.color_change(music_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on user-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play original song variation with this selection
                if song0_button.user_input(music_mouse_pos):
                    button_click_fx.play()
                    pygame.mixer.music.load('sounds/main_game.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                    pygame.mixer.music.set_volume(0.10)
                    main_menu()
                    
                # Play song variation 1 with this selection
                if song1_button.user_input(music_mouse_pos):
                    button_click_fx.play()
                    pygame.mixer.music.load('sounds/main_game1.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                    pygame.mixer.music.set_volume(0.10)
                    main_menu()

                # Play song variation 2 with this selection
                if song2_button.user_input(music_mouse_pos):
                    pygame.mixer.music.load('sounds/main_game2.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                    pygame.mixer.music.set_volume(0.10)
                    main_menu()

                # Play song variation 3 with this selection
                if song3_button.user_input(music_mouse_pos):
                    pygame.mixer.music.load('sounds/main_game4.mp3')
                    pygame.mixer.music.play(-1, 0.0)
                    pygame.mixer.music.set_volume(0.10)
                    main_menu()

                # Turn off game music with this selection
                if mute_button.user_input(music_mouse_pos):
                    pygame.mixer.music.stop()
                    main_menu()

            # Shuts down the game if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
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
    # Primary settings for the window and important variable creation
    pygame.display.set_caption('Board Settings - Press Space Bar for Main Menu')
    run = True
    clock = pygame.time.Clock()
    button_face = pygame.image.load("button.jpg")
    button_face = pygame.transform.scale(button_face, (600, 150))

    # Starts game loop
    while run:
        clock.tick(FPS)         # Used to standardize frame rate across systems
        WIN.fill("black")

        # Creation of buttons and mouse tracking to get user seletions
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

        # UI feedback to show user can select a button with cursor
        for selection in [br_button, bw_button, bg_button, bb_button]:
            selection.color_change(opt_mouse_pos)
            selection.update(WIN)

        # Tracks game actions and adapts UI based on realized actions
        for event in pygame.event.get():
            # Changes game screen based on use-input
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Users will play on a normal black and red board
                if br_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, RED)

                # Users will play on a black and white board
                if bw_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, WHITE)

                # Users will play on a black and grey board
                if bg_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, GREY)

                # Users will play on a black and blue board
                if bb_button.user_input(opt_mouse_pos):
                    button_click_fx.play()
                    game_mode(BLACK, BLUE)

            # Shuts down the game if the exit button is selected
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # Brings users back to the main menu if spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    back_click_fx.play()
                    main_menu()

        pygame.display.update()

##############################################################################
pygame.init()   # Initialize pygame to run checkers game and its variations
mixer.init()    # Initialize mixer to create sounds for the game
FPS = 60        # Sets frame rate to 60 frames per second (for all functions)

# Initial game music that can be changed by users
pygame.mixer.music.load('sounds/main_game.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.10)

# Sounds effects used throughout the different game functions
button_click_fx = pygame.mixer.Sound("sounds/button_click.wav")
button_click_fx.set_volume(0.75)
back_click_fx = pygame.mixer.Sound("sounds/back_to_menu.wav")
back_click_fx.set_volume(0.75)
win_fx = pygame.mixer.Sound("sounds/victory.wav")
win_fx.set_volume(0.75)
end_fx = pygame.mixer.Sound("sounds/times_up.wav")
end_fx.set_volume(0.75)

# Creates pygame window of size 800 by 800 (defined in constants.py)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Begin game from main menu
main_menu()
