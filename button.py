# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:04:22 2022

@author: trecr
"""
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.x = pos[0]
        self.y = pos[1]
        self.image = image
        self.font = font
        self.text_input = text_input
        self.base_color= base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.text_rect = self.text.get_rect(center = (self.x, self.y))
        
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
            
    def user_input(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def color_change(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
