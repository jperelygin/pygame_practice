import pygame
import conf
from spritesheet_parser import get_sprite


class Background(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = get_sprite(conf.backgrounds, (231, 62), 0, 0)
        self.image = pygame.transform.scale(self.image, (conf.SCREEN_WIDTH + 2, conf.SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, 0))
