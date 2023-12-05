"""
Author: Darrien Guan
Date: December 1, 2023
Disc: Modified code from paint program example. Added additional features such as loading, and other coloured lines.
"""

# I - Import and Initialize
import pygame
pygame.init()

def statusSurface(drawColor, lineWidth):
    """creates a Surface object for status text"""
    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (drawColor, lineWidth)
    status = myFont.render(status_string, 1, (drawColor))
    return status

def main():
    '''This function defines the 'mainline logic' for our paint program.'''
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint: (w)hite, blac(k), (c)lear, (b)lue, g(reen), (r)ed, (l)oad , (s)ave (q)uit, 1-9 for width")

    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    # Load image
    portrait = pygame.image.load("painting.bmp").convert
    
    load_save_image = False

    # L - Loop
    while keepGoing:

        # T - Timer to set frame rate
        clock.tick(120) # 120 fps cause my computer has a 120hz display.

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                # Check if a left mouse button is down
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                    lineStart = lineEnd

            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    # quit
                    keepGoing = False
                elif event.key == pygame.K_c:
                    # clear screen
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    # white
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    # black
                    drawColor = (0, 0, 0)
                
                elif event.key == pygame.K_r:
                    # red
                    drawColor = (255, 0, 0)

                elif event.key == pygame.K_g:
                    # green
                    drawColor = (0, 255, 0)

                elif event.key == pygame.K_b:
                    # blue
                    drawColor = (0, 0, 255)

                elif event.key == pygame.K_s:
                    pygame.image.save(background, "painting.bmp")

                elif event.key == pygame.K_l:
                    # Load image
                    portrait = pygame.image.load("painting.bmp").convert()
                    load_save_image = not load_save_image

                elif event.key >= 49 and event.key <= 57:
                    # Set line width of event.key 50 to 57.
                    lineWidth = event.key - 48


        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (300, 450))

        if load_save_image == True:
            screen.blit(portrait, (0, 0))

        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()
