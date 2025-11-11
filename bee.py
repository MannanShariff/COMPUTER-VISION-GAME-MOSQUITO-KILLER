import random
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BEE_SPEED

class Bee(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 200)
        self.speed_x = random.choice([-BEE_SPEED, BEE_SPEED])
        self.speed_y = random.choice([-BEE_SPEED, BEE_SPEED])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT - 100:
            self.speed_y *= -1
