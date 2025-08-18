import os
from os import PathLike

from client.src.engine.settings import *

def load_folder(path:PathLike, *args, **kwargs) -> list[pg.Surface]:
    images = []

    for _,__,image_paths in os.walk(path):
        for image_path in image_paths:
            full_path = os.path.join(path,image_path)

            if "convert" in args:
                image = pg.image.load(full_path).convert()
            else:
                image = pg.image.load(full_path).convert_alpha()

            images.append(image)

    return images