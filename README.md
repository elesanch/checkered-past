![jhu](https://user-images.githubusercontent.com/63515843/208501234-ec3800a5-d2fb-4ae8-af5f-2d2994b8d421.jpg)

# Checkered-Past!

This python program allows users to play a fun game of two-player Checkers on the 
same machine! The game grants users the opportunity to customize their checkers 
experience in many ways including:

        1. Game mode selections (standard, instructional, and timed!)
        2. Checkerboard color arrangement selection
        3. Game music selection

For beginners and/or users that are new to the game, instructions are offered in 
both the main menu and at the start of a "quick-play" game. Furthermore, the game's 
"Instructional Mode" gives players visual cues regarding their possible moves. 
The different timed modes offer an extra challenge for players that get comfortable
with the game interface! Enjoy the game - test your speed checkers skill and see 
if you and a friend can finish a game in less than a minute!

## Authors

Contributors:
        
        1. Elena Sanchez - esanch27@jhu.edu
        2. Ken Crittendon - kcritte1@jhu.edu

## Motivation

The code in this repository was developed to succesfully complete a collaborative 
final project that is part of the Software Carpentry course (EN.540.635) offered by the 
Johns Hopkins University Whiting School of Engineering. This project grants students 
the opportunity to combine the many python programming skills and techniques they 
learn over the course of the semester and poses challenges that forces them to 
use creative problem solving.This project also served as an opportunity to explore 
basic GUI development capabilities of python and its associated pygame library. 
Through the application of the various modules offered in pygame, we were able 
to develop a base knowledge of user-interface creation in python and form an 
understanding of how small details greatly impact the overall user-experience. 

## Build Status

The project currently allows users to play a "local" game of checkers in a standard, 
instructional, or timed variation. Given that the focus of this project was GUI 
development, there are various elements that could be added to the program to
improve the user-experience. A few things that could drive large improvement for 
the project are:

        1. Adding remote-play functionality where players can compete on different machines
        2. Adding  timer based on time lost during each player's turn (like chess)
        3. Adding more aesthetic detail to the checkerboard
        4. Adding a feature that allows users to change the color of their pieces
    
Even with the many opportunities for improvement, the current program allows users
to enjoy a fun and interactive digital checkers experience. 

## Code Description

The program starts the users off at the main menu where the primary music for 
the game begins playing immediately. From the main menu, the different features
of the game can be easily explored. Navigation to different interactive windows 
and game boards are goverened by the clicking of buttons. In general, the users 
have the option of going directly into gameplay where they are shown the instructions 
of the game and then allowed to play or return to the main menu; but they also 
have the option to customize the sounds, colors, and game mode for their match. 

The customizablity feature of this game is achieved through the use of different 
classes that were developed in separate files. Developing the game in this way 
allowed for greater organization of the code and relatively straightforward game
customization through the tweaking of different class objects. Each of these classes
funnel into one another in a cascading fashion and are handled in the main game 
file (main.py) through the use of various helper functions. Furthermore, sound 
effects are added in each of the files as well as the main file to enhance the 
user-experience. As previously mentioned, the class-separated organization of the
program allowed for easy adaptation of the code and more specifically the allocation
of different sounds to different actions. 

The checkers game functionality is handled similarly to game customization. As 
in real-life checkers, pieces are taken off the board whenever they are jumped 
by an oppoent and pieces cannot be moved to square where a piece already resides.
With standard checkers rules in mind (see acknowledgement), python lists of pieces were 
updated continously to track the movement and presence of the pieces on the digital board. 
Movement, captures and the board were visually handled using pygame's draw
functionality. Kings were also accounted for in this digital checkers game by 
superimposing an image of a crown onto pieces that achieved the "edge" locations 
of the board. The use of images was critical not only to the creation of king pieces, 
but also many of the other interactive objects in the game including buttons, timers, 
and user-messages (pygame is image-reliant). Finally, once a user's list of pieces 
was empty, the program was configured to acknowledge a winner which is simply 
the user who still has pieces present in their list. 

Successful completion of the game will result in a winner message that pops up 
for the user that captured all of their opponent's pieces. If the users are
playing a timed mode and time runs out before there is a winner, the game will 
be stopped and users have the option to play again or exit the game. The responsive
and smooth piece motion, addition of sound effects, variety of color schemes, and 
integration of different game modes make for a fun time between two people that 
have some time to kill!

## How to Use
All you need is a python3 IDE and/or interpreter. Ensure the pygame module is 
properly downloaded on your device as well. No additional software or hardware 
requirements need to be considered to run this program. Refer to the following 
steps for explicit instructions:

1. Ensure that you have python3 downloaded to your machine
    - If you do not have python3 - you can go here to download an easy to use IDE:
    [PyCharm](https://www.simplilearn.com/tutorials/python-tutorial/pycharm)

2. Download the zip file to your machine
    - Unzip the file to the location of your choice
    
3. Unzip the sounds follder that is found within your new checkers game folder
    - Keep this in your checkers game folder so that you have music and sounds
    in your game
    
4. Run main.py

5. Play the game!
    - Refer to "Instructions" in the game for more details on the gameplay

6. Force exit at anytime using the "x" in the top-right corner of the window

Feel free to email either of us using our contact information above with feedback
and/or suggestions for improvement.

## Inputs/Outputs

The program is primarily driven by users clicking their mouse or trackpad to make
in-game selections. Depending on the particular screen the user is on, the game
output will respond accordingly (ex. selection of piece and then selection of a
valid checkers move will show the piece "moving" to said square on the checkerboard). 
Ultimately, completion of the game will result in a winner message that pops up 
for the user that captured all of their opponent's pieces. If the users are
playing a timed mode and time runs out before there is a winner, the game will 
be stopped and users have the option to play again or exit the game.

## Acknowledgements

 - Colin Yancey (Instructor)
 - Anastasia Georgiou (Instructor)
 - [Checkers Rules](https://www.youtube.com/watch?v=ScKIdStgAfU)
 - [Checkers Base Game](https://www.youtube.com/watch?v=vnd3RfeG3NM)
 - [Pygame Buttons](https://www.youtube.com/watch?v=al_V4OGSvFU)
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
