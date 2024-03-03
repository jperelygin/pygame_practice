import pygame


class SpritesheetParser:
    def __init__(self):
        self.tile_size = ()
        self.scale_tile_size = self.tile_size
        self.sprite_sheet = ""

    def get_sprite(self, row: int, table: int, scale=False):
        sheet = pygame.image.load(self.sprite_sheet)
        if scale:
            sheet.set_clip(pygame.Rect(self.scale_tile_size[0] * table, self.scale_tile_size[1] * row,
                                       self.scale_tile_size[0], self.scale_tile_size[1]))
        return sheet.subsurface(sheet.get_clip())

    def get_collision_rect(self, image: pygame.surface.Surface, transparent_color):
        size = image.get_size()
        x_left = 0
        x_size = size[0]
        y_top = 0
        y_size = size[1]
        for x in range(size[0]):
            for y in range(size[1]):
                if image.get_at((x, y)) != transparent_color:
                    x_left = x
        for y in range(size[1]):
            for x in range(size[0]):
                if image.get_at((x, y)) != transparent_color:
                    y_top = y
        for x in range(size[0], 0, -1):
            for y in range(size[1], 0, -1):
                if image.get_at((x, y)) != transparent_color:
                    x_size = x - x_left
        for y in range(size[1], 0, -1):
            for x in range(size[0], 0, -1):
                if image.get_at((x, y)) != transparent_color:
                    y_size = y - y_top
        return pygame.Rect((x_left, y_top), (x_size, y_size))


def get_sprite(sprite_sheet: str, tiles: tuple, row: int, table: int) -> pygame.Surface:
    sheet = pygame.image.load(sprite_sheet)
    sheet.set_clip(pygame.Rect(tiles[0] * table, tiles[1] * row, tiles[0], tiles[1]))
    return sheet.subsurface(sheet.get_clip())
