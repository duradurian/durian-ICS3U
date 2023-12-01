"""
Add the following features to this paint program:
b. Add events for the keys '1' through '9' such that they set the line width to that many pixels.
c. Add an event for the 's' (save) key that will cause the current picture to be held in the current
directory with the filename painting.bmp.
d. Add an event for the 'l' (load) key that will cause the painting.bmp file to be loaded and
displayed in the window.
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
    pygame.display.set_caption("Paint: (w)hite, blac(k), (c)lear, (q)uit")

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

    # L - Loop
    while keepGoing:
        # T - Timer to set frame rate
        clock.tick(30)

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


        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (450, 450))
        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()
