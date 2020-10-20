#pylint: disable=F0401
'''
This hadles the user controlled Player
'''
from enum import Enum
import pygame
from game import game
from game.sprite import SpriteSheet, Sprite
from .mob import Mob
from ..collision_mask import CollisionMask

class Player(Mob):
    ''' Defines universal characteristics for all Mobs ie Players, Monsters, NPCs... '''
    class Direction(Enum):
        ''' Direction player is facing '''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

    # Arrays of sprites for animations
    sprite_up = []
    sprite_right = []
    sprite_down = []
    sprite_left = []

    # Current Frame
    frame = 0.0

    # Number of frames
    frame_count = 8

    # Starting direction
    direction = Direction.DOWN

    def __init__(self, x, y):
        super().__init__(x, y)

        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/player.png")

        # Add each direction of the walking animation
        for frame in range (0, self.frame_count):
            self.sprite_up   .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 0, 32, 32), 32, 32))
            self.sprite_right.append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 1, 32, 32), 32, 32))
            self.sprite_down .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 2, 32, 32), 32, 32))
            self.sprite_left .append(Sprite(sprite_sheet.get_image(32 * frame, 32 * 3, 32, 32), 32, 32))

        # Starting Sprite
        self.sprite = self.sprite_down[0]

        # Define collision mask
        self.collision_mask = CollisionMask(12, 12, -6, -6)

        # Place (x, y) origin in the center of where the feet are.
        self.sprite_x_offset = 16
        self.sprite_y_offset = 25

    def update(self, tile_map, tiles, width, height):
        self.collision_mask.update(self.x, self.y)
        update_frame = False
        player_speed = 2

        # Ammount to move
        xa = 0
        ya = 0

        # Check for player input to move the player
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
        self.move(tile_map, tiles, width, height, xa, ya)

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
