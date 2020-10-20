#pylint: disable=F0401
'''
This handles Tile-based levels
'''
from game import game
from entity.mob.player import Player
from ..level import Level

class GameLevel(Level):
    '''
    Tile Based Level
    '''
    # Define tile dimenstions
    width = 0
    height = 0

    # Tile types for level
    tiles = []

    # Tile map for level
    tile_map = []

    ################################################################################################
    # Initialize Level
    ################################################################################################
    def __init__(self):
        #Call Level constructor
        super().__init__()

    ################################################################################################
    # Update Level
    ################################################################################################
    def update(self):
        '''
        This loops through every element of the level and calls it's update function.
        '''
        for entity in self.entities:
            entity.update()
            if isinstance(entity, Player):
                self.scroll_follow(entity.x, entity.y)

    ################################################################################################
    # Move Camera towards x, y Positon
    ################################################################################################
    def scroll_follow(self, x, y):
        '''
        Moves camera position towards the x, y position specified in the level
        '''
        # Distance from edge of screen that merits moving the camera
        camera_border = 128

        # Check each of the 4 sides of the screen
        if x - self.x_scroll < camera_border:
            if self.x_scroll > 0:
                self.x_scroll -= 2
        if x - self.x_scroll > -camera_border + game.SCREEN_WIDTH:
            if self.x_scroll < self.width * 16 - game.SCREEN_WIDTH:
                self.x_scroll += 2
        if y - self.y_scroll < camera_border:
            if self.y_scroll > 0:
                self.y_scroll -= 2
        if y - self.y_scroll > -camera_border + game.SCREEN_HEIGHT:
            if self.y_scroll < self.height * 16 - game.SCREEN_HEIGHT:
                self.y_scroll += 2

    ################################################################################################
    # Render Level
    ################################################################################################
    def draw(self, screen):
        # Define the 4 corners of the screen
        x0 = int((self.x_scroll - 16) / 16)
        x1 = int((self.x_scroll + game.SCREEN_WIDTH + 16) / 16)
        y0 = int((self.y_scroll - 16) / 16)
        y1 = int((self.y_scroll + game.SCREEN_HEIGHT + 16) / 16)

        #Loop through tile_map
        for y in range (y0, y1):
            for x in range (x0, x1):
                # Location on screen
                coords = (x * 16 - self.x_scroll, y * 16 - self.y_scroll)
                # Draw Tile
                screen.blit(self.get_tile(x, y).sprite, coords)

        super().draw(screen)

    ################################################################################################
    # Get tile at coordinate x, y
    ################################################################################################
    def get_tile(self, x, y):
        '''
        Takes a tile coordinate and returns the type of tile at that location
        '''
        if (x < 0 or y < 0 or x >= self.width or y >= self.height or len(self.tile_map) == 0 or\
                len(self.tiles) == 0):
            return self.tiles[0]
        try:
            return self.tiles[int(self.tile_map[y * self.width + x])]
        except IndexError:
            return self.tiles[0]

    ################################################################################################
    # Loads tile array from file
    ################################################################################################
    def load_level(self, file_name):
        '''
        Loads tiles from file format .csv
        '''
        map_file = open(file_name, "r")
        rows = map_file.readlines()
        map_file.close()

        self.height = len(rows)
        self.width = len(rows[0].split(","))

        tile_map = []
        for row in rows:
            row = row.split(",")
            for element in row:
                tile_map.append(element)

        return tile_map
