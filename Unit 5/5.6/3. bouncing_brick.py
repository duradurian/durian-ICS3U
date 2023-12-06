"""
Author: Darrien Guan
Date: Dec 5
Disc: Bouncing brick with collision.
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
    all_sprites = pygame.sprite.Group()

    brick_list = []
    
    # Create instances of your sprites
    for i in range(25):
        brick_list.append(newSprites.Brick(screen))

    brick_group = pygame.sprite.Group(brick_list)  # Rename the group to 'brick_group'

    # Add sprites to groups
    all_sprites.add(brick_group)  # Add the group, not the list

    # Assign
    clock = pygame.time.Clock()
    keep_going = True

    # Loop
    while keep_going:

        # Time (Adjusted to 60 fps to prevent screen ghosting)
        clock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        # Refresh screen
        all_sprites.update()

        # Draw objects
        screen.fill((0, 0, 0))  # White background
        all_sprites.draw(screen)

        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
