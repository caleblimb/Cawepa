'''
This module is used to pull individual sprites from sprite sheets.
'''
import pygame

class Sprite():
    image = None
    width = 0
    height = 0

    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height

    # Draws sprite to screen
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    # Draws sprite to screen chopping the bottom off according to value of w
    def draw_sub(self, screen, x, y, w):
        screen.blit(self.image, (x,y), (0, 0, self.width, self.height - w))

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey((255, 0, 255))

        # Return the image
        return image
