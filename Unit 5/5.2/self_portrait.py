import pygame
import math

def drawStuff(background):
    """ given a Surface, this function draws a bunch of
    shapes on it """

    # draw polygon
    points = ((137, 372), (232, 319), (383, 335), (442, 389),
              (347, 432), (259, 379), (220, 439), (132, 392))
    pygame.draw.polygon(background, (0x33, 0xFF, 0x33), points)

def main():
    # Initialize Pygame
    pygame.init()

    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing commands")

    # E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    background.fill((255, 255, 255))
    drawStuff(background)

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

    # L - Loop
    while keepGoing:
        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())

        # R - Refresh display
        screen.blit(background, (0, 0))
        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()

