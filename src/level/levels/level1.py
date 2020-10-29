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

class Level1(GameLevel):
    '''
    Define Test Level
    '''
    def __init__(self):
        # Call Level constructor
        super().__init__()

        # Load tile_map from file
        self.tile_map = TileMap("res/levels/test_level")

        # Define Starting Position for Camera
        self.x_scroll = 400
        self.y_scroll = 400

        for _ in range(100):
            self.entities.append(Chicken(random.randint(30 * 16, 98 * 16), random.randint(30 * 16, 98 * 16)))
