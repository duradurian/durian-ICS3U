"""
Author: Darrien Guan
Date: Dec 5
Disc: Modified label sprite.
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
    labels = pygame.sprite.Group()  # Rename the group to 'labels'

    # Create instances of your sprites
    label_sprite = newSprites.Label("ICS3U1!!!!!", (320, 50), None, 30, (255, 255, 0))  # Red circle
    # Rename the sprite to 'label_sprite'

    # Add sprites to groups
    all_sprites.add(label_sprite)
    labels.add(label_sprite)  # Use 'labels' group here

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
