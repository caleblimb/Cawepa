#pylint: disable=F0401
'''
This is the Main Menu and is the first screen seen when the game is launched.
'''
import pygame
from game import game
from game.sprite import SpriteSheet

from level.level import Level
from .component.button import Button
from .component.label import Label

####################################################################################################
# Main Menu
####################################################################################################
class MainMenu(Level):
    ''' Define the characteristics of the main menu '''
    def __init__(self):
        # Create Button spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/gui/menu_button.png")
        sprite_button_idle = sprite_sheet.get_image(0, 0, 100, 18)
        sprite_button_hover = sprite_sheet.get_image(0, 18, 100, 18)
        sprite_button_press = sprite_sheet.get_image(0, 36, 100, 18)

        # Menu title
        self.title = Label(0, 0, game.SCREEN_WIDTH, 100, 64, "Cawepa")

        # Position for buttons in center of screen
        x = game.SCREEN_WIDTH / 2 - 50

        # Size of buttons
        width = 100
        height = 18

        # Play a single player game
        y = game.SCREEN_HEIGHT / 2 - 40
        self.button_single_player = Button(x, y, width, height, \
                                    sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_single_player.label = Label(x, y, width, height, 14, "Single Player")

        # Play an online game
        y = game.SCREEN_HEIGHT / 2 - 19
        self.button_online = Button(x, y, width, height, \
                             sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_online.label = Label(x, y, width, height, 14, "Play Online")
        
        # Go to options menu
        y = game.SCREEN_HEIGHT / 2 + 1
        self.button_options = Button(x, y, width, height, \
                              sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_options.label = Label(x, y, width, height, 14, "Options")

        # Creddits button
        y = game.SCREEN_HEIGHT / 2 + 22
        self.button_credits = Button(x, y, width, height, \
                              sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_credits.label = Label(x, y, width, height, 14, "Credits")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
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
        self.title.draw(screen)
        self.button_single_player.draw(screen)
        self.button_online.draw(screen)
        self.button_options.draw(screen)
        self.button_credits.draw(screen)
