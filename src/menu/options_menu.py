#pylint: disable=F0401
'''
This will contain global options such as sound/music levels.
'''
import pygame
from game import game
from game.sprite import SpriteSheet

from menu.menu import Menu
from .component.button import Button
from .component.label import Label

####################################################################################################
# Options Menu
####################################################################################################
class OptionsMenu(Menu):
    '''
    Menu for game options
    '''
    def __init__(self):
        super().__init__("Options", True)

        # Vertical center of screen
        y = game.SCREEN_HEIGHT / 2

        # Placeholder for option components
        self.info = [ \
            Label(0, y - 30, game.SCREEN_WIDTH, 20, 24, "Options"), \
            Label(0, y - 10, game.SCREEN_WIDTH, 20, 24, "to be put"), \
            Label(0, y + 10, game.SCREEN_WIDTH, 20, 24, "here") \
            ]

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        super().update()

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        super().draw(screen)
        for i in self.info:
            i.draw(screen)
