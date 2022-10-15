import pygame


class Car:
    def __init__(self, image: str, x: int, y: int, window: pygame.Surface, speed: int = 10):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.initial_speed = speed
        self.speed = speed
        self.window = window
        self.score = 0

    def move(self, direction: int):
        if direction not in (-1, 1):
            raise ValueError("Direction have to be equal to 1 or -1")
        new_position = self.y + direction * self.speed
        if new_position >= 0 and new_position + 40 <= self.window.get_height():
            self.y = new_position

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return [self.x,  self.x + self.image.get_width(), self.y, self.y + self.image.get_height()]

    def win(self):
        self.score += 1

    def drop_score(self):
        self.score = 0
