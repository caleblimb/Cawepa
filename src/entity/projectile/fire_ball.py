#pylint: disable=F0401
'''
This if for the universal attributes of all projectiles.
'''
import pygame
from game.sprite import SpriteSheet, Sprite
from .projectile import Projectile

class Fireball(Projectile):
    def __init__(self, x, y, xa, ya):
        super().__init__(x, y, xa, ya)

        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/projectiles/fireball.png")

        self.sprite_frame = [Sprite(sprite_sheet.get_image(0, 0, 10, 5), 10, 10), Sprite(sprite_sheet.get_image(0, 5, 10, 5), 10, 10)]
        self.sprite_x_offset = 5
        self.sprite_y_offset = 5

        self.sprite_frame[0].rot_center(self.direction)
        self.sprite_frame[1].rot_center(self.direction)

        self.sprite = self.sprite_frame[0]
        
        self.animation_frames = 2
        self.current_frame = 0
        self.animation_delay = 10

    def update(self, tile_map, x_offset, y_offset):
        super().update(tile_map, x_offset, y_offset)
        self.animation_delay -= 1
        if self.animation_delay <= 0:
            self.animation_delay = 2
            self.current_frame += 1
            self.sprite = self.sprite_frame[self.current_frame % self.animation_frames]

    def draw(self, screen, x_offset, y_offset):
        super().draw(screen, x_offset, y_offset)
