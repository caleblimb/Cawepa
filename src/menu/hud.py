#pylint: disable=F0401
'''
This is the heads up display. It shows things such as the health bar and inventory hot bar
'''
import pygame
from game.sprite import SpriteSheet

class HUD():
    def __init__(self):
        self.x = 6
        self.y = 6

        self.total_health = 51
        self.total_stamina = 51
        self.total_mana = 51
        self.health = 100
        self.stamina = 100
        self.mana = 100

        # Create Player spritesheet
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("res/graphics/hud_sheet.png")

        self.bars = sprite_sheet.get_image(0, 0, 100, 32)
        self.health_bar = sprite_sheet.get_image(0, 32, 51, 4)
        self.stamina_bar = sprite_sheet.get_image(0, 36, 51, 4)
        self.mana_bar = sprite_sheet.get_image(0, 40, 51, 4)

    def draw(self, screen):
        # Draw Bars frame
        screen.blit(self.bars, (self.x, self.y))
        # Draw Health bar
        screen.blit(self.health_bar, (self.x + 37, self.y + 4), \
            (0, 0, int(self.total_health / 100 * self.health), 4))
        # Draw Stamina bar
        screen.blit(self.stamina_bar, (self.x + 37, self.y + 14), \
            (0, 0, int(self.total_stamina / 100 * self.stamina), 4))
        # Draw Mana bar
        screen.blit(self.mana_bar, (self.x + 37, self.y + 24), \
            (0, 0, int(self.total_mana / 100 * self.mana), 4))
