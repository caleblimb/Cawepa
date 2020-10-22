#pylint: disable=F0401
'''
This is just a screen that shows the credits.
'''
from game import game

from menu.menu import Menu
from .component.label import Label

####################################################################################################
# Credits Menu
####################################################################################################
class CreditsMenu(Menu):
    ''' This is the Online Menu and will be used to set up online games
        (probably only LAN considering the time we have). '''
    def __init__(self):
        super().__init__("Credits", True)

        # Vertical center of screen
        y = game.SCREEN_HEIGHT / 2

        # Lines of text to be drawn
        self.info = [ \
            Label(0, y - 30, game.SCREEN_WIDTH, 20, 24, "Caleb Limb"), \
            Label(0, y - 10, game.SCREEN_WIDTH, 20, 24, "Wei Hsu"), \
            Label(0, y + 10, game.SCREEN_WIDTH, 20, 24, "Paulo Dallastra") \
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
