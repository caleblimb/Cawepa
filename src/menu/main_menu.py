#pylint: disable=F0401
'''
This is the Main Menu and is the first screen seen when the game is launched.
'''
from game import game

from menu.menu import Menu
from .component.button import Button
from .component.label import Label

####################################################################################################
# Main Menu
####################################################################################################
class MainMenu(Menu):
    ''' Define the characteristics of the main menu '''
    def __init__(self):
        super().__init__("Cawepa", False)

        # Position for buttons in center of screen
        x = game.SCREEN_WIDTH / 2 - 50

        # Play a single player game
        y = game.SCREEN_HEIGHT / 2 - 40
        self.button_single_player = Button(x, y, self.button_width, self.button_height, \
                                           self.sprite_button_idle, \
                                           self.sprite_button_hover, \
                                           self.sprite_button_press)

        self.button_single_player.label = Label(x, y, self.button_width, self.button_height, 14, \
                                                "Single Player")

        # Play an online game
        y = game.SCREEN_HEIGHT / 2 - 19
        self.button_online = Button(x, y, self.button_width, self.button_height, \
                                    self.sprite_button_idle, \
                                    self.sprite_button_hover, \
                                    self.sprite_button_press)
        self.button_online.label = Label(x, y, self.button_width, self.button_height, 14, \
                                         "Play Online")
        
        # Go to options menu
        y = game.SCREEN_HEIGHT / 2 + 1
        self.button_options = Button(x, y, self.button_width, self.button_height, \
                                     self.sprite_button_idle, \
                                     self.sprite_button_hover, \
                                     self.sprite_button_press)
        self.button_options.label = Label(x, y, self.button_width, self.button_height, 14, \
                                          "Options")

        # Creddits button
        y = game.SCREEN_HEIGHT / 2 + 22
        self.button_credits = Button(x, y, self.button_width, self.button_height, \
                                     self.sprite_button_idle, \
                                     self.sprite_button_hover, \
                                     self.sprite_button_press)

        self.button_credits.label = Label(x, y, self.button_width, self.button_height, 14, \
                                          "Credits")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        super().update()
        # Start Single-Player Game
        self.button_single_player.update()
        if self.button_single_player.action_event > 0:
            game.CHANGE_LEVEL = "LEVEL_TEST"
            self.button_single_player.action_event -= 1

        # Go to Online Menu
        self.button_online.update()
        if self.button_online.action_event > 0:
            game.CHANGE_LEVEL = "MENU_ONLINE"
            self.button_online.action_event -= 1

        # Go to Options Menu
        self.button_options.update()
        if self.button_options.action_event > 0:
            game.CHANGE_LEVEL = "MENU_OPTIONS"
            self.button_options.action_event -= 1

        # Go to Credits
        self.button_credits.update()
        if self.button_credits.action_event > 0:
            game.CHANGE_LEVEL = "MENU_CREDITS"
            self.button_credits.action_event -= 1

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        super().draw(screen)
        self.button_single_player.draw(screen)
        self.button_online.draw(screen)
        self.button_options.draw(screen)
        self.button_credits.draw(screen)
