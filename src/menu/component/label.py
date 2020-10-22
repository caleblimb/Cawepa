'''
This hadles what I'm calling lables. They are text object that are drawn on the screen.
'''
import pygame
from .component import Component

class Label(Component):
    ''' Set up default parameters for Label '''
    text = None
    font_size = 12
    color = (0,0,0)
    font = None
    def __init__(self, x, y, width, height, font_size, text):
        super().__init__(x, y, width, height)
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", font_size)
        self.set_text(text)

    ################################################################################################
    # Set Label Text
    ################################################################################################
    def set_text(self, text):
        ''' This is needed because simply changing the value of "text" will not update how it will
            render to the screen '''
        self.text = self.font.render(text, 1, self.color)

    ################################################################################################
    # Draw Label Text to the screen
    ################################################################################################
    def draw(self, screen):
        ''' This draws the text centered both horizontally and vertically. If you want it to print
            out left-aligned then just make sure the width of the label is 0 '''
        screen.blit(self.text, \
            (self.x +self.width / 2 - self.text.get_width() / 2, \
             self.y +self.height / 2 - self.text.get_height() / 2))
