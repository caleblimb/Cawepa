#pylint: disable=F0401
'''
Test Level
'''
import pygame
import random
from game import game
from game.sprite import SpriteSheet
from entity.mob.player import Player
from entity.mob.fauna.chicken import Chicken
from ..tile.game_level import GameLevel
from ..tile.tile import Tile
from ..tile.tile import TileMap

class LevelTown(GameLevel):
    '''
    Define Test Level
    '''
    def __init__(self):
        # Call Level constructor
        super().__init__()

        # Load tile_map from file
        self.tile_map = TileMap("res/levels/town")

        # Define Starting Position for Camera
        self.x_scroll = 400
        self.y_scroll = 400

        for _ in range(32):
            self.entities.append(Chicken(random.randint(0, self.tile_map.width * 16), random.randint(0, self.tile_map.height * 16)))

    def update(self):
        super().update()
        if game.PLAYER.x < 0:
            game.PLAYER.x = self.tile_map.width * 16 - 4
            game.CHANGE_LEVEL = "LEVEL_CAMP"
