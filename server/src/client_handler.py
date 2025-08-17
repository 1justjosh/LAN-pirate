import socket
import threading

from server.src.settings import *

class ClientHandler:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((SERVER_ADDRESS,SERVER_PORT))
        self.server.listen()

        print(f"server has started | {socket.gethostbyname(socket.gethostname())}")

        self.running = True
        self.lock = threading.Lock()

    def connect_client(self, conn, addr):
        try:
            while self.running:
                # Placeholder for actual recv/send logic
                pass
        except Exception as e:
            print(f"Client {addr} Disconnected -> {e}")
        finally:
            conn.close()

    def run(self):
        while self.running:
            conn,addr = self.server.accept()
            print(f"Client {addr} connected from")

            threading.Thread(target=self.connect_client, args=(conn,addr), daemon=True).start()
