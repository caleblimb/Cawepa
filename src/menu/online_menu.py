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
class OnlineMenu(Menu):
    ''' Define the characteristics of the options menu '''
    def __init__(self):
        super().__init__("Online Game", True)

        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT / 2 - 19

        self.button_host = Button(x, y, self.button_width, self.button_height, \
                                  self.sprite_button_idle, \
                                  self.sprite_button_hover, \
                                  self.sprite_button_press)

        self.button_host.label = Label(x, y, self.button_width, self.button_height, 14, \
                                       "Host LAN Game")

        y = game.SCREEN_HEIGHT / 2 + 1
        self.button_join = Button(x, y, self.button_width, self.button_height, \
                                  self.sprite_button_idle, \
                                  self.sprite_button_hover, \
                                  self.sprite_button_press)

        self.button_join.label = Label(x, y, self.button_width, self.button_height, 14, \
                                       "Join LAN Game")


    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        super().update()
        self.button_host.update()
        self.button_join.update()

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        super().draw(screen)
        self.button_host.draw(screen)
        self.button_join.draw(screen)
