import pygame
from random import randrange, choice

pygame.init()

# PLAYER or CPU
GAME_MODE = "CPU"

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "purple"
SECOND_COLOR = "white"
FONT = pygame.font.SysFont(None, 30)
margin_height = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pypong")
clock = pygame.time.Clock()
FPS = 60

player1_score = 0
player2_score = 0
winner = 0
ball_moving = False


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self, key_up, key_down):
        key = pygame.key.get_pressed()
        if key[key_up] and self.rect.top > margin_height:
            self.rect.move_ip(0, -1 * self.speed)
        if key[key_down] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.speed)

    def ai(self):
        if self.rect.centery < ball.rect.top and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.speed)
        if self.rect.centery > ball.rect.top and self.rect.top > margin_height:
            self.rect.move_ip(0, -1 * self.speed)

    def draw(self):
        pygame.draw.rect(screen, SECOND_COLOR, self.rect)


class Ball:
    def __init__(self, x, y):
        self.reset(x, y)

    def draw(self):
        pygame.draw.circle(screen, SECOND_COLOR, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)

    def move(self):
        # collision detection
        if self.rect.top < margin_height or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.rect.left < 0:
            self.winner = -1
        if self.rect.right > SCREEN_WIDTH:
            self.winner = 1
        # check collision with paddles
        if self.rect.colliderect(player1_paddle) or self.rect.colliderect(player2_paddle):
            self.speed_x *= -1
            if self.speed_x > 0:
                self.speed_x += randrange(0, 2)
            if self.speed_x < 0:
                self.speed_x -= randrange(0, 2)
            if self.speed_y > 0:
                self.speed_y += randrange(0, 2)
            if self.speed_y < 0:
                self.speed_y -= randrange(0, 2)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.radius = 8
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.speed_x = choice([-3, 3])
        self.speed_y = choice([-3, 3])
        self.winner = 0


def draw_background():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, SECOND_COLOR, (0, margin_height), (SCREEN_WIDTH, margin_height), 5)


def draw_text(text, font, color, x, y):
    image = font.render(text, False, color)
    screen.blit(image, (x, y))


player1_paddle = Paddle(20, SCREEN_HEIGHT // 2)
player2_paddle = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2)

ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

is_running = True
while is_running:

    clock.tick(FPS)

    draw_background()
    draw_text(f"Player 1: {player1_score}", FONT, SECOND_COLOR, 20, 15)
    draw_text(f"Player 2: {player2_score}", FONT, SECOND_COLOR, SCREEN_WIDTH - 150, 15)

    player1_paddle.draw()
    player2_paddle.draw()

    if ball_moving:
        winner = ball.move()
        if winner == 0:
            player1_paddle.move(key_up=pygame.K_UP, key_down=pygame.K_DOWN)
            if GAME_MODE == "CPU":
                player2_paddle.speed = 3
                player2_paddle.ai()
            if GAME_MODE == "PLAYER":
                player2_paddle.move(key_up=pygame.K_w, key_down=pygame.K_s)
            ball.draw()
        else:
            ball_moving = False
            if winner == 1:
                player1_score += 1
            else:
                player2_score += 1

    if not ball_moving:
        if winner == 0:
            draw_text("PRESS SPACE TO START", FONT, SECOND_COLOR, SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 100)
        if winner != 0:
            draw_text(f"{'Player 1' if winner == 1 else 'Player 2'} scored!",
                      FONT, SECOND_COLOR, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
            draw_text("PRESS SPACE TO CONTINUE", FONT, SECOND_COLOR, SCREEN_WIDTH // 2 - 155, SCREEN_HEIGHT // 2 - 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            is_running = False
        if pygame.key.get_pressed()[pygame.K_SPACE] and not ball_moving:
            ball_moving = True
            ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)

    pygame.display.flip()

pygame.quit()
