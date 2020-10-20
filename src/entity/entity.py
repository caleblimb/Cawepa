#pylint: disable=F0401
'''
This hadles everything that all entities have in common.
'''

class Entity():
    x = 0
    y = 0
    sprite = None
    sprite_x_offset = 0
    sprite_y_offset = 0
    collision_mask = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    ################################################################################################
    # Update Entity
    ################################################################################################
    def update(self, tile_map, tiles, width, height):
        '''
        This method is necessary as a placeholder for child classes
        '''

    ################################################################################################
    # Draw Entity
    ################################################################################################
    def draw(self, screen, x_offset, y_offset):
        '''
        Draws the sprite to the screen. x_offset and y_offset refer to the camera position.
        '''
        self.sprite.draw(screen, self.x - self.sprite_x_offset - x_offset, self.y - self.sprite_y_offset - y_offset)


    ################################################################################################
    # Get tile at coordinate x, y
    ################################################################################################
    def get_tile(self, tile_map, tiles, width, height, x, y):
        '''
        Takes a tile coordinate and returns the type of tile at that location.
        '''
        if (x < 0 or y < 0 or x >= width or y >= height or len(tile_map) == 0 or\
                len(tiles) == 0):
            return tiles[0]
        try:
            return tiles[int(tile_map[y * width + x])]
        except IndexError:
            return tiles[0]

    ################################################################################################
    # Get solid status tile at coordinate x, y
    ################################################################################################
    def tile_collision(self, tile_map, tiles, width, height, xa, ya):
        '''
        This method is used for collision detection with solid tiles such as walls.
        '''
        x0 = int((self.collision_mask.x + xa) / 16)
        x1 = int((self.collision_mask.x + xa + self.collision_mask.width) / 16)
        y0 = int((self.collision_mask.y + ya) / 16)
        y1 = int((self.collision_mask.y + ya + self.collision_mask.height) / 16)

        return self.get_tile(tile_map, tiles, width, height, x0, y0).solid or \
               self.get_tile(tile_map, tiles, width, height, x1, y0).solid or \
               self.get_tile(tile_map, tiles, width, height, x0, y1).solid or \
               self.get_tile(tile_map, tiles, width, height, x1, y1).solid

    ################################################################################################
    # Get average depth of collsion mask
    ################################################################################################
    def tile_depth(self, tile_map, tiles, width, height):
        '''
        This method takes the depth of each tile at the 4 corners of a collision mask and returns
        their average
        '''
        x0 = int((self.collision_mask.x) / 16)
        x1 = int((self.collision_mask.x + self.collision_mask.width) / 16)
        y0 = int((self.collision_mask.y) / 16)
        y1 = int((self.collision_mask.y + self.collision_mask.height) / 16)

        return (self.get_tile(tile_map, tiles, width, height, x0, y0).depth + \
                self.get_tile(tile_map, tiles, width, height, x1, y0).depth + \
                self.get_tile(tile_map, tiles, width, height, x0, y1).depth + \
                self.get_tile(tile_map, tiles, width, height, x1, y1).depth) / 4
