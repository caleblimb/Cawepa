#pylint: disable=F0401
'''
Execute this file to run the game. This file is where all of the code for the project is called.
'''
# Import Pygame
import pygame
#from pygame.locals import *

# Import local modules
from game import game
from level.level import Level

# Initialize pygame module
pygame.init()

####################################################################################################
# Game Loop
####################################################################################################
def run():
    '''
    This function sets up the window and runs the game loop
    '''
    # Boolean for if the game is supposed to be running
    running = True

    # Initialize pygame clock
    clock = pygame.time.Clock()

    # Create game window
    screen = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT),\
         pygame.RESIZABLE | pygame.SCALED)

    # Set program name in title-bar
    pygame.display.set_caption("Cawepa")

    # Set icon in title-bar
    icon = pygame.image.load('res/graphics/icon.png')
    pygame.display.set_icon(icon)

    #testImg = pygame.image.load('assets/sprites/icon.png')

    current_level = Level()

    while running:
        # Loop through Pygame Events
        for event in pygame.event.get():
            # Check if running
            if event.type == pygame.QUIT:
                running = False
            # Check if keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.INPUT_UP = True
                if event.key == pygame.K_RIGHT:
                    game.INPUT_RIGHT = True
                if event.key == pygame.K_DOWN:
                    game.INPUT_DOWN = True
                if event.key == pygame.K_LEFT:
                    game.INPUT_LEFT = True

            # Check if keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    game.INPUT_UP = False
                if event.key == pygame.K_RIGHT:
                    game.INPUT_RIGHT = False
                if event.key == pygame.K_DOWN:
                    game.INPUT_DOWN= False
                if event.key == pygame.K_LEFT:
                    game.INPUT_LEFT = False

        # Update the current level
        update(current_level)

        # Draw the current level to Screen
        draw(screen, current_level)

        #Pygame - 60 updates/ticks per second
        clock.tick(60)

####################################################################################################
# Update function called 60 times a second
####################################################################################################
def update(level):
    '''
    This updates the level and other top-level aspects of the game.
    Things like the player and mobs are updated within the level, not here.
    '''
    level.update()

####################################################################################################
# Reder everything to screen
####################################################################################################
def draw(screen, level):
    '''
    This draws everything
    '''
    # Clear Screen
    screen.fill((0, 0, 0))
    level.draw(screen)
    pygame.display.update()

####################################################################################################
# Program execution starts here
####################################################################################################
def main():
    '''
    Starts the game, I might copy the code from run() and just put it here in the short future.
    '''
    run()

if __name__ == "__main__":
    main()
