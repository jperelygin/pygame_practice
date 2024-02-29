import pygame
import sys

import conf
from Player import Player
from Background import Background
from Floor import Floor


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(conf.RES)
        self.clock = pygame.time.Clock()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.background = pygame.sprite.Group()
        self.background.add(Background(0))
        self.floor = pygame.sprite.Group()
        floor_increment = 0
        # TODO: Move to separate function
        while floor_increment < conf.SCREEN_WIDTH + 10:
            self.floor.add(Floor(floor_increment))
            floor_increment += conf.INGAME_TILE_SIZE[0]
            print(f"floor: {self.floor}")
        # events
        self.background_move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.background_move_event, 100)
        self.floor_move_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.floor_move_event, 10)

    def move_background(self):
        for sprite in self.background.sprites():
            sprite.rect.x -= 1
        if self.background.sprites()[-1].rect.midright[0] <= conf.SCREEN_WIDTH + 1:
            self.background.add(Background(conf.SCREEN_WIDTH + 1))
            print(f"sprites: {self.background}")
        if self.background.sprites()[0].rect.midright[0] <= -2:
            self.background.remove(self.background.sprites()[0])
            print(f"sprites: {self.background}")

    def move_floor(self):
        for sprite in self.floor.sprites():
            sprite.rect.x -= 1
        if self.floor.sprites()[-1].rect.midright[0] <= conf.SCREEN_WIDTH:
            self.floor.add(Floor(conf.SCREEN_WIDTH))
            print(f"floor sprites: {self.background}")
        if self.floor.sprites()[0].rect.midright[0] <= -2:
            self.floor.remove(self.floor.sprites()[0])
            print(f"floor sprites: {self.floor}")

    def new_game(self):
        pass

    def update(self):
        pygame.display.update()
        self.clock.tick(conf.FPS)
        pygame.display.set_caption(conf.GAME_TITLE)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == self.background_move_event:
                self.move_background()
            if event.type == self.floor_move_event:
                self.move_floor()

    def draw(self):
        self.screen.fill(conf.COLOR_DARK)
        self.background.draw(self.screen)
        self.floor.draw(self.screen)
        self.player.draw(self.screen)
        self.player.update()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
