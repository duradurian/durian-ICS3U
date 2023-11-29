"""
Author: Darrien Guan
Date: November 27, 2023
Disc: Modified code from example, green box, brown bg, 
box moves top to bottom repeatedly.
"""

# Initialize
import pygame
pygame.init()

# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("move a box")

# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 50, 0))

# make a red 25 x 25 box
box = pygame.Surface((25, 25))
box = box.convert()
box.fill((0, 255, 0))

# set up some box variables
box_x = 320
box_y = 200

# ACTION

# Assign 
clock = pygame.time.Clock()
keepGoing = True

# Loop
while keepGoing:

    # Time
    clock.tick(30)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    # modify box value
    box_y += 5
    
    # check boundaries and reset position
    if box_y > 480:
        box_y = 0

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()

# Close the game window
pygame.quit()