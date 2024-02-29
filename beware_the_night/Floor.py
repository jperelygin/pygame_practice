import pygame
import conf
from spritesheet_parser import get_sprite

GROUND_SPRITE = get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 7, 6)
WATER_SPRITE = get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 7, 8)


class Floor(pygame.sprite.Sprite):
    def __init__(self, x: int, water=False):
        super().__init__()
        self.image = GROUND_SPRITE if not water else WATER_SPRITE
        self.image = pygame.transform.scale(self.image, conf.INGAME_TILE_SIZE)
        self.rect = self.image.get_rect(bottomleft=(x, conf.SCREEN_HEIGHT))
