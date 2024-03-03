import random

import pygame
import sys

import conf
from Player import Player
from Background import Background
from Floor import Floor
from Enemy import Fly, OneEye, Drill, Slime, Bat
from UI import StartMenu, RunningMenu, EndMenu
from GameState import GameState
from Decorations import Grass, House

DEBUG = False
DEATH = False

ENEMY_CLASSES = (Fly, OneEye, Drill, Slime, Bat)
# ENEMY_CLASSES = (Fly, )

DECOR_CLASSES = (Grass, House)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(conf.RES)
        self.clock = pygame.time.Clock()
        # events (timers)
        self.background_move_event = pygame.USEREVENT + 1
        self.floor_move_event = pygame.USEREVENT + 2
        self.score_update = pygame.USEREVENT + 3
        self.spawn_timer = pygame.USEREVENT + 4
        self.crouch_timer = pygame.USEREVENT + 5
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
        self.ui = pygame.sprite.Group()
        self.decorations = pygame.sprite.Group()
        # Reset timers
        pygame.time.set_timer(self.background_move_event, 0)
        pygame.time.set_timer(self.floor_move_event, 0)
        pygame.time.set_timer(self.score_update, 0)
        pygame.time.set_timer(self.spawn_timer, 0)
        pygame.time.set_timer(self.crouch_timer, 0)
        # Music stop
        pygame.mixer_music.stop()

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

    def spawn_enemies(self):
        # not more than 2 on screen
        if len(self.enemies.sprites()) < 2:
            self.enemies.add(random.choice(ENEMY_CLASSES)(
                random.randint(conf.ENEMY_POSITION_X_1, conf.ENEMY_POSITION_X_2)))
        # remove skipped enemies
        for enemy in self.enemies.sprites():
            if enemy.rect.midright[0] < -20:
                self.enemies.remove(enemy)

    def spawn_decor(self):
        if len(self.decorations.sprites()) < 1:
            self.decorations.add(random.choice(DECOR_CLASSES)())
            print("Decor added!")
        for decor in self.decorations.sprites():
            if decor.rect.midright[0] < -100:
                self.decorations.remove(decor)

    def update(self):
        pygame.display.update()
        self.clock.tick(conf.FPS)
        pygame.display.set_caption(conf.GAME_TITLE)
        self.player.update()
        # switch game states
        match self.state.get_state():
            case "START":
                self.ui.add(StartMenu())
            case "RUNNING":
                self.ui.empty()
                self.ui.add(RunningMenu())
                self.ui.update(self.player_instance.score)
                self.enemies.update()
                if DEATH:
                    for enemy in self.enemies.sprites():
                        if (enemy.collider_rect.collidepoint(self.player_instance.rect.midright)
                                or enemy.collider_rect.collidepoint(self.player_instance.rect.midbottom)
                                or enemy.collider_rect.collidepoint(self.player_instance.rect.midtop)):
                            self.state.next_state()
                self.spawn_decor()
                self.decorations.update()
            case "END":
                self.ui.empty()
                self.player_instance.damage()
                self.ui.add(EndMenu(self.player_instance.score))
                pygame.mixer_music.stop()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            # GAME START
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.state.get_state() == "START":
                # Activating timers
                pygame.time.set_timer(self.background_move_event, 200)
                pygame.time.set_timer(self.floor_move_event, 10)
                pygame.time.set_timer(self.score_update, 500)
                pygame.time.set_timer(self.spawn_timer, 1500)
                self.player_instance.is_running = True
                self.state.next_state()
                # Music start
                pygame.mixer_music.load(conf.main_music)
                pygame.mixer_music.play()
                pygame.mixer_music.set_volume(.02)
            if event.type == self.background_move_event and self.state.get_state() == "RUNNING":
                self.move_background()
            if event.type == self.floor_move_event and self.state.get_state() == "RUNNING":
                self.move_floor()
            if event.type == self.score_update and self.state.get_state() == "RUNNING":
                self.update_score()
            if event.type == self.spawn_timer and self.state.get_state() == "RUNNING":
                self.spawn_enemies()
            if (pygame.key.get_pressed()[pygame.K_s] and not self.player_instance.is_crouching
                    and self.state.get_state() == "RUNNING"):
                pygame.time.set_timer(self.crouch_timer, 800)
                self.player_instance.crouch()
            if event.type == self.crouch_timer and self.state.get_state() == "RUNNING":
                self.player_instance.is_crouching = False
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.state.get_state() == "END":
                self.new_game()

            if DEBUG:
                if pygame.key.get_pressed()[pygame.K_q]:
                    self.new_game()

    def draw(self):
        self.screen.fill(conf.COLOR_DARK)
        self.background.draw(self.screen)
        self.update_floor()
        self.floor.draw(self.screen)
        self.decorations.draw(self.screen)
        self.ui.draw(self.screen)
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        if DEBUG:
            player_coll_rect = self.player_instance.rect.copy()
            pygame.draw.rect(self.screen, "cyan", player_coll_rect, 2)
            for enemy in self.enemies.sprites():
                coll_rect = enemy.collider_rect.copy()
                pygame.draw.rect(self.screen, "pink", coll_rect, 2)

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
