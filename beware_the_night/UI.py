import pygame
import conf


class GameState:
    def __init__(self):
        self.states = ["START", "RUNNING", "END"]
        self.state = 0

    def next_state(self):
        self.state += 1
        if self.state >= len(self.states):
            self.state = 0

    def get_state(self):
        return self.states[self.state]


class StartMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(conf.FONT, conf.START_SCREEN_TEXT_SIZE)
        self.image = self.font.render(conf.START_SCREEN_TEXT, False, conf.COLOR_BLACK)
        self.rect = self.image.get_rect(midbottom=conf.START_SCREEN_TEXT_POSITION)


class RunningMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(conf.FONT, conf.SCORE_TEXT_SIZE)
        self.image = self.font.render(f"Score: 000000000", False, conf.COLOR_BLACK)
        self.rect = self.image.get_rect(topright=conf.SCORE_TEXT_POSITION)

    def update(self, score):
        self.image = self.font.render(f"Score: {score:09d}", False, conf.COLOR_BLACK)
