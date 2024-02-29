import pygame


def get_sprite(sprite_sheet: str, tiles: tuple, row: int, table: int) -> pygame.Surface:
    sheet = pygame.image.load(sprite_sheet)
    sheet.set_clip(pygame.Rect(tiles[0] * table, tiles[1] * row, tiles[0], tiles[1]))
    return sheet.subsurface(sheet.get_clip())
