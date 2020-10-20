#pylint: disable=F0401
'''
This hadles the user controlled Player
'''
from enum import Enum
import pygame
from game import game
from game.sprite import SpriteSheet, Sprite
from .mob import Mob

class Player(Mob):
    '''
    Defines universal characteristics for all Mobs ie Players, Monsters, NPCs...
    '''
    class Direction(Enum):
        '''
        Direction player is facing
        '''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    sprite_up = []
    sprite_right = []
    sprite_down = []
    sprite_left = []

    frame = 0.0
    frame_count = 8

    direction = Direction.DOWN

    def __init__(self, x, y):
        super().__init__(x, y)
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/player.png")

        for frame in range (0, self.frame_count):
            self.sprite_up   .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 0, 32, 32), 32, 32))
            self.sprite_right.append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 1, 32, 32), 32, 32))
            self.sprite_down .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 2, 32, 32), 32, 32))
            self.sprite_left .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 3, 32, 32), 32, 32))
        
        self.sprite = self.sprite_down[0]

    def update(self):
        update_frame = False
        player_speed = 2
        xa = 0
        ya = 0

        if game.INPUT_RIGHT:
            xa += player_speed
            self.direction = Player.Direction.RIGHT
            update_frame = True
        if game.INPUT_LEFT:
            xa -= player_speed
            self.direction = Player.Direction.LEFT
            update_frame = True
        if game.INPUT_UP:
            ya -= player_speed
            self.direction = Player.Direction.UP
            update_frame = True
        if game.INPUT_DOWN:
            ya += player_speed
            self.direction = Player.Direction.DOWN
            update_frame = True

        # Update player position
        self.x += xa
        self.y += ya

        if update_frame:
            # Update animation frame
            self.frame += player_speed / 4
            while self.frame >= self.frame_count:
                self.frame -= self.frame_count

            # Update player direction
            if self.direction == Player.Direction.UP:
                self.sprite = self.sprite_up[int(self.frame)]
            if self.direction == Player.Direction.RIGHT:
                self.sprite = self.sprite_right[int(self.frame)]
            if self.direction == Player.Direction.DOWN:
                self.sprite = self.sprite_down[int(self.frame)]
            if self.direction == Player.Direction.LEFT:
                self.sprite = self.sprite_left[int(self.frame)]
