#pylint: disable=F0401
'''
This is the Online Menu and will be used to set up online games
(probably only LAN considering the time we have).
'''
import pygame
from game import game
from game.sprite import SpriteSheet

from level.level import Level
from .component.button import Button
from .component.label import Label

####################################################################################################
# Online Play Menu
####################################################################################################
class OnlineMenu(Level):
    ''' Define the characteristics of the options menu '''
    def __init__(self):
        # Create Button spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/gui/menu_button.png")
        sprite_button_idle = sprite_sheet.get_image(0, 0, 100, 18)
        sprite_button_hover = sprite_sheet.get_image(0, 18, 100, 18)
        sprite_button_press = sprite_sheet.get_image(0, 36, 100, 18)

        self.title = Label(0, 0, game.SCREEN_WIDTH, 100, 56, "Online Game")

        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT / 2 - 19
        width = 100
        height = 18
        self.button_host = Button(x, y, width, height, \
                           sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_host.label = Label(x, y, width, height, 14, "Host LAN Game")

        y = game.SCREEN_HEIGHT / 2 +1
        self.button_join = Button(x, y, width, height, \
                           sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_join.label = Label(x, y, width, height, 14, "Join LAN Game")

        y = game.SCREEN_HEIGHT - 32
        self.button_back = Button(x, y, width, height, \
                           sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_back.label = Label(x, y, width, height, 14, "BACK")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        self.button_host.update()
        self.button_join.update()
        self.button_back.update()
        if self.button_back.action_event > 0:
            game.CHANGE_LEVEL = "MENU_MAIN"
            self.button_back.action_event -= 1

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        self.title.draw(screen)
        self.button_host.draw(screen)
        self.button_join.draw(screen)
        self.button_back.draw(screen)
