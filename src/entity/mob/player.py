#pylint: disable=F0401
'''
This hadles the user controlled Player
'''
from enum import Enum
import pygame
import math
from game import game
from game.sprite import SpriteSheet, Sprite
from menu.hud import HUD
from .mob import Mob
from ..collision_mask import CollisionMask
from ..projectile.fire_ball import Fireball


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

        # Create HUD
        self.hud = HUD()

        # Set max levels
        self.max_health = 100.0
        self.max_stamina = 100.0
        self.max_mana = 100.0

        # Set levels
        self.health = 100.0
        self.stamina = 100.0
        self.mana = 100.0

        # Spell Cooldown
        self.cooldown = 60

        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/player.png")

        # Add each direction of the walking animation
        for frame in range (0, self.frame_count):
            self.sprite_up   .append(Sprite( \
                sprite_sheet.get_image(32 * frame, 32 * 0, 32, 32), 32, 32))
            self.sprite_right.append(Sprite( \
                sprite_sheet.get_image(32 * frame, 32 * 1, 32, 32), 32, 32))
            self.sprite_down .append(Sprite( \
                sprite_sheet.get_image(32 * frame, 32 * 2, 32, 32), 32, 32))
            self.sprite_left .append(Sprite( \
                sprite_sheet.get_image(32 * frame, 32 * 3, 32, 32), 32, 32))

        # Starting Sprite
        self.sprite = self.sprite_down[0]

        # Define collision mask
        self.collision_mask = CollisionMask(12, 12, -6, -6)

        # Place (x, y) origin in the center of where the feet are.
        self.sprite_x_offset = 16
        self.sprite_y_offset = 25

    def update(self, tile_map, x_offset, y_offset):
        self.hud.health = (self.health * 100) // self.max_health
        self.hud.stamina = (self.stamina * 100) // self.max_stamina
        self.hud.mana = (self.mana * 100) // self.max_mana

        mouse_direction = math.atan2(game.MOUSE_X - (self.x - x_offset), game.MOUSE_Y - (self.y - y_offset))

        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown <= 0:
            if game.MOUSE_LEFT and self.mana >= 10:
                self.projectile = Fireball(self.x, self.y, 2 * math.sin(mouse_direction), 2 * math.cos(mouse_direction))
                self.cooldown = 60
                self.mana -= 10

        self.collision_mask.update(self.x, self.y)
        self.check_movement(tile_map)

        if self.stamina < self.max_stamina:
            self.stamina += 0.01
        if self.health < self.max_health:
            self.health += 0.01
        if self.mana < self.max_mana:
            self.mana += 0.01

    def check_movement(self, tile_map):
        update_frame = False

        player_speed = 1
        movement_cost = 0.01
        if game.INPUT_SHIFT and self.stamina > 4:
            player_speed = 2
            movement_cost = 0.02

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
        self.move(tile_map, xa, ya)
        self.stamina -= (abs(xa) + abs(ya)) * movement_cost

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



    def draw(self, screen, x_offset, y_offset):
        super().draw(screen, x_offset, y_offset)
        self.hud.draw(screen)
