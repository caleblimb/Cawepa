
class Component():
    x = 0
    y = 0
    width = 0
    height = 0
    sprite = None
    label = None

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        if self.label:
            self.label.draw(screen)
