"""
Pygame base template for opening a window
These three header elements must be present in any code you submit
"""
__author__ = "Julian Cochran"
__version__ = "12.13.2023"

import pygame

# Globals -- color definitions using RGB standards
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# start the Pygame engine
pygame.init()

# Set the width and height of the screen (width, height)
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50
# Speed and direction of rectangle, used for movement
# change these values to increase/decrease the speed of the rectangle
rect_change_x = 2
rect_change_y = 2

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    # Here, we clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    # --- Move the rect left or right based on rect_change_x and rect_change_y

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit, exits the program
pygame.quit()