"""
Author: Darrien Guan
Date: Dec 4, 2023
Disc: Modifed code from example, replaced box with image.
"""

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

class Box(pygame.sprite.Sprite):
    '''Our Box class inherits from the Sprite class'''
    def __init__(self, color: tuple, starting_location: tuple):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image attribute for our Box sprite
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill(color)
        
        # Set the rect attribute for our Box sprite
        self.rect = self.image.get_rect()
        self.rect.left = starting_location[0]
        self.rect.top = starting_location[1]
        self.__directionX = 5
        self.__directionY = 5

    def update(self, sound_variable):
        self.rect.left += self.__directionX
        self.rect.top += self.__directionY
        
        if (self.rect.left < 0) or (self.rect.right > screen.get_width()):
            self.__directionX = -self.__directionX
            sound_variable.play()
            
        if (self.rect.top < 0) or (self.rect.bottom > screen.get_height()):
            self.__directionY = -self.__directionY
            sound_variable.play()
            
def random_colour():
    '''returns random SRGB colour in tuple format'''
    return ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            
def main():
    '''This function defines the 'mainline logic' for our game.'''
    
    # Display
    pygame.display.set_caption("Basic Sprite Demo: e(add extra)")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))
    bounce = pygame.mixer.Sound("boing.wav")
    
    # create a Box sprite objects
    box1 = Box(random_colour(), (random.randint(40,600),random.randint(40,440)))
    box2 = Box(random_colour(), (random.randint(40,600),random.randint(40,440)))
    box3 = Box(random_colour(), (random.randint(40,600),random.randint(40,440)))
    
    box_list = [box1,box2,box3]
    allSprites = pygame.sprite.Group(box_list)
    
    # ACTION
    
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Loop
    while keepGoing:
    
        # Time (Adjusted to 60 fps to prevent screen ghosting)
        clock.tick(60)
    
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_e:
                    new_box = Box(random_colour(), (random.randint(0,640),random.randint(0,480)))
                    box_list.append(new_box)
                    allSprites.add(new_box)

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update(bounce)
        allSprites.draw(screen)
    
        pygame.display.flip()
   
    # Close the game window
    pygame.quit()        
        

# Call the main function
main()