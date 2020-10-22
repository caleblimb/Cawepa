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
class Menu(Level):
    ''' Define the characteristics of the main menu '''
    def __init__(self, title, main_menu_button):
        self.main_menu_button = main_menu_button

        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load("res/graphics/gui/menu_background.png")

        # Create Button spritesheet
        sprite_sheet = SpriteSheet("res/graphics/gui/menu_button.png")
        self.sprite_button_idle = sprite_sheet.get_image(0, 0, 100, 18)
        self.sprite_button_hover = sprite_sheet.get_image(0, 18, 100, 18)
        self.sprite_button_press = sprite_sheet.get_image(0, 36, 100, 18)

        # Menu title
        self.title = Label(0, 0, game.SCREEN_WIDTH, 100, 64, title)

        # Size of buttons
        self.button_width = 100
        self.button_height = 18

        # Back button
        # Location of back button
        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT - 32
        self.button_back = Button(x, y, self.button_width, self.button_height, \
                                  self.sprite_button_idle, \
                                  self.sprite_button_hover, \
                                  self.sprite_button_press)

        if main_menu_button:
            self.button_back.label = Label(x, y, self.button_width, self.button_height, 14, "BACK")
        else:
            self.button_back.label = Label(x, y, self.button_width, self.button_height, 14, "QUIT")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        self.button_back.update()
        if self.button_back.action_event > 0:
            if self.main_menu_button:
                game.CHANGE_LEVEL = "MENU_MAIN"
            else:
                game.CHANGE_LEVEL = "QUIT"

            self.button_back.action_event -= 1

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        screen.blit(self.background, (0, 0))
        self.title.draw(screen)
        self.button_back.draw(screen)
