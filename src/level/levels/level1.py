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
        # Call Level constructor
        super().__init__()

        # Load tile_map from file
        self.tile_map = self.load_level("res/levels/test_level.csv")

        # Define dimenstions of tile spritesheet according to how many tiles it has
        tile_type_width = 5
        tile_type_height = 176

        # Create tile spritesheet
        pygame.sprite.Sprite.__init__(self)
        tile_sheet = SpriteSheet("res/graphics/basic_tiles.png")

        # Add all tiles from tile spritesheet to tile types
        for y in range(0, tile_type_height):
            for x in range(0, tile_type_width):
                tile = Tile(tile_sheet.get_image(x * 16, y * 16, 16, 16))

                # Define water tile depths
                if y <= 5:
                    tile.depth = 2
                if y == 0:
                    if x == 0:
                        tile.depth = 10
                    if x == 1:
                        tile.depth = 8
                if y == 1 and x == 3:
                    tile.depth = 8
                if y == 4 and x == 3:
                    tile.depth = 4

                # Define flower bed depth
                if y >= 141 and y < 152:
                    tile.depth = 2

                # Define which tiles are walls
                if y >= 152:
                    tile.solid = True

                # Add tile to list of tile types
                self.tiles.append(tile)

        # Define Starting Position for Camera
        self.x_scroll = 400
        self.y_scroll = 400

        # Add Player to Level
        self.entities.append(Player(500, 500))
