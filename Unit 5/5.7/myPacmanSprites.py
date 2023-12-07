"""
Author: Darrien Guan
Date: Dec 6
Disc: Pacman sprites.
"""

import pygame
import random

pygame.init()

class Cherry(pygame.sprite.Sprite):
    """Displays cherry in random location on screen."""
    
    def __init__(self, screen):
        
        pygame.sprite.Sprite.__init__(self)
        
        # Set image attributes
        self.image = pygame.image.load("cherries.gif")
        self.image = self.image.convert()
        
        # Get rect attributes
        self.rect = self.image.get_rect()
        
        self.rect.left = random.randrange(30, screen.get_width()-30)
        self.rect.top = random.randrange(30, screen.get_height()-30)

class Pacman(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        
        pygame.sprite.Sprite.__init__(self)
        
        # Load all files
        self.right_pacman = pygame.image.load("pacman-right.gif")
        self.left_pacman = pygame.image.load("pacman-left.gif")
        self.up_pacman = pygame.image.load("pacman-up.gif")
        self.down_pacman = pygame.image.load("pacman-down.gif")
        
        # Start with pacman facing right
        self.image = self.right_pacman.convert()
        
        # Get rect attributes
        self.rect = self.image.get_rect()
        
        self.rect.left = screen.get_width()/2
        self.rect.top = screen.get_height()/2
        
    def go_left(self):
        self.image = self.left_pacman.convert()
        self.rect.left -= 5
        
    def go_right(self):
        self.image = self.right_pacman.convert()
        self.rect.left += 5
        
    def go_up(self):
        self.image = self.up_pacman.convert()
        self.rect.top -= 5
        
    def go_down(self):
        self.image = self.down_pacman.convert()
        self.rect.top += 5
        
    def update(self, screen):
        
        # Sends sprite to opposite corner if the sprite's position exceeds window.
        if self.rect.left > screen.get_width():
            self.rect.left = 0
        
        if self.rect.left < 0:
            self.rect.left = screen.get_width()
            
        if self.rect.top > screen.get_height():
            self.rect.top = 0
            
        if self.rect.top < 0:
            self.rect.top = screen.get_height()
