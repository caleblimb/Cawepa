#pylint: disable=F0401
'''
Test Level
'''
import pygame
import random
from game.sprite import SpriteSheet
from entity.mob.player import Player
from entity.mob.fauna.chicken import Chicken
from ..tile.game_level import GameLevel
from ..tile.tile import Tile
from ..tile.tile import TileMap

class LevelCamp(GameLevel):
    '''
    Define Test Level
    '''
    def __init__(self):
        # Call Level constructor
        super().__init__()

        # Load tile_map from file
        self.tile_map = TileMap("res/levels/camp")

        # Define Starting Position for Camera
        self.x_scroll = 400
        self.y_scroll = 400

