import pygame

import conf
from spritesheet_parser import get_sprite

JUMP_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 2, 0),
                                     conf.INGAME_TILE_SIZE)

IDLE_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 0),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 1),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 2),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITE_4 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 3),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITES = [IDLE_SPRITE_1, IDLE_SPRITE_2, IDLE_SPRITE_3]

RUN_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 0),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 1),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 2),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITES = [RUN_SPRITE_1, RUN_SPRITE_2, RUN_SPRITE_3]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IDLE_SPRITE_1
        self.rect = self.image.get_rect(bottomleft=conf.PLAYER_POSITION)
        self.gravity = 0
        self.idle_sprite = 0
        self.running = False
        self.run_sprite = 0
        self.score = 0

    def run(self):
        if self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.run_sprite += 0.1
            if self.run_sprite >= len(RUN_SPRITES):
                self.run_sprite = 0
            self.image = RUN_SPRITES[int(self.run_sprite)]
            self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def idle(self):
        self.idle_sprite += 0.05
        if self.idle_sprite >= len(IDLE_SPRITES):
            self.idle_sprite = 0
        self.image = IDLE_SPRITES[int(self.idle_sprite)]
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def input(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.score > 1:
            if self.running and self.rect.bottom >= conf.PLAYER_POSITION[1]:
                self.image = JUMP_SPRITE
                self.image.set_colorkey(conf.COLOR_TRANSPARENT)
                self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.rect.bottom = conf.PLAYER_POSITION[1]

    def update(self):
        if self.running:
            self.run()
        else:
            self.idle()
        self.input()
        self.apply_gravity()
