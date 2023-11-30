import pygame
pygame.init()

def main():
    '''main logic'''
    
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("display some text")
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    
    # Get user input
    name = input("Please enter the user's name: ")

    mySystemFont = pygame.font.SysFont("Regular", 60)
    label1 = mySystemFont.render(name, 1, (0, 0, 0))
    
    portrait = pygame.image.load("portrait.png")
    portrait = portrait.convert()

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

        # R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(portrait, (40, 80))
        screen.blit(label1, (30, 30))
        pygame.display.flip()
    
    # Close the game window
    pygame.quit()

# Call the main function
main()
