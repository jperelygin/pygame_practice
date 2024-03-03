import pygame

import conf
from spritesheet_parser import get_sprite

JUMP_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 2, 0),
                                     conf.INGAME_TILE_SIZE)
FALL_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 2, 1),
                                     conf.INGAME_TILE_SIZE)

IDLE_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 0),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 1),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 2),
                                       conf.INGAME_TILE_SIZE)
IDLE_SPRITES = [IDLE_SPRITE_1, IDLE_SPRITE_2, IDLE_SPRITE_3]

RUN_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 0),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITE_2 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 1),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITE_3 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 2),
                                      conf.INGAME_TILE_SIZE)
RUN_SPRITES = [RUN_SPRITE_1, RUN_SPRITE_2, RUN_SPRITE_3]

DAMAGE_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 2, 5),
                                       conf.INGAME_TILE_SIZE)

CROUCH_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 1, 4),
                                       conf.INGAME_TILE_SIZE)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IDLE_SPRITE_1
        self.rect = self.image.get_rect(bottomleft=conf.PLAYER_POSITION)
        self.gravity = 0
        self.idle_sprite = 0
        self.is_running = False
        self.run_sprite = 0
        self.score = 0
        self.current_position = conf.PLAYER_POSITION
        self.health = 1
        self.is_crouching = False

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

    def jump(self):
        self.image = JUMP_SPRITE
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)
        self.gravity = -20

    def fall(self):
        self.image = FALL_SPRITE
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def damage(self):
        self.image = DAMAGE_SPRITE
        self.is_running = False
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def crouch(self):
        self.image = CROUCH_SPRITE
        self.image.set_colorkey(conf.COLOR_TRANSPARENT)
        self.is_crouching = True

    def input(self):
        if pygame.key.get_pressed()[pygame.K_w] and self.score > 1 and not self.is_crouching:
            if self.is_running and self.rect.bottom >= conf.PLAYER_POSITION[1]:
                self.jump()

    def apply_gravity(self):
        if self.is_running:
            if self.rect.bottomleft[1] > self.current_position[1]:
                self.fall()
            self.current_position = self.rect.bottomleft
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.rect.bottom = conf.PLAYER_POSITION[1]

    def update(self):
        if self.is_running and not self.is_crouching:
            self.run()
        elif self.is_crouching:
            self.crouch()
        else:
            self.idle()
        self.input()
        self.apply_gravity()
