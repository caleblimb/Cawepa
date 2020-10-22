#pylint: disable=F0401
'''
This if for the universal attributes of all projectiles.
'''
import math
from ..entity import Entity

class Projectile(Entity):
    def __init__(self, x, y, xa, ya):
        super().__init__(x, y)

        self.xa = xa
        self.ya = ya
        self.direction = math.atan2(xa, ya) * 18 * math.pi - 90

    def update(self, tile_map, tiles, width, height, x_offset, y_offset):
        self.x += self.xa
        self.y += self.ya

    def draw(self, screen, x_offset, y_offset):
        super().draw(screen, x_offset, y_offset)
