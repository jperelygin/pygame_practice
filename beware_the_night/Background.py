import pygame
import conf
from spritesheet_parser import get_sprite

DAY_SPRITE = get_sprite(conf.backgrounds, (231, 62), 0, 0)
NIGHT_SPRITE = get_sprite(conf.backgrounds, (231, 62), 1, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = DAY_SPRITE
        self.image = pygame.transform.scale(self.image, (conf.SCREEN_WIDTH + 2, conf.SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, 0))
