"""
Author: Darrien Guan
Date: November 27, 2023
Disc: Program has four different boxes
moving in different directions.
Boxes repeated move.
"""

# Initialize
import pygame
pygame.init()

# Display
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption("move a box")

# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 50, 0))

# make a red 25 x 25 box
box1 = pygame.Surface((25, 25))
box2 = pygame.Surface((25, 25))
box3 = pygame.Surface((25, 25))
box4 = pygame.Surface((25, 25))

box1 = box1.convert()
box2 = box2.convert()
box3 = box3.convert()
box4 = box4.convert()

box1.fill((255, 255, 255))
box2.fill((20, 42, 231))
box3.fill((244, 0, 0))
box4.fill((232, 255, 0))

# set up some box variables
box1_x = 240
box1_y = 0

box2_x = 480-25
box2_y = 0

box3_x = 0
box3_y = 0

box4_x = 0
box4_y = 240

# ACTION

# Assign 
clock = pygame.time.Clock()
keepGoing = True

# Loop
while keepGoing:

    # Time
    clock.tick(100)

    # Spectrum cycling background
    
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    # modify box value
    box2_x -= 1
    box2_y += 1
    
    box3_x += 1
    box3_y += 1
    
    box1_y += 1
    box4_x += 1
    
    # reset boxes to appear from opposite side.
    if box1_y > 480:
        box1_y = 0
        
    if box4_x > 480:
        box4_x = 0
    
    if box2_y > 480:
        box2_x = 480-25
        box2_y = 0
        
    if box3_y > 480:
        box3_x = 0
        box3_y = 0

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box1, (box1_x, box1_y))
    screen.blit(box2, (box2_x, box2_y))
    screen.blit(box3, (box3_x, box3_y))
    screen.blit(box4, (box4_x, box4_y))
    pygame.display.flip()

# Close the game window
pygame.quit()