import pygame
from game import game
from game.sprite import SpriteSheet, Sprite

from level.level import Level
from .component.button import Button
from .component.label import Label

class OptionsMenu(Level):
    '''
    This is the Online Menu and will be used to set up online games (probably only LAN considering the time we have).
    '''
    def __init__(self):
        # Create Button spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/gui/menu_button.png")
        sprite_button_idle = sprite_sheet.get_image(0, 0, 100, 18)
        sprite_button_hover = sprite_sheet.get_image(0, 18, 100, 18)
        sprite_button_press = sprite_sheet.get_image(0, 36, 100, 18)

        self.title = Label(0, 0, game.SCREEN_WIDTH, 100, 56, "Options")

        y = game.SCREEN_HEIGHT / 2

        self.info = [ \
            Label(0, y - 30, game.SCREEN_WIDTH, 20, 24, "Options"), \
            Label(0, y - 10, game.SCREEN_WIDTH, 20, 24, "to be put"), \
            Label(0, y + 10, game.SCREEN_WIDTH, 20, 24, "here") \
            ]

        width = 100
        height = 18
        
        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT - 32
        self.button_back = Button(x, y, width, height, sprite_button_idle, sprite_button_hover, sprite_button_press)
        self.button_back.label = Label(x, y, width, height, 14, "BACK")

    def update(self):
        self.button_back.update()
        if self.button_back.action_event > 0:
            game.CHANGE_LEVEL = "MENU_MAIN"
            self.button_back.action_event -= 1

    def draw(self, screen):
        self.title.draw(screen)
        for i in self.info:
            i.draw(screen)
        self.button_back.draw(screen)
