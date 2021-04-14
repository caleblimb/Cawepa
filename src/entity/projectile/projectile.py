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
        self.direction = math.atan2(xa, ya) * (180 / math.pi) - 90
        self.exploded = False

    def update(self, tile_map, x_offset, y_offset):
        if not self.exploded:
            self.x += self.xa
            self.y += self.ya

    def draw(self, screen, x_offset, y_offset):
        if not self.exploded:
            super().draw(screen, x_offset, y_offset)
