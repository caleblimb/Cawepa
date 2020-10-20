#pylint: disable=F0401
'''
Test Level
'''
import pygame
from game.sprite import SpriteSheet
from entity.mob.player import Player
from ..tile.game_level import GameLevel
from ..tile.tile import Tile

class Level1(GameLevel):
    '''
    Define Test Level
    '''
    def __init__(self):
        #Call Level constructor
        super().__init__()

        self.tile_map = self.load_level("res/levels/test_level")

        tile_type_width = 5
        tile_type_height = 176
        pygame.sprite.Sprite.__init__(self)
        tile_sheet = SpriteSheet("res/graphics/basic_tiles.png")

        for y in range(0, tile_type_height):
            for x in range(0, tile_type_width):
                tile = Tile(tile_sheet.get_image(x * 16, y * 16, 16, 16))
                

                if y >= 141 and y < 152:
                    tile.depth = 4
                if y >= 152:
                    tile.solid = True


                self.tiles.append(tile)

        self.x_scroll = 400
        self.y_scroll = 400
        self.entities.append(Player(500, 500))
