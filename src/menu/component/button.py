#pylint: disable=F0401
from game import game
from .component import Component

class Button(Component):
    '''
    This handles in-game buttons such as menu buttons
    '''
    sprite_idle = None
    sprite_hover = None
    sprite_pressed = None
    mouse_pressed = False
    action_event = False
    enable = False

    def __init__(self, x, y, width, height, sprite_idle, sprite_hover, sprite_pressed):
        super().__init__(x, y, width, height)
        self.sprite_idle = sprite_idle
        self.sprite_hover = sprite_hover
        self.sprite_pressed = sprite_pressed

    def update(self):
        hover = self.x <= game.MOUSE_X <= self.x + self.width and \
                self.y <= game.MOUSE_Y <= self.y + self.height

        if hover:
            self.sprite = self.sprite_hover
            if game.MOUSE_LEFT:
                if self.enable:
                    self.mouse_pressed = True
                    self.sprite = self.sprite_pressed
            else:
                if self.mouse_pressed:
                    self.action_event = True
                self.enable = True
                self.mouse_pressed = False
        else:
            if not game.MOUSE_LEFT:
                self.mouse_pressed = False
                self.enable = False
            self.sprite = self.sprite_idle

    def reset_action_event(self):
        self.action_event = False
