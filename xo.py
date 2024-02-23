import pygame

SCREEN_RESOLUTION = (640, 480)

WINNING_CONDITIONS = (
    [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
)

pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()
running = True

board = [[], [], []]
x_player = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
o_player = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

rectangles = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    start_pointer = (0, 0)
    for i in range(3):
        for j in range(3):
            r = pygame.draw.rect(screen,
                                 "purple",
                                 pygame.Rect(start_pointer,
                                             (SCREEN_RESOLUTION[0] / 3 - 1, SCREEN_RESOLUTION[1] / 3 - 1)))
            if r not in board:
                board[i][j] = r
            start_pointer = (start_pointer[0] + SCREEN_RESOLUTION[0] / 3 + 1, start_pointer[1])
        start_pointer = (0, start_pointer[1] + SCREEN_RESOLUTION[1] / 3 + 1)

    pygame.display.flip()
    clock.tick(60)

print(board)
pygame.quit()
