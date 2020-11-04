#pylint: disable=F0401
'''
This is the template for a type of file
'''
from time import time_ns as nano_time
import pygame
from game import game
from game.sprite import SpriteSheet

class Tile():
    sprite = None

    ################################################################################################
    # Define Tile
    ################################################################################################
    def __init__(self, sprite):
        self.sprite = sprite

    def load_tiles(self, file_name):
        pass

class TileMap():
    # Tile types for level
    tiles = []

    width = 0
    height = 0
    # Background Layers
    tile_layer_background_1 = []
    tile_layer_background_2 = []

    # Foreground Layers
    tile_layer_foreground_1 = []
    tile_layer_foreground_2 = []

    tile_layer_solid = []
    tile_layer_depth = []

    # List of speacial tiles that need to be animated
    tiles_with_fire_animation = [1406, 1408, 1411, 1413, 1416, 1418, 1241, 1423, 1426, 1428, 1431]
    tiles_with_waterfall_animation = [1145, 1146, 1147, 1149, 1185, 1186, 1187, 1189]
    tiles_with_doors_that_open = []
    for i in range (440, 454):
        tiles_with_doors_that_open.append(i * 5)
        tiles_with_doors_that_open.append(i * 5 + 2)

    def __init__(self, folder_name):
        # Define dimenstions of tile spritesheet according to how many tiles it has
        self.tile_type_width = 5
        self.tile_type_height = 455

        # Create tile spritesheet
        pygame.sprite.Sprite.__init__(self)
        tile_sheet = SpriteSheet("res/graphics/tiles.png")

        # Add all tiles from tile spritesheet to tile types
        for y in range(0, self.tile_type_height):
            for x in range(0, self.tile_type_width):
                tile = tile_sheet.get_image(x * 16, y * 16, 16, 16)
                # Add tile to list of tile types
                self.tiles.append(tile)

        self.load_level(folder_name)        

    ################################################################################################
    # Get tile at coordinate x, y
    ################################################################################################
    def get_sprite(self, tile_map, x, y):
        ''' Takes a tile coordinate and returns the type of tile at that location. '''
        # Check if the coordinate is outside of the level
        if (x < 0 or y < 0 or x >= self.width or y >= self.height or len(tile_map) == 0 or\
                len(self.tiles) == 0):
            return None
        try:
            # Return the tile_type at the specified location
            tile_index = int(tile_map[y * self.width + x])
            if tile_index == -1:
                return None

            if tile_index in self.tiles_with_fire_animation and nano_time() // 100000000 % 2 == 0:
                return self.tiles[tile_index + 1]

            if tile_index in self.tiles_with_waterfall_animation and nano_time() // 100000000 % 2 == 0:
                return self.tiles[tile_index + self.tile_type_height]

            if tile_index in self.tiles_with_doors_that_open \
                and abs(game.PLAYER.x - (x * 16 + 8)) < 16 and abs(game.PLAYER.y - (y * 16 + 8)) < 32:
                return self.tiles[tile_index + 1]

            return self.tiles[tile_index]
        except IndexError:
            return None

    ################################################################################################
    # Get solid status tile at coordinate x, y
    ################################################################################################
    def tile_collision(self, collision_mask, xa, ya):
        ''' This method is used for collision detection with solid tiles such as walls. '''
        # Define the 4 corners of the collsion mask
        # top-left = (x0, y0), top-right = (x1,y0), bottom-left = (x0, y1), bottom-right = (x1, y1)
        x0 = int((collision_mask.x + xa) // 16)
        x1 = int((collision_mask.x + xa + collision_mask.width) // 16)
        y0 = int((collision_mask.y + ya) // 16)
        y1 = int((collision_mask.y + ya + collision_mask.height) // 16)

        try:
            # Return a collsion if any of the four corners run into a solid tile
            return self.tile_layer_solid[y0 * self.width + x0] != -1 or \
                    self.tile_layer_solid[y0 * self.width + x1] != -1 or \
                    self.tile_layer_solid[y1 * self.width + x0] != -1 or \
                    self.tile_layer_solid[y1 * self.width + x1] != -1
        except IndexError:
            return True

    ################################################################################################
    # Get average depth of collsion mask
    ################################################################################################
    def tile_depth(self, collision_mask):
        ''' This method takes the depth of each tile at the 4 corners of a collision mask and
        returns their average. '''
        # Define the 4 corners of the collsion mask
        # top-left = (x0, y0), top-right = (x1,y0), bottom-left = (x0, y1), bottom-right = (x1, y1)
        x0 = int((collision_mask.x) / 16)
        x1 = int((collision_mask.x + collision_mask.width) / 16)
        y0 = int((collision_mask.y) / 16)
        y1 = int((collision_mask.y + collision_mask.height) / 16)

        # Return average depth of each corner
        return (self.tile_layer_depth[y0 * self.width + x0] + \
                self.tile_layer_depth[y0 * self.width + x1] + \
                self.tile_layer_depth[y1 * self.width + x0] + \
                self.tile_layer_depth[y1 * self.width + x1]) / 4

    ################################################################################################
    # Loads tile array from file
    ################################################################################################
    def load_level(self, folder_name):
        # Background Layers
        self.tile_layer_background_1 = self.load_array(folder_name + "/background_1.csv")
        self.tile_layer_background_2 = self.load_array(folder_name + "/background_2.csv")
        self.tile_layer_foreground_1 = self.load_array(folder_name + "/foreground_1.csv")
        self.tile_layer_foreground_2 = self.load_array(folder_name + "/foreground_2.csv")
        self.tile_layer_solid = self.load_array(folder_name + "/collision.csv")

        for tile in self.tile_layer_background_1:
            if tile <= 14:
                self.tile_layer_depth.append(16 - tile)
            elif 15 <= tile <= 29:
                self.tile_layer_depth.append(2)
            elif 60 <= tile <= 119:
                self.tile_layer_depth.append(2)
            elif 1120 <= tile <= 1199:
                self.tile_layer_depth.append(2)
            else:
                self.tile_layer_depth.append(0)

    def load_array(self, file_name):
        ''' Loads tiles from file format .csv and returns and array of those tiles.
            It also sets the width and height of the level tile map.
            Hopefully we'll update this to also load entities using a different file tiype. '''

        # Open file
        map_file = open(file_name, "r")

        # Create a matrix of rows with each element being a row
        rows = map_file.readlines()

        # Close file
        map_file.close()

        # Set map height and width based on the file_data
        self.height = len(rows)
        self.width = len(rows[0].split(","))

        tile_array = []
        # Loop through rows
        for row in rows:
            # Loop through elements on a row
            row = row.split(",")
            for element in row:
                # Add element to tile_map
                tile_array.append(int(element))
        return tile_array
