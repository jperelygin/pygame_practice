import pygame
import sys

import conf
from Player import Player
from Background import Background
from Floor import Floor
from Enemy import Fly, OneEye, Drill
from UI import GameState, StartMenu, RunningMenu

DEBUG = False


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(conf.RES)
        self.clock = pygame.time.Clock()
        # events (timers)
        self.background_move_event = pygame.USEREVENT + 1
        self.floor_move_event = pygame.USEREVENT + 2
        self.score_update = pygame.USEREVENT + 3
        self.new_game()


    def new_game(self):
        self.state = GameState()
        # Sprite groups
        self.player = pygame.sprite.GroupSingle()
        self.player_instance = Player()
        self.player.add(self.player_instance)
        self.background = pygame.sprite.Group()
        self.background.add(Background(0))
        self.floor = pygame.sprite.Group()
        self.floor.add(Floor(0))
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Drill())
        self.ui = pygame.sprite.Group()
        # Reset timers
        pygame.time.set_timer(self.background_move_event, 0)
        pygame.time.set_timer(self.floor_move_event, 0)
        pygame.time.set_timer(self.score_update, 0)

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

    def update_ui(self):
        self.state.next_state()
        self.ui.empty()

    def update(self):
        pygame.display.update()
        self.clock.tick(conf.FPS)
        if DEBUG:
            pygame.display.set_caption(f"{conf.GAME_TITLE}. Score: {self.player_instance.score}")
        else:
            pygame.display.set_caption(conf.GAME_TITLE)
        self.player.update()
        if self.player_instance.running:
            self.enemies.update()
        # ui
        if self.state.get_state() == "START":
            self.ui.add(StartMenu())
        if self.state.get_state() == "RUNNING":
            self.ui.add(RunningMenu())
            self.ui.update(self.player_instance.score)
        if self.state.get_state() == "END":
            pass


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            # GAME START
            if pygame.key.get_pressed()[pygame.K_SPACE] and not self.player_instance.running:
                # Activating timers
                pygame.time.set_timer(self.background_move_event, 200)
                pygame.time.set_timer(self.floor_move_event, 10)
                pygame.time.set_timer(self.score_update, 500)
                self.player_instance.running = True
                self.update_ui()
            if event.type == self.background_move_event and self.player_instance.running:
                self.move_background()
            if event.type == self.floor_move_event and self.player_instance.running:
                self.move_floor()
            if event.type == self.score_update and self.player_instance.running:
                self.update_score()
            if DEBUG:
                if pygame.key.get_pressed()[pygame.K_q]:
                    self.new_game()

    def draw(self):
        self.screen.fill(conf.COLOR_DARK)
        self.background.draw(self.screen)
        self.update_floor()
        self.floor.draw(self.screen)
        self.ui.draw(self.screen)
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--DEBUG":
            DEBUG = True
    game = Game()
    game.run()
