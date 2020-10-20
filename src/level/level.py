#pylint: disable=F0401
'''
This file handles the code for managing a level
It doesn not contain any level-specific data
'''
from game import game

class Level():
    '''
    This class defines the universal function of all levels, including menus
    '''
    #Define camera offset
    x_scroll = 0
    y_scroll = 0

    #Define entities list
    entities = []

    ################################################################################################
    # Initialize Level
    ################################################################################################
    def __init__(self):
        pass

    ################################################################################################
    # Update Level
    ################################################################################################
    def update(self):
        '''
        This loops through every element of the level and calls it's update function.
        '''
        if game.INPUT_UP:
            self.y_scroll -= 10
        if game.INPUT_RIGHT:
            self.x_scroll += 10
        if game.INPUT_DOWN:
            self.y_scroll += 10
        if game.INPUT_LEFT:
            self.x_scroll -= 10

        for entity in self.entities:
            entity.update()

    ################################################################################################
    # Render Level
    ################################################################################################
    def draw(self, screen):
        '''
        This loops through every element of the level and calls it's draw function.
        '''
        for entity in self.entities:
            entity.draw(screen)
