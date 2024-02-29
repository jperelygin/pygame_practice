import pygame

import conf
from spritesheet_parser import get_sprite

JUMP_SPRITE = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 2, 0),
                                     conf.INGAME_TILE_SIZE)

IDLE_SPRITE_1 = pygame.transform.scale(get_sprite(conf.sprite_sheet, conf.TILE_SIZE, 0, 0),
                                       conf.INGAME_TILE_SIZE)

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
        self.running = 0

    def run(self):
        if self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.running += 0.1
            if self.running >= len(RUN_SPRITES):
                self.running = 0
            self.image = RUN_SPRITES[int(self.running)]
            self.image.set_colorkey(conf.COLOR_TRANSPARENT)

    def input(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.image = JUMP_SPRITE
            self.image.set_colorkey(conf.COLOR_TRANSPARENT)
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= conf.PLAYER_POSITION[1]:
            self.rect.bottom = conf.PLAYER_POSITION[1]

    def update(self):
        self.run()
        self.input()
        self.apply_gravity()

        # player_surf = get_sprite(conf.sprite_sheet, 16, 16, 1, int(self.sprite_counter))
        # player_surf.set_colorkey(conf.COLOR_TRANSPARENT)
        # player_surf = pygame.transform.scale(player_surf, (200, 200))
        # player_rect = player_surf.get_rect(center=(conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2))
        # self.screen.blit(player_surf, player_rect)
