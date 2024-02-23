import pygame

pygame.init()

# Has to be square
SCREEN_RESOLUTION = (600, 600)
BACKGROUND_COLOR = (200, 200, 200)
GRID_COLOR = (50, 50, 50)
GRID_LINE_WIDTH = 6
CELL_BORDER = SCREEN_RESOLUTION[0] // 3
MARKS_WIDTH = 12
FONT = pygame.font.SysFont(None, 40)

screen = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption("Tictaktoe")

clicked = False

again_button_rect = pygame.Rect((SCREEN_RESOLUTION[0]//2 - 85, SCREEN_RESOLUTION[1]//2, 160, 50))


class Game:
    def __init__(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.pos = ()
        self.player = 1
        self.winner = 0

    def restart(self):
        self.__init__()

    def winner_check(self):
        board_y = 0
        for x in self.board:
            if sum(x) == 3:
                self.winner = 1
            if sum(x) == -3:
                self.winner = -1
            if self.board[0][board_y] + self.board[1][board_y] + self.board[2][board_y] == 3:
                self.winner = 1
            if self.board[0][board_y] + self.board[1][board_y] + self.board[2][board_y] == -3:
                self.winner = -1
            board_y += 1
        if (self.board[0][0] + self.board[1][1] + self.board[2][2] == 3
                or self.board[2][0] + self.board[1][1] + self.board[0][2] == 3):
            self.winner = 1
        if (self.board[0][0] + self.board[1][1] + self.board[2][2] == -3
                or self.board[2][0] + self.board[1][1] + self.board[0][2] == -3):
            self.winner = -1


def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for x in range(1, 3):
        pygame.draw.line(screen, GRID_COLOR, (0, x * CELL_BORDER),
                         (SCREEN_RESOLUTION[0], x * CELL_BORDER), GRID_LINE_WIDTH)
        pygame.draw.line(screen, GRID_COLOR, (x * CELL_BORDER, 0)
                         , (x * CELL_BORDER, SCREEN_RESOLUTION[1]), GRID_LINE_WIDTH)


def draw_board(g: Game):
    board_x = 0
    for x in g.board:
        board_y = 0
        for y in x:
            # CROSS
            if y == 1:
                pygame.draw.line(screen, "green",
                                 (board_x * CELL_BORDER + 15, board_y * CELL_BORDER + 15),
                                 (board_x * CELL_BORDER + CELL_BORDER - 15, board_y * CELL_BORDER + CELL_BORDER - 15),
                                 MARKS_WIDTH)
                pygame.draw.line(screen, "green",
                                 (board_x * CELL_BORDER + 15, board_y * CELL_BORDER + CELL_BORDER - 15),
                                 (board_x * CELL_BORDER + CELL_BORDER - 15, board_y * CELL_BORDER + 15),
                                 MARKS_WIDTH)
            # CIRCLE
            if y == -1:
                pygame.draw.circle(screen, "red", (board_x * CELL_BORDER + CELL_BORDER / 2,
                                                   board_y * CELL_BORDER + CELL_BORDER / 2),
                                   int(CELL_BORDER / 2.5), MARKS_WIDTH)
            board_y += 1
        board_x += 1


def draw_winner(g: Game):
    text_color = "green" if g.winner == 1 else "red"
    win_text = f"Player {1 if g.winner == 1 else 2} wins!"
    win_text_img = FONT.render(win_text, True, text_color)
    retry_text = "Retry?"
    retry_text_img = FONT.render(retry_text, True, text_color)

    pygame.draw.rect(screen, "blue", (SCREEN_RESOLUTION[0]//2 - 100, SCREEN_RESOLUTION[1]//2 - 60, 200, 50))
    pygame.draw.rect(screen, "blue", again_button_rect)
    screen.blit(win_text_img, (SCREEN_RESOLUTION[0]//2 - 95, SCREEN_RESOLUTION[1] // 2 - 50))
    screen.blit(retry_text_img, (SCREEN_RESOLUTION[0]//2 - 50, SCREEN_RESOLUTION[1] // 2 + 10))


is_running = True
game = Game()
while is_running:

    draw_grid()
    draw_board(game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if game.winner == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                if game.board[pos_x // CELL_BORDER][pos_y // CELL_BORDER] == 0:
                    game.board[pos_x // CELL_BORDER][pos_y // CELL_BORDER] = game.player
                    game.player *= -1
                    game.winner_check()

    if game.winner != 0:
        draw_winner(game)
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_button_rect.collidepoint(pos):
                game.restart()

    pygame.display.flip()

pygame.quit()
