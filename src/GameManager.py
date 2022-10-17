import pygame
from os.path import join

from Car import Car
from Circle import Circle
from constants import COLORS, SCRIPT_PATH


class GameManager:
    def __init__(self, window, time, background_image, fps: int = 50):
        self.window = window
        self.fps = fps
        self.time = time
        self.background = pygame.image.load(background_image)
        self.init_objects()
        self.run = True
        self.pause = True
        self.font = pygame.font.SysFont('arial', 30)
        self.has_winner = True
        self.victory_sound = pygame.mixer.Sound(join(SCRIPT_PATH, "assets", "sounds", "victory.wav"))

    def init_objects(self):
        self.red_car = Car(join(SCRIPT_PATH, "assets/images", "RedCar.jpg"), 0, 220, self.window)
        self.blue_car = Car(join(SCRIPT_PATH, "assets/images", "BlueCar.jpg"), self.window.get_width() - 20, 220, self.window)
        self.circle = Circle(self.window.get_width() / 2, self.window.get_height() / 2, 10)

    def get_text(self):
        if self.red_car.score < 6 and self.blue_car.score < 6:
            text = f"{self.red_car.score}:{self.blue_car.score}"
        else:
            self.has_winner = True
            self.victory_sound.play()
            if self.red_car.score == 6:
                text = "Red player wins!"
            else:
                text = "Blue player wins!"
            self.change_pause(self.has_winner)
        text_object = self.font.render(text, True, COLORS['white'])
        text_rect = text_object.get_rect()
        text_rect.center = (self.window.get_width() / 2, 100)
        return text_object, text_rect

    def draw_objects(self):
        self.window.blit(self.background, (0, 0))
        self.red_car.draw()
        self.blue_car.draw()
        text, text_rect = self.get_text()
        self.window.blit(text, text_rect)
        if self.has_winner:
            text = "Press <SPACE> to start new game"
            text_object = self.font.render(text, True, COLORS['white'])
            text_rect = text_object.get_rect()
            text_rect.center = (self.window.get_width() / 2, 150)
            self.window.blit(text_object, text_rect)
        pygame.draw.circle(self.window, (COLORS['yellow']), (self.circle.get_position()), self.circle.radius)

    def change_pause(self, value):
        self.pause = value

    def reset_game(self):
        self.init_objects()
        self.has_winner = False

    def game_loop(self):
        while self.run:
            self.time.tick(self.fps)
            self.draw_objects()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if self.has_winner and event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.change_pause(False)
                    if event.key == pygame.K_ESCAPE and not self.has_winner:
                        self.change_pause(not self.pause)
            if not self.pause:
                keys = pygame.key.get_pressed()
                self.circle.move(self.window.get_height(), self.window.get_width(), self.red_car, self.blue_car)
                if keys[pygame.K_s]:
                    self.red_car.move(1)
                elif keys[pygame.K_w]:
                    self.red_car.move(-1)
                elif keys[pygame.K_DOWN]:
                    self.blue_car.move(1)
                elif keys[pygame.K_UP]:
                    self.blue_car.move(-1)
            pygame.display.update()
