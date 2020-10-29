#pylint: disable=F0401
'''
This handles Tile-based levels
'''
from game import game
from entity.mob.fauna.chicken import Chicken
from entity.mob.player import Player
from entity.mob.mob import Mob
from ..level import Level
from .tile import TileMap

class GameLevel(Level):
    ''' Tile Based Level '''
    tile_map = None

    players = []
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
        game.CLIENT_PLAYER.update(self.tile_map, self.x_scroll, self.y_scroll)
        self.scroll_follow(game.CLIENT_PLAYER.x, game.CLIENT_PLAYER.y)

        for entity in self.entities:
            entity.update(self.tile_map, self.x_scroll, self.y_scroll)
            if isinstance(entity, Mob):
                if entity.projectile:
                    self.entities.append(entity.projectile)
                    entity.projectile = None

        for player in self.players:
            if player.projectile:
                self.entities.append(player.projectile)
                player.projectile = None


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
        while x - self.x_scroll > -camera_border + game.SCREEN_WIDTH and self.x_scroll < self.tile_map.width * 16 - game.SCREEN_WIDTH:
            # Move the camera right
            self.x_scroll += 1

        # If on top of screen
        # Make sure the camera isn't already at the edge of the level
        while y - self.y_scroll < camera_border and self.y_scroll > 0:
                # Move the camera up
                self.y_scroll -= 1

        # If on bottom of screen
        # Make sure the camera isn't already at the edge of the level
        while y - self.y_scroll > -camera_border + game.SCREEN_HEIGHT and self.y_scroll < self.tile_map.height * 16 - game.SCREEN_HEIGHT:
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

        self.drawTiles(screen, self.tile_map.tile_layer_0,  x0, x1, y0, y1)
        self.drawTiles(screen, self.tile_map.tile_layer_1,  x0, x1, y0, y1)

        ''' This loops through every element of the level and calls it's draw function. '''
        self.entities.sort(key=lambda Entity: Entity.y, reverse=False)
        self.players.sort(key=lambda Player: Player.y, reverse=False)
        player_index = 0

        if len(self.entities) > 0:
            for e in range (0, len(self.entities)):
                if player_index < len(self.players):
                    entity_before_y = 0
                    if e > 0:
                        entity_before_y = self.entities[e - 1].y
                    if entity_before_y <= self.players[player_index].y <= self.entities[e].y:
                        if - 32 < self.players[player_index].y - self.y_scroll < game.SCREEN_HEIGHT + 32 and - 32 < self.players[player_index].x - self.x_scroll < game.SCREEN_WIDTH + 32:
                            self.players[player_index].draw(screen, self.x_scroll, self.y_scroll)
                        player_index += 1

                if - 32 < self.entities[e].y - self.y_scroll < game.SCREEN_HEIGHT + 32 and - 32 < self.entities[e].x - self.x_scroll < game.SCREEN_WIDTH + 32:
                    self.entities[e].draw(screen, self.x_scroll, self.y_scroll)
        elif len(self.players) > 0:
            for p in self.players:
                p.drawdraw(screen, self.x_scroll, self.y_scroll)

        self.drawTiles(screen, self.tile_map.tile_layer_2,  x0, x1, y0, y1)
        game.CLIENT_PLAYER.hud.draw(screen)

    def drawTiles(self, screen, tile_layer, x0, x1, y0, y1):
        #Loop through tile_map
        for y in range (y0, y1):
            for x in range (x0, x1):
                # Location on screen
                coords = (x * 16 - self.x_scroll, y * 16 - self.y_scroll)
                # Draw Tile
                tile_sprite = self.tile_map.get_sprite(tile_layer, x, y)
                if tile_sprite:
                    screen.blit(tile_sprite, coords)

