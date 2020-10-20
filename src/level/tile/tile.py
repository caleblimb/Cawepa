#pylint: disable=F0401
'''
This is the template for a type of file
'''

class Tile():
    sprite = None
    solid = False

    ################################################################################################
    # Define Tile
    ################################################################################################
    def __init__(self, sprite):
        self.sprite = sprite

    def load_tiles(self, file_name):
        pass
    