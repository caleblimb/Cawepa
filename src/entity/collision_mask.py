#pylint: disable=F0401
'''
This handles collision masks
'''

class CollisionMask():
    ''' This is a rectangle used for collision detection. '''

    # Top left corner of rectangle
    x = 0
    y = 0

    # Dimensions of rectangle
    width = 0
    height = 0

    # Where should the top-left corner of the collision mask be relative to the entities x and y
    x_offset = 0
    y_offset = 0

    def __init__(self, width, height, x_offset, y_offset):
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset

    def update(self, x, y):
        '''Updates the location of the colision mask to follow the entity.'''
        self.x = x + self.x_offset
        self.y = y + self.y_offset
