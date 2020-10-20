#pylint: disable=F0401
'''
This handles everything that every creature has in common including the player
'''
from ..entity import Entity

class Mob(Entity):
    '''
    Defines universal characteristics for all Mobs ie Players, Monsters, NPCs...
    '''
    # This defines how deep the Mob is and aids with drawing underwater and such.
    tred = 0

    def __init__(self, x, y):
        super().__init__(x, y)

    ################################################################################################
    # Move Mob to new position
    ################################################################################################
    def move (self, tile_map, tiles, width, height, xa, ya):
        ''' This handles the movement of mobs. It handles each direction separately so that if
            it tries moving up against a wall, it can still slide along the surface instead of
            getting stuck. '''
        # Move one direction at a time
        if (xa != 0 and ya != 0):
            self.move(tile_map, tiles, width, height, xa, 0)
            self.move(tile_map, tiles, width, height, 0, ya)
            return

        # Move horizontally
        while xa != 0:
            self.collision_mask.update(self.x, self.y)
            if (abs(xa) > 1):
                if (not self.tile_collision(tile_map, tiles, width, height, self.one(xa), int(ya))):
                    self.x += self.one(xa)
                xa -= self.one(xa)
            else:
                if (not self.tile_collision(tile_map, tiles, width, height, self.one(xa), int(ya))):
                    self.x += xa
                xa = 0

        # Move vertically
        while ya != 0:
            self.collision_mask.update(self.x, self.y)
            if abs(ya) > 1:
                if not self.tile_collision(tile_map, tiles, width, height, int(xa), self.one(ya)):
                    self.y += self.one(ya)
                ya -= self.one(ya)
            else:
                if not self.tile_collision(tile_map, tiles, width, height, int(xa), self.one(ya)):
                    self.y += ya
                ya = 0

        self.tred = self.tile_depth(tile_map, tiles, width, height)

    ################################################################################################
    # Make value equal 1 or -1
    ################################################################################################
    def one(self, value):
        '''
        This function takes a number and returns 1 if positive and -1 if negative.
        It is used for the movement of mobs.
        '''
        if value < 0:
            return -1
        return 1

    ################################################################################################
    # Update Mob
    ################################################################################################
    def update(self, tile_map, tiles, width, height):
        pass

    ################################################################################################
    # Draw Mob
    ################################################################################################
    def draw(self, screen, x_offset, y_offset):
        if self.tred == 0:
            super().draw(screen, x_offset, y_offset)
        else:
            self.sprite.draw_sub(screen, \
                                 self.x - self.sprite_x_offset - x_offset, \
                                 self.y - self.sprite_y_offset - y_offset, \
                                 self.tred)
