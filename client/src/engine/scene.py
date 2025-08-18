from client.src.engine.settings import *
from client.src.world.generator import Generator

class Scene:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.generator = Generator()

    def render(self):
        self.generator.render()

    def update(self, dt):
        self.generator.update(dt)