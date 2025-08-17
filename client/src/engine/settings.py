import pygame as pg
import socket
import os
import sys
import threading

pg.init()

SERVER_PORT = 5555
SERVER_ADDRESS = "localhost"

WINDOW_RESOLUTION = WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
WINDOW_TITLE = "Pirate LAN"