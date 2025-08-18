from client.src.engine.settings import *
from client.src.engine.loader import load_folder

class Generator:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.assets = self.load_assets()

    @staticmethod
    def load_assets():
        return {
            "player":{
                "idle":load_folder(os.path.join("assets", "Captain Clown Nose", "Sprites", "Captain Clown Nose", "Captain Clown Nose with Sword", "09-Idle Sword"))
            }
        }

    def render(self):
        self.win.blit(self.assets["player"]["idle"][0])

    def update(self,dt):
        pass