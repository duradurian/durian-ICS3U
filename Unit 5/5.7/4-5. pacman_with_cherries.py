"""
Author: Darrien Guan
Date: Dec 6
Disc: Pacman simple minigame
"""

import myPacmanSprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

def main():
    '''mainline logic'''
    
    pygame.display.set_caption("10 Random Cherries")
    
    # Sprites
    pacman = myPacmanSprites.Pacman(screen)
    
    cherry_walls = pygame.sprite.Group()
    
    # Create 10 instances of the cherry sprite.
    for i in range(10):
        cherry_walls.add(myPacmanSprites.Cherry(screen))

    allSprites = pygame.sprite.Group(cherry_walls, pacman)
    
    # Entities
    eating_sfx = pygame.mixer.Sound("eating.mp3")
    
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

        # To keep pacman constantly moving with keep press down (Method learned from past projects).
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            pacman.go_up()
        if keys[pygame.K_DOWN]:
            pacman.go_down()

        if keys[pygame.K_RIGHT]:
            pacman.go_right()
        if keys[pygame.K_LEFT]:
            pacman.go_left()

        # Multiple-sprite collision detection and reporting.
        collisions = pygame.sprite.spritecollide(pacman, cherry_walls, True)  # Set True to remove cherries on collision

        for cherry in collisions:
            eating_sfx.play()

        # Refresh screen
        allSprites.update(screen)

        # Draw objects
        screen.fill((255, 255, 255))
        allSprites.draw(screen)

        pygame.display.flip()
        
    pygame.quit()
    
main()