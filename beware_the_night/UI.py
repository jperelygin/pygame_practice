import pygame
import conf


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


class EndMenu(pygame.sprite.Sprite):
    def __init__(self, score):
        super().__init__()
        self.font = pygame.font.Font(conf.FONT, conf.START_SCREEN_TEXT_SIZE)
        self.image = self.font.render(f"You are dead. Your score is: {score}", False, conf.COLOR_BLACK)
        self.rect = self.image.get_rect(midbottom=conf.END_SCREEN_TEXT_POSITION)
