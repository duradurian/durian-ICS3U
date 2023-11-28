"""
Author: Darrien Guan
Date: November 27, 2023
Disc: Modified code from example, pink
box moves diagonally on a white bg.
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
box_x = 0
box_y = 0

# ACTION

# Assign 
clock = pygame.time.Clock()
keepGoing = True

box_x_path = True
box_y_path = True

# Loop
while keepGoing:

    # Time
    clock.tick(100)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    # modify box value
    if box_y_path == True:
        box_y += 1
    else: box_y -= 1
    
    if box_x_path == True:
        box_x += 1
    else: box_x -= 1
    
    # check boundaries and change direction
    if box_x < 0 or box_x > 640 - 25:
        box_x_path = not box_x_path
        
    if box_y < 0 or box_y > 480 - 25:
        box_y_path = not box_y_path

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()

# Close the game window
pygame.quit()