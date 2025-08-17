from client.src.engine.settings import *
from client.src.engine.connection import try_connect, disconnect
from client.src.ui.connect_to_server import ConnectToServerUI

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(WINDOW_RESOLUTION)
        pg.display.set_caption(WINDOW_TITLE)

        self.clock = pg.time.Clock()

        self.running = True

        self.conn = None
        self.connect = threading.Thread(target=self.connect_to_server)
        self.connect.start()

        self.connect_to_server_ui = ConnectToServerUI()


    def connect_to_server(self):
        while self.conn is None and self.running:
            self.conn = try_connect()

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                if not self.connect.is_alive():
                    disconnect(self.conn)
                pg.quit()
                sys.exit()

    def render(self):
        if self.connect.is_alive():
            self.connect_to_server_ui.render()

        pg.display.flip()

    def update(self):
        dt = self.clock.tick(120) / 1000

        if self.connect.is_alive():
            self.connect_to_server_ui.update(dt)

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()