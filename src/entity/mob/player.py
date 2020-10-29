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

    # Number of frames

    # Starting direction
    direction = Direction.DOWN

    def __init__(self, x, y, num_choice):
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

        self.frame_count = 4

        self.sprite_up = []
        self.sprite_right = []
        self.sprite_down = []
        self.sprite_left = []

        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/players.png")

        # There are 5 options here
        num_choice = num_choice % 5
        # Add each direction of the walking animation
        for frame in range (2):
            # Left
            self.sprite_left .append(Sprite(sprite_sheet.get_image \
                (16 * 0, 16 * 0 + (48 * num_choice), 16, 16), 16, 16))
            self.sprite_left .append(Sprite(sprite_sheet.get_image \
                (16 * 0, 16 * (1 + frame) + (48 * num_choice), 16, 16), 16, 16))
            
            # Down
            self.sprite_down .append(Sprite(sprite_sheet.get_image \
                (16 * 1, 16 * 0 + (48 * num_choice), 16, 16), 16, 16))
            self.sprite_down .append(Sprite(sprite_sheet.get_image \
                (16 * 1, 16 * (1 + frame) + (48 * num_choice), 16, 16), 16, 16))
            
            # Up
            self.sprite_up   .append(Sprite(sprite_sheet.get_image \
                (16 * 2, 16 * 0 + (48 * num_choice), 16, 16), 16, 16))
            self.sprite_up   .append(Sprite(sprite_sheet.get_image \
                (16 * 2, 16 * (1 + frame) + (48 * num_choice), 16, 16), 16, 16))
            
            # Right
            self.sprite_right.append(Sprite(sprite_sheet.get_image \
                (16 * 3, 16 * 0 + (48 * num_choice), 16, 16), 16, 16))
            self.sprite_right.append(Sprite(sprite_sheet.get_image \
                (16 * 3, 16 * (1 + frame) + (48 * num_choice), 16, 16), 16, 16))

        # Starting Sprite
        self.sprite = self.sprite_down[0]

        # Define collision mask
        self.collision_mask = CollisionMask(9, 9, 5, 4)

        # Place (x, y) origin in the center of where the feet are.
        self.sprite_x_offset = 8
        self.sprite_y_offset = 10

    def update(self, tile_map, x_offset, y_offset):
        self.hud.health = (self.health * 100) // self.max_health
        self.hud.stamina = (self.stamina * 100) // self.max_stamina
        self.hud.mana = (self.mana * 100) // self.max_mana

        # Mouse direction is tha angle of the line from the player to the cursor
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
            update_frame = True
        if game.INPUT_LEFT:
            xa -= player_speed
            update_frame = True
        if game.INPUT_UP:
            ya -= player_speed
            update_frame = True
        if game.INPUT_DOWN:
            ya += player_speed
            update_frame = True

        # Update player position
        self.move(tile_map, xa, ya)
        self.stamina -= (abs(xa) + abs(ya)) * movement_cost

        if update_frame:
            # Update animation frame
            self.frame += player_speed / 6
            while self.frame >= self.frame_count:
                self.frame -= self.frame_count

    def draw(self, screen, x_offset, y_offset):
        super().draw(screen, x_offset, y_offset)
