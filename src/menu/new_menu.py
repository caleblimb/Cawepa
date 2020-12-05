#pylint: disable=F0401
'''
This is the Online Menu and will be used to set up online games
(probably only LAN considering the time we have).
'''
import pygame
from game import game
from game.sprite import SpriteSheet, Sprite
from entity.mob.player import Player
from .menu import Menu
from .component.button import Button
from .component.label import Label

####################################################################################################
# Online Play Menu
####################################################################################################
class NewMenu(Menu):
    ''' Define the characteristics of the options menu '''
    def __init__(self):
        super().__init__("New Game", True)

        self.player_choice = 0
        self.number_of_choices = 5

        self.label_player_choice = Label \
                (0, game.SCREEN_HEIGHT // 2 - 32, game.SCREEN_WIDTH, self.button_height, 28, "Character Select")

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/players.png")
        self.player_choice_sprite = []
        for i in range(self.number_of_choices):
            option = sprite_sheet.get_image(16 * 1, i * 48, 16, 16)
            scaled_option = pygame.transform.scale(option, (32, 32))
            self.player_choice_sprite.append(scaled_option)

        sprite_sheet = SpriteSheet("res/graphics/gui/menu_button_small.png")
        self.button_choose_width = 32
        self.button_choose_height = 16

        self.sprite_choose_button_idle = sprite_sheet.get_image( \
            0, 0, self.button_choose_width, self.button_choose_height)
        self.sprite_choose_button_hover = sprite_sheet.get_image( \
            0, self.button_choose_height, self.button_choose_width, self.button_choose_height)
        self.sprite_choose_button_press = sprite_sheet.get_image( \
            0, self.button_choose_height * 2, self.button_choose_width, self.button_choose_height)

        x = game.SCREEN_WIDTH / 2 - self.button_choose_width - 17
        y = game.SCREEN_HEIGHT / 2 + 10

        self.button_choose_left = Button(x, y, self.button_choose_width, \
                                        self.button_choose_height, \
                                        self.sprite_choose_button_idle, \
                                        self.sprite_choose_button_hover, \
                                        self.sprite_choose_button_press)
        self.label_choose_left = Label(x, y, self.button_choose_width, \
                                        self.button_choose_height, 14, "Prev")

        x = game.SCREEN_WIDTH / 2 + 17
        self.button_choose_right = Button(x, y, self.button_choose_width, \
                                        self.button_choose_height,\
                                        self.sprite_choose_button_idle, \
                                        self.sprite_choose_button_hover, \
                                        self.sprite_choose_button_press)
        self.label_choose_right = Label(x, y, self.button_choose_width, \
                                        self.button_choose_height, 14, "Next")

        x = game.SCREEN_WIDTH / 2 - 50
        y = game.SCREEN_HEIGHT / 2 + 42

        self.button_new = Button(x, y, self.button_width, self.button_height, \
                                  self.sprite_button_idle, \
                                  self.sprite_button_hover, \
                                  self.sprite_button_press)

        self.label_new = Label(x, y, self.button_width, self.button_height, 14, "Play")

    ################################################################################################
    # Update Menu
    ################################################################################################
    def update(self):
        ''' Update menu components '''
        super().update()
        self.button_choose_left.update()
        self.button_choose_right.update()
        self.button_new.update()

        if self.button_choose_left.action_event:
            if self.player_choice > 0:
                self.player_choice -= 1
            self.button_choose_left.reset_action_event()

        if self.button_choose_right.action_event:
            if self.player_choice < self.number_of_choices - 1:
                self.player_choice += 1
            self.button_choose_right.reset_action_event()

        print(self.player_choice)
        if self.button_new.action_event:
            game.PLAYER = Player(15 * 16 + 8, 48 * 16 + 8, self.player_choice)
            game.CHANGE_LEVEL = "LEVEL_CAMP"
            self.button_back.reset_action_event()

    ################################################################################################
    # Draw Menu
    ################################################################################################
    def draw(self, screen):
        ''' Draw menu components '''
        super().draw(screen)
        self.label_player_choice.draw(screen)
        # Draw Player Choice on screen
        screen.blit(self.player_choice_sprite[self.player_choice], \
                    (game.SCREEN_WIDTH // 2 - 16, game.SCREEN_HEIGHT // 2))

        self.button_choose_left.draw(screen)
        self.button_choose_right.draw(screen)
        self.label_choose_left.draw(screen)
        self.label_choose_right.draw(screen)

        self.button_new.draw(screen)
        self.label_new.draw(screen)
