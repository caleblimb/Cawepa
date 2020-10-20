#pylint: disable=F0401
'''
This hadles everything that all entities have in common.
'''

class Entity():
    x = 0
    y = 0
    sprite = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    ################################################################################################
    # Update Entity
    ################################################################################################
    def update(self):
        '''
        This method is necessary as a placeholder for child classes
        '''

    ################################################################################################
    # Draw Entity
    ################################################################################################
    def draw(self, screen, x_offset, y_offset):
        '''
        Draws the sprite to the screen. x_offset and y_offset refer to the camera position.
        '''
        self.sprite.draw(screen, self.x - x_offset, self.y - y_offset)
