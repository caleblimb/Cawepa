#pylint: disable=F0401
'''
This hadles the chicken
'''
from enum import Enum
import pygame
import math
import random
from game import game
from game.sprite import SpriteSheet, Sprite
from menu.hud import HUD
from ..mob import Mob
from ...collision_mask import CollisionMask
from ...projectile.fire_ball import Fireball


class Chicken(Mob):
    # Starting direction
    direction = Mob.Direction.DOWN

    def __init__(self, x, y):
        super().__init__(x, y)

        self.health = 10
        self.max_health = 10
        self.action_counter = 10
        self.state = 0
        self.xa = 0
        self.ya = 0

        self.sprite_up = []
        self.sprite_right = []
        self.sprite_down = []
        self.sprite_left = []

        self.frame_count = 8
        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/mobs/chicken_black.png")

        # Add each direction of the walking animation
        for frame in range (0, self.frame_count):
            self.sprite_left .append(Sprite( \
                sprite_sheet.get_image(13 * frame, 11 * 0, 13, 11), 13, 11))
            self.sprite_right.append(Sprite( \
                sprite_sheet.get_image(13 * frame, 11 * 1, 13, 11), 13, 11))
            self.sprite_down .append(Sprite( \
                sprite_sheet.get_image(13 * frame, 11 * 2, 13, 11), 13, 11))
            self.sprite_up   .append(Sprite( \
                sprite_sheet.get_image(13 * frame, 11 * 3, 11, 11), 13, 11))

        # Starting Sprite
        self.sprite = self.sprite_down[0]

        # Define collision mask
        self.collision_mask = CollisionMask(5, 9, -1, -5)

        # Place (x, y) origin in the center of where the feet are.
        self.sprite_x_offset = 6
        self.sprite_y_offset = 6

    def update(self, tile_map, x_offset, y_offset):

        self.action_counter -= 1

        if self.action_counter <= 0:
            self.action_counter = 100 + random.randint(0, 600)
            direction = random.uniform(-math.pi, math.pi)

        ## 0 = Idle, 1 = Eating, 2 = Walking, 3 = Running
            self.state = random.randint(0, 3)
            if self.state == 0 or self.state == 1:
                self.xa = 0
                self.ya = 0
            if self.state == 2:
                self.xa = 0.5 * math.cos(direction)
                self.ya = 0.5 * math.sin(direction)
            if self.state == 3:
                self.xa = math.cos(direction)
                self.ya = math.sin(direction)

        ## 0 = Idle, 1 = Eating, 2 = Walking, 3 = Running
        if self.state == 0:
            self.frame = 2

        if self.state == 1:
            self.frame = (self.action_counter // 10) % 2

        if self.state == 2:
            self.frame = 3 + (self.action_counter // 10) % 3

        if self.state == 3:
            self.frame = 3 + (self.action_counter // 5) % 3

        # Regenerate Health
        if self.health < self.max_health:
            self.health += 0.01

        # Update Collsiion Mask
        self.collision_mask.update(self.x, self.y)
        if self.xa != 0 and self.ya != 0:
            self.move(tile_map, self.xa, self.ya)

    def draw(self, screen, x_offset, y_offset):
        self.update_sprite_direction()
        super().draw(screen, x_offset, y_offset)
