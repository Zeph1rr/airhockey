from random import choice
from os.path import join
import pygame

from Car import Car
from constants import SCRIPT_PATH

class Circle:
    def __init__(self, x, y, radius, speed: int = 5):
        self.initial_x = x
        self.initial_y = y
        self.radius = radius
        self.speed = speed
        self.initial_speed = speed
        self.reset()
        self.win_sound = pygame.mixer.Sound(join(SCRIPT_PATH, "assets", "sounds", "win.wav"))
        self.collision_sound = pygame.mixer.Sound(join(SCRIPT_PATH, "assets", "sounds", "collision.wav"))
        self.win_sound.set_volume(0.1)
        self.collision_sound.set_volume(0.1)

    def get_position(self):
        return self.x, self.y

    def reset(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed = self.initial_speed
        self.x_direction = choice([1, -1])
        self.y_direction = choice([1, -1])

    def check_walls(self, window_height, window_width, red_car, blue_car):
        if self.y > window_height or self.y < 0:
            self.y_direction *= -1
            self.collision_sound.play()
        if self.x >= window_width or self.x <= 0:
            self.win_sound.play()
            if self.x >= window_width:
                red_car.win()
            if self.x <= 0:
                blue_car.win()
            self.reset()

    def check_collision(self, red_car, blue_car):
        return red_car[0] <= self.x <= red_car[1] and red_car[2] <= self.y <= red_car[3] \
               or blue_car[0] <= self.x <= blue_car[1] and blue_car[2] <= self.y <= blue_car[3]

    def move(self, window_height, window_width, red_car: Car, blue_car: Car):
        self.x += self.x_direction * self.speed
        self.y += self.y_direction * self.speed
        if self.check_collision(red_car.get_rect(), blue_car.get_rect()):
            self.x_direction *= -1
            self.speed += 1
            self.collision_sound.play()
            return
        self.check_walls(window_height, window_width, red_car, blue_car)
