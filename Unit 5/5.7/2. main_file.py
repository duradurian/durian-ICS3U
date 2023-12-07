"""
Author: Darrien Guan
Date: Dec 6
Disc: Test Cherry Sprite.
"""

import myPacmanSprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

def main():
    '''mainline logic'''
    
    pygame.display.set_caption("10 Random Cherries")
    
    # Sprites
    cherry_list = []
    
    # Create 10 instances of the cherry sprite.
    for i in range(10):
        cherry_list.append(myPacmanSprites.Cherry(screen))
        
    allSprites = pygame.sprite.Group(cherry_list)
    
    # Variables
    clock = pygame.time.Clock()
    keep_going = True
    
    # Main game loop
    while keep_going:
        
        # Time
        clock.tick(60)
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
                
        # Refresh screen
        allSprites.update()
        
        # Draw objects
        screen.fill((255,255,255))
        allSprites.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    
main()