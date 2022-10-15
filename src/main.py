import pygame
from os.path import join

from GameManager import GameManager
from constants import SCRIPT_PATH


window_width = 800
window_height = 480


if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Air Hockey")
    time = pygame.time.Clock()

    game = GameManager(window=window, time=time, background_image=join(SCRIPT_PATH, "images", "bg.jpg"))
    game.game_loop()
