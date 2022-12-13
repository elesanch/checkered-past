# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:04:22 2022

@author: trecr
"""
import pygame
import sys
from constants import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAY")
main_font = pygame.font.SysFont("couriernew", 50)

class Button():
    def __init__(self, image, x, y, text_input):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center = (self.x, self.y))
        
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
            
    def user_input(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            print("BUTTON CLICKED")
        
    def color_change(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "red")
        else:
            self.text = main_font.render(self.text_input, True, "black")

## The code below was ran to test the functionality of the class             
# button_face = pygame.image.load("button.jpg")
# button_face = pygame.transform.scale(button_face, (400, 150))

# play_button = Button(button_face, 400, 150, "PLAY")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             play_button.user_input(pygame.mouse.get_pos())
            
#     screen.fill("black")
#     play_button.update()
#     play_button.color_change(pygame.mouse.get_pos())
#     pygame.display.update()
