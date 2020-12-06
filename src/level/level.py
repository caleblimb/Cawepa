#pylint: disable=F0401
'''
This file handles the code for managing a level
It doesn not contain any level-specific data
'''
from game import game
class Level():
    ''' This class defines the universal function of all levels, including menus '''
    #Define camera offset
    x_scroll = 0
    y_scroll = 0

    #Define entities list
    entities = []

    ################################################################################################
    # Initialize Level
    ################################################################################################
    def __init__(self):
        self.entities = []

    ################################################################################################
    # Update Level
    ################################################################################################
    def update(self):
        ''' This loops through every element of the level and calls it's update function. '''
        for entity in self.entities:
            if - 100 < entity.y - self.y_scroll < game.SCREEN_HEIGHT + 100 and - 100 < entity.x - self.x_scroll < game.SCREEN_WIDTH + 100:
                entity.update()

    ################################################################################################
    # Render Level
    ################################################################################################
    def draw(self, screen):
        pass
