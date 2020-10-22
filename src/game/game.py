'''
These are values that can be accesded by anywhere in the code.
'''
import pygame

#Global Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

#Input Values
INPUT_LEFT = False
INPUT_RIGHT = False
INPUT_UP = False
INPUT_DOWN = False

# Current Level
MAIN_MENU = None
TEST_LEVEL = None

# This is used by menues to request a level change from the game loop
CHANGE_LEVEL = None

#Mouse properties
CURSOR_ARROW = pygame.image.load('res/graphics/gui/cursor.png')
MOUSE_CURSOR = None

MOUSE_LEFT = False
MOUSE_RIGHT = False

MOUSE_X = 0
MOUSE_Y = 0
