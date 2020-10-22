#pylint: disable=F0401
'''
This handles Tile-based levels
'''
from game import game
from entity.mob.player import Player
from ..level import Level

class GameLevel(Level):
    ''' Tile Based Level '''
    # Define tile_map dimenstions
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
        ''' This loops through every element of the level and calls it's update function. '''
        for entity in self.entities:
            entity.update(self.tile_map, self.tiles, self.width, self.height)
            if isinstance(entity, Player):
                self.scroll_follow(entity.x, entity.y)

    ################################################################################################
    # Move Camera towards x, y Positon
    ################################################################################################
    def scroll_follow(self, x, y):
        ''' Moves camera position towards the x, y position specified in the level '''
        # Distance from edge of screen that merits moving the camera
        camera_border = 128

        # Check each of the 4 sides of the screen

        # If on left of screen
        # Make sure the camera isn't already at the edge of the level
        while x - self.x_scroll < camera_border and self.x_scroll > 0:
            # Move the camera left
                self.x_scroll -= 1

        # If on right of screen
        # Make sure the camera isn't already at the edge of the level
        while x - self.x_scroll > -camera_border + game.SCREEN_WIDTH and self.x_scroll < self.width * 16 - game.SCREEN_WIDTH:
            # Move the camera right
            self.x_scroll += 1

        # If on top of screen
        # Make sure the camera isn't already at the edge of the level
        while y - self.y_scroll < camera_border and self.y_scroll > 0:
                # Move the camera up
                self.y_scroll -= 1

        # If on bottom of screen
        # Make sure the camera isn't already at the edge of the level
        while y - self.y_scroll > -camera_border + game.SCREEN_HEIGHT and self.y_scroll < self.height * 16 - game.SCREEN_HEIGHT:
                # Move the camera down
                self.y_scroll += 1

    ################################################################################################
    # Render Level
    ################################################################################################
    def draw(self, screen):
        ''' Draws tile_map and then calls parent draw funtion to draw the rest like entities. '''
        # Define the 4 corners of the screen
        # top-left = (x0, y0), top-right = (x1,y0), bottom-left = (x0, y1), bottom-right = (x1, y1)
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

        #Parent draw function found in level.py
        super().draw(screen)

    ################################################################################################
    # Get tile at coordinate x, y
    ################################################################################################
    def get_tile(self, x, y):
        ''' Takes a tile coordinate and returns the type of tile at that location. '''
        # Check if the coordinate is outside of the level
        if (x < 0 or y < 0 or x >= self.width or y >= self.height or len(self.tile_map) == 0 or\
                len(self.tiles) == 0):
            return self.tiles[0]
        try:
            # Return the tile_type at the specified location
            return self.tiles[int(self.tile_map[y * self.width + x])]
        except IndexError:
            return self.tiles[0]

    ################################################################################################
    # Loads tile array from file
    ################################################################################################
    def load_level(self, file_name):
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

        # Create tile_map to return
        tile_map = []

        # Loop through rows
        for row in rows:
            # Loop through elements on a row
            row = row.split(",")
            for element in row:
                # Add element to tile_map
                tile_map.append(element)

        # Return result
        return tile_map
