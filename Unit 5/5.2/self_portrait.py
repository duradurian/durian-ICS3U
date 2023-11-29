import pygame
pygame.init()

def drawStuff(background):
    """ given a Surface, this function draws a bunch of
    shapes on it """

    # hair coords
    hair_points = ((201, 70),(214, 148),(224, 92),(238, 147),(259, 93),
              (273, 148),(287, 109),(297, 155),(313, 112),(334, 149),(356, 117),(385, 146),
              (417, 99),(409, 40),(381, 24),(308, 18),(255, 19),(169, 43),(170, 100),(177, 159))
    
    # Mouth coords
    coordinates = (
                (231, 217),(234, 223),(241, 227),(246, 229),(258, 229),(268, 229),
                (276, 229),(283, 228),(293, 226),(301, 224),(304, 223))

    pygame.draw.circle(background, (210,180,100), (295, 159), 125)
    pygame.draw.circle(background, (0, 0, 0), (238, 157), 10)
    pygame.draw.circle(background, (0, 0, 0), (295, 160), 10)
    pygame.draw.polygon(background, (0, 0, 0), hair_points)
    pygame.draw.polygon(background, (0, 0, 0), coordinates)

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

