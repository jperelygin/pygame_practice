import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
text1 = "You loose!"
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
fps = 30


def get_text(freq):
    list_letters = []
    text_surf = font.render(text1, False, "black")
    text_rect = text_surf.get_rect(center=(250, 250))
    start = text_rect.midleft
    increment = 0
    # remove add frequency instead of i
    for i, letter in enumerate(text1):
        letter_surf = font.render(letter, False, "black")
        letter_rect = letter_surf.get_rect(midleft=(start[0] + increment, 250 + freq * i * 2))
        print(letter_rect)
        increment += font.size(letter)[0]
        list_letters.append([letter_surf, letter_rect])
    return list_letters


def wobble_text(letters):
    global directions
    center = 250
    for index, i in enumerate(letters):
        y_now = i[1].centery
        if y_now > center + 17 or y_now < center - 17:
            directions[index] *= -1
            print(directions)
        i[1].centery += directions[index]
        screen.blit(i[0], i[1])


letters = get_text(1)
directions = [1 for _ in range(len(text1))]
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    wobble_text(letters)
    pygame.display.update()

pygame.quit()
