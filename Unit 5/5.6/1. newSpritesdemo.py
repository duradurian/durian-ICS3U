"""
Author: Darrien Guan
Date: Dec 5
Disc: Circle, brick, and label sprite.
"""

import pygame
import newSprites
pygame.init()
screen = pygame.display.set_mode((640, 480))

            
def main():
    '''This function defines the 'mainline logic' for our game.'''
    
    # Display
    pygame.display.set_caption("Basic Sprite Demo")
    
    # Create sprite groups
    allSprites = pygame.sprite.Group()
    circles = pygame.sprite.Group()

    # Create instances of your sprites
    circle = newSprites.Circle((255, 0, 0))  # Red circle

    # Add sprites to groups
    allSprites.add(circle)
    circles.add(circle)
    
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

        # Refresh screen
        allSprites.update()

        # Draw objects
        screen.fill((255, 255, 255))  # White background
        allSprites.draw(screen)

        pygame.display.flip()
   
    # Close the game window
    pygame.quit()        
        

# Call the main function
main()