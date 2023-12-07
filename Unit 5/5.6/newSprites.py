"""
Author: Darrien Guan
Date: Dec 5
Disc: Circle sprite with colour parameter.
"""

import pygame
import random

class Circle(pygame.sprite.Sprite):
    '''Our Circle class inherits from the Sprite class'''
    def __init__(self, colour: tuple):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the circle
        self.image = pygame.Surface((50, 50))
        self.image.fill((colour))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        
    def update(self):
        # Move the center of the circle to where the mouse is pointing
        self.rect.center = pygame.mouse.get_pos()

        
class Label(pygame.sprite.Sprite):
    def __init__(self, message, x_y_center, font_name, size, rgb:tuple):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont(font_name, size)
        self.__text = message
        self.__center = x_y_center
        self.__color = rgb
        
    def set_text(self, message):
        self.__text = message
                
    def update(self):
        self.image = self.__font.render(self.__text, 1, (self.__color))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center


class Brick(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.screen = screen

        # Set the image attribute for our Brick sprite
        self.image = pygame.image.load("bricks.png")
        self.image = self.image.convert()

        # Set the rect attribute for our Brick sprite
        self.rect = self.image.get_rect()
        
        # Set the initial position randomly
        self.rect.left = random.randrange(0, screen.get_width() - self.rect.width)
        self.rect.top = random.randrange(0, screen.get_height() - self.rect.height)

        self.__directionX = 5
        self.__directionY = 5

    def update(self):
        self.rect.left += self.__directionX
        self.rect.top += self.__directionY
        
        if (self.rect.left < 0) or (self.rect.right > self.screen.get_width()):
            self.__directionX = -self.__directionX
            
        if (self.rect.top < 0) or (self.rect.bottom > self.screen.get_height()):
            self.__directionY = -self.__directionY
