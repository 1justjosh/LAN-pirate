from client.src.engine.settings import *

class ConnectToServerUI:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.border = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), flags=pg.SRCALPHA)
        self.border.fill((20,40,80))
        self.border_rect = self.border.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        self.font = pg.font.Font(pg.font.get_default_font(), 40)
        self.dot_count = 0
        self.connecting_text = self.font.render("Connecting to Server", False, (200, 200, 200))

    def animate_text(self, dt):
        self.dot_count += 2 * dt

        if int(self.dot_count) > 3:
            self.dot_count = 0

        self.connecting_text = self.font.render(f"Connecting to Server {"." * int(self.dot_count)}", False, (200, 200, 200))


    def render(self):
        self.win.blit(self.border,self.border_rect)
        self.win.blit(self.connecting_text, (WINDOW_WIDTH // 2 - self.connecting_text.get_width() // 2,WINDOW_HEIGHT // 2 - self.connecting_text.get_height() // 2))

    def update(self,dt):
        self.animate_text(dt)