import pygame
import conf
from spritesheet_parser import get_sprite

FLY_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 6, 0),
                                      conf.INGAME_TILE_SIZE)
FLY_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 6, 1),
                                      conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 0),
                                         conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 1),
                                         conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 2),
                                         conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_4 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 3),
                                         conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_5 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 4),
                                         conf.INGAME_TILE_SIZE)
ONEEYE_SPRITE_6 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 3, 5),
                                         conf.INGAME_TILE_SIZE)
DRILL_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 0),
                                        conf.INGAME_TILE_SIZE)
DRILL_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 1),
                                        conf.INGAME_TILE_SIZE)
DRILL_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 2),
                                        conf.INGAME_TILE_SIZE)
DRILL_SPRITE_4 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 3),
                                        conf.INGAME_TILE_SIZE)
DRILL_SPRITE_5 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 4),
                                        conf.INGAME_TILE_SIZE)
DRILL_SPRITE_6 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 4, 5),
                                        conf.INGAME_TILE_SIZE)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_array):
        super().__init__()
        self.image_array = image_array
        self.image = self.image_array[0]
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)
        self.rect = self.image.get_rect(bottomleft=conf.ENEMY_POSITION)
        self.move_sprite = 0
        self.sprite_speed = 0.2
        self.speed = 5

    def move(self):
        self.move_sprite += self.sprite_speed
        if self.move_sprite >= len(self.image_array):
            self.move_sprite = 0
        self.image = self.image_array[int(self.move_sprite)]
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)
        self.rect.x -= self.speed

    def update(self):
        self.move()


class Fly(Enemy):
    def __init__(self):
        self.image_array = [FLY_SPRITE_1, FLY_SPRITE_2]
        super().__init__(self.image_array)


class OneEye(Enemy):
    def __init__(self):
        self.image_array = [ONEEYE_SPRITE_1, ONEEYE_SPRITE_2, ONEEYE_SPRITE_3,
                            ONEEYE_SPRITE_4, ONEEYE_SPRITE_5, ONEEYE_SPRITE_6]
        super().__init__(self.image_array)


class Drill(Enemy):
    def __init__(self):
        self.image_array = [DRILL_SPRITE_1, DRILL_SPRITE_2, DRILL_SPRITE_3,
                            DRILL_SPRITE_4, DRILL_SPRITE_5, DRILL_SPRITE_6]
        super().__init__(self.image_array)
