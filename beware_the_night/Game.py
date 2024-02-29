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
        self.player_instance = Player()
        self.player.add(self.player_instance)
        self.background = pygame.sprite.Group()
        self.background.add(Background(0))
        self.floor = pygame.sprite.Group()
        self.floor.add(Floor(0))
        # events
        self.background_move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.background_move_event, 100)
        self.floor_move_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.floor_move_event, 10)
        self.score_update = pygame.USEREVENT + 3
        pygame.time.set_timer(self.score_update, 500)

    def move_background(self):
        for sprite in self.background.sprites():
            sprite.rect.x -= 1
        if self.background.sprites()[-1].rect.midright[0] <= conf.SCREEN_WIDTH + 1:
            self.background.add(Background(conf.SCREEN_WIDTH + 1))
        if self.background.sprites()[0].rect.midright[0] <= -2:
            self.background.remove(self.background.sprites()[0])

    def move_floor(self):
        for sprite in self.floor.sprites():
            sprite.rect.x -= 1

    def update_floor(self):
        while self.floor.sprites()[-1].rect.midright[0] <= conf.SCREEN_WIDTH + 10:
            self.floor.add(Floor(self.floor.sprites()[-1].rect.midright[0]))
        if self.floor.sprites()[0].rect.midright[0] <= -2:
            self.floor.remove(self.floor.sprites()[0])

    def update_score(self):
        self.player_instance.score += 1

    def new_game(self):
        pass

    def update(self):
        pygame.display.update()
        self.clock.tick(conf.FPS)
        pygame.display.set_caption(f"{conf.GAME_TITLE}. Score: {self.player_instance.score}")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if pygame.key.get_pressed()[pygame.K_SPACE] and not self.player_instance.running:
                self.player_instance.running = True
            if event.type == self.background_move_event and self.player_instance.running:
                self.move_background()
            if event.type == self.floor_move_event and self.player_instance.running:
                self.move_floor()
            if event.type == self.score_update and self.player_instance.running:
                self.update_score()

    def draw(self):
        self.screen.fill(conf.COLOR_DARK)
        self.background.draw(self.screen)
        self.update_floor()
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
