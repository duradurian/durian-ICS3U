"""
Author: Darrien Guan
Date: Dec 6
Disc: Test of pacman movement.
"""

import myPacmanSprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

def main():
    '''mainline logic'''
    
    pygame.display.set_caption("Pacman movement test")
    
    pacman = myPacmanSprites.Pacman(screen)
        
    allSprites = pygame.sprite.Group(pacman)
    
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
                
            if event.type == pygame.KEYDOWN:
                
                # PACMAN MOVEMENT (WASD)
                if event.key == pygame.K_w:
                    pacman.go_up()
                    
                if event.key == pygame.K_a:
                    pacman.go_left()
                    
                if event.key == pygame.K_s:
                    pacman.go_down()
                    
                if event.key == pygame.K_d:
                    pacman.go_right()
                
        # Refresh screen
        allSprites.update(screen)
        
        # Draw objects
        screen.fill((255,255,255))
        allSprites.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    
main()