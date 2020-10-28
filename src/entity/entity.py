#pylint: disable=F0401
'''
This hadles everything that all entities have in common.
'''

class Entity():
    x = 0
    y = 0
    sprite = None
    sprite_x_offset = 0
    sprite_y_offset = 0
    collision_mask = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    ################################################################################################
    # Update Entity
    ################################################################################################
    def update(self, tile_map, x_offset, y_offset):
        ''' This method is necessary as a placeholder for child classes '''

    ################################################################################################
    # Draw Entity
    ################################################################################################
    def draw(self, screen, x_offset, y_offset):
        ''' Draws the sprite to the screen. x_offset and y_offset refer to the camera position. '''
        self.sprite.draw(screen, \
                         self.x - self.sprite_x_offset - x_offset, \
                         self.y - self.sprite_y_offset - y_offset)
