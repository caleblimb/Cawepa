'''
This module is used to pull individual sprites from sprite sheets.
'''
import pygame

class Sprite():
    ''' This handles a single sprite image and contains meta-data about that sprite '''
    image = None
    width = 0
    height = 0

    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height

    # Draws sprite to screen
    def draw(self, screen, x, y):
        ''' Draw sprite '''
        screen.blit(self.image, (x, y))

    # Draws sprite to screen to w
    def draw_sub(self, screen, x, y, w):
        ''' This chops of the bottom of the sprite w pixels from the bottom
            It is used for drawing things that are partially underwater or in tall grass '''
        screen.blit(self.image, (x,y), (0, 0, self.width, self.height - w))

    def rot_center(self, angle):
        ''' rotate an image while keeping its center '''
        self.image = pygame.transform.rotate(self.image, angle)

class SpriteSheet():
    ''' Class used to grab images out of a sprite sheet. '''
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        ''' Constructor. Pass in the file name of the sprite sheet. '''

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        ''' Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. '''

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Setting the transparent color of sprites to 0x FF00FF
        image.set_colorkey((255, 0, 255))

        # Return the image
        return image
