#pylint: disable=F0401
'''
This handles collision masks
'''

class CollisionMask():
    x = 0
    y = 0
    width = 0
    height = 0
    x_offset = 0
    y_offset = 0

    def __init__(self, width, height, x_offset, y_offset):
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset

    def update(self, x, y):
        self.x = x + self.x_offset
        self.y = y + self.y_offset
