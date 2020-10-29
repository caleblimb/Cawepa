#pylint: disable=F0401
'''
This is the Online Menu and will be used to set up online games
(probably only LAN considering the time we have).
'''
from game import game

from .menu import Menu
from .component.button import Button
from .component.label import Label

####################################################################################################
# Online Play Menu
####################################################################################################
class LoadMenu(Menu):
    ''' Define the characteristics of the options menu '''
    def __init__(self):
        super().__init__("Load Game", True)

        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT / 2 - 9

        self.button_load = Button(x, y, self.button_width, self.button_height, \
                                  self.sprite_button_idle, \
                                  self.sprite_button_hover, \
                                  self.sprite_button_press)

        self.label_load = Label(x, y, self.button_width, self.button_height, 14, \
                                       "Load Game")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        super().update()
        self.button_load.update()

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        super().draw(screen)
        self.button_load.draw(screen)
        self.label_load.draw(screen)
