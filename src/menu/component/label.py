import pygame
from .component import Component

class Label(Component):
    text = None
    font_size = 12
    color = (0,0,0)
    font = None
    def __init__(self, x, y, width, height, font_size, text):
        super().__init__(x, y, width, height)
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", font_size)
        self.setText(text)

    def setText(self, text):
        self.text = self.font.render(text, 1, self.color)

    def draw(self, screen):
        screen.blit(self.text, \
            (self.x +self.width / 2 - self.text.get_width() / 2, \
             self.y +self.height / 2 - self.text.get_height() / 2))
