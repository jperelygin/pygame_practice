import pygame
from spritesheet_parser import get_sprite
import conf

GRASS_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 11, 0),
                                        conf.INGAME_TILE_SIZE)
GRASS_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 11, 1),
                                        conf.INGAME_TILE_SIZE)
HOUSE_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, (48, 32), 4, 0),
                                      (240, 160))

class Decoration(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ""
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.speed = 3

    def move(self):
        self.rect.x -= self.speed


class Grass(Decoration):
    def __init__(self):
        super().__init__()
        self.image_array = [GRASS_SPRITE_1, GRASS_SPRITE_2]
        self.image = self.image_array[0]
        self.rect = self.image.get_rect(bottomleft=conf.DECOR_START_POSITION)
        self.sprite = 0
        self.sprite_speed = 0.02

    def update_sprite(self):
        self.sprite += self.sprite_speed
        if self.sprite >= len(self.image_array):
            self.sprite = 0
        self.image = self.image_array[int(self.sprite)]
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def update(self):
        self.move()
        self.update_sprite()


class House(Decoration):
    def __init__(self):
        super().__init__()
        self.image = HOUSE_SPRITE
        self.rect = self.image.get_rect(bottomleft=conf.DECOR_START_POSITION)
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def update(self):
        self.move()
