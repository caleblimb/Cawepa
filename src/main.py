#pylint: disable=F0401
#pylint: disable=R0912
#pylint: disable=R0915
'''
Execute this file to run the game. This file is where all of the code for the project is called.
'''
# Import Pygame
import pygame
#from pygame.locals import *

# Import local modules
from game import game
from level.levels.level1 import Level1
from menu.main_menu import MainMenu
from menu.online_menu import OnlineMenu
from menu.credits_menu import CreditsMenu
from menu.options_menu import OptionsMenu

# Initialize pygame module
pygame.init()

####################################################################################################
# Update function called 60 times a second
####################################################################################################
def update(level):
    ''' This updates the level and other top-level aspects of the game.
    Things like the player and mobs are updated within the level, not here. '''
    level.update()

####################################################################################################
# Reder everything to screen
####################################################################################################
def draw(screen, level):
    ''' This draws everything '''
    # Clear Screen
    screen.fill((150, 100, 150))
    level.draw(screen)
    screen.blit(game.MOUSE_CURSOR, (game.MOUSE_X, game.MOUSE_Y))
    pygame.display.update()

####################################################################################################
# Game Loop - Program execution starts here
####################################################################################################
def main():
    ''' This function sets up the window and runs the game loop '''
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

    # Set Mouse Properties
    game.MOUSE_CURSOR = game.CURSOR_ARROW
    pygame.mouse.set_visible(False)

    # Set which level to start the game on, we'll change this to a menu screen later.
    game.MAIN_MENU = MainMenu()
    current_level = game.MAIN_MENU

    # Game Loop
    while running:
        # Loop through Pygame Events
        for event in pygame.event.get():
            # Check if running
            if event.type == pygame.QUIT:
                running = False
            # Check if keys are pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.INPUT_UP = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.INPUT_RIGHT = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.INPUT_DOWN = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.INPUT_LEFT = True

            # Check if keys are released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.INPUT_UP = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.INPUT_RIGHT = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.INPUT_DOWN= False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.INPUT_LEFT = False

            # Check if Mouse Buttons are pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    game.MOUSE_LEFT = True
                if event.button == pygame.BUTTON_RIGHT:
                    game.MOUSE_RIGHT = True

            # Check if Mouse Buttons are released
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    game.MOUSE_LEFT = False
                if event.button == pygame.BUTTON_RIGHT:
                    game.MOUSE_RIGHT = True

        # Update the current level
        mouse_pos = pygame.mouse.get_pos()
        game.MOUSE_X = mouse_pos[0]
        game.MOUSE_Y = mouse_pos[1]

        # Check Level and update it if needed
        if game.CHANGE_LEVEL:
            if game.CHANGE_LEVEL == "LEVEL_TEST":
                current_level = Level1()
            if game.CHANGE_LEVEL == "MENU_MAIN":
                current_level = MainMenu()
            if game.CHANGE_LEVEL == "MENU_ONLINE":
                current_level = OnlineMenu()
            if game.CHANGE_LEVEL == "MENU_OPTIONS":
                current_level = OptionsMenu()
            if game.CHANGE_LEVEL == "MENU_CREDITS":
                current_level = CreditsMenu()

            # Reset the change level request variable
            game.CHANGE_LEVEL = None

        # Update the current level
        # When online play is added this will update more than just the current level
        update(current_level)

        # Draw the current level to Screen
        # This will only ever draw the current level
        draw(screen, current_level)

        #Pygame - 60 updates/ticks per second
        clock.tick(60)

if __name__ == "__main__":
    main()
