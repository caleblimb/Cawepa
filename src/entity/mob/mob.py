#pylint: disable=F0401
'''
This handles everything that every creature has in common including the player
'''
from enum import Enum
from ..entity import Entity

class Mob(Entity):
    '''
    Defines universal characteristics for all Mobs ie Players, Monsters, NPCs...
    '''
    class Direction(Enum):
        ''' Direction player is facing '''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
    # This defines how deep the Mob is and aids with drawing underwater and such.
    tred = 0
    projectile = None
    direction = None

    # Current Frame
    frame = 0.0

    # Number of frames
    frame_count = 0

    sprite_up = []
    sprite_right = []
    sprite_down = []
    sprite_left = []

    def __init__(self, x, y):
        super().__init__(x, y)

    ################################################################################################
    # Move Mob to new position
    ################################################################################################
    def move (self, tile_map, xa, ya, update_direction = True):
        ''' This handles the movement of mobs. It handles each direction separately so that if
            it tries moving up against a wall, it can still slide along the surface instead of
            getting stuck. '''

        if update_direction and (xa !=0 or ya != 0):
            if abs(xa) > abs(ya):
                if xa > 0:
                    self.direction = Mob.Direction.RIGHT
                else:
                    self.direction = Mob.Direction.LEFT
            else:
                if ya >= 0:
                    self.direction = Mob.Direction.DOWN
                else:
                    self.direction = Mob.Direction.UP
            self.update_sprite_direction()

        # Move one direction at a time
        if (xa != 0 and ya != 0):
            self.move(tile_map, xa, 0, False)
            self.move(tile_map, 0, ya, False)
            return

        # Move horizontally
        while xa != 0:
            self.collision_mask.update(self.x, self.y)
            if (abs(xa) > 1):
                if (not tile_map.tile_collision(self.collision_mask, self.one(xa), int(ya))):
                    self.x += self.one(xa)
                xa -= self.one(xa)
            else:
                if (not tile_map.tile_collision(self.collision_mask, self.one(xa), int(ya))):
                    self.x += xa
                xa = 0

        # Move vertically
        while ya != 0:
            self.collision_mask.update(self.x, self.y)
            if abs(ya) > 1:
                if not tile_map.tile_collision(self.collision_mask, int(xa), self.one(ya)):
                    self.y += self.one(ya)
                ya -= self.one(ya)
            else:
                if not tile_map.tile_collision(self.collision_mask, int(xa), self.one(ya)):
                    self.y += ya
                ya = 0

        self.tred = tile_map.tile_depth(self.collision_mask)

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

    def update_sprite_direction(self):
        # Update sprite direction
        if self.direction == Mob.Direction.UP:
            self.sprite = self.sprite_up[int(self.frame)]
        if self.direction == Mob.Direction.RIGHT:
            self.sprite = self.sprite_right[int(self.frame)]
        if self.direction == Mob.Direction.DOWN:
            self.sprite = self.sprite_down[int(self.frame)]
        if self.direction == Mob.Direction.LEFT:
            self.sprite = self.sprite_left[int(self.frame)]
    ################################################################################################
    # Update Mob
    ################################################################################################
    def update(self, tile_map, x_offset, y_offset):
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
