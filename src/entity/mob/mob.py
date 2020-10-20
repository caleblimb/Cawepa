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
    # Update Mob
    ################################################################################################
    def update(self):
        pass
