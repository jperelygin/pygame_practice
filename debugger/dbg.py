import pygame

class Debugger:
    def __init__(self, font: pygame.font.Font, x=20, text_color='green', bg_color='black'):
        self.messages = {}
        self.font = font
        self.x = x
        self.text_color = text_color
        self.bg_color = bg_color

    def add_message(self, title, value):
        self.messages[title] = str(value)

    def remove_message(self, title):
        self.messages.pop(title)

    def print(self):
        display = pygame.display.get_surface()
        y = 10
        for i in self.messages:
            surface = self.font.render(f"{i}: {self.messages[i]}", False, self.text_color, self.bg_color)
            rect = surface.get_rect(topleft=(self.x, y))
            y += surface.get_size()[1]
            display.blit(surface, rect)
