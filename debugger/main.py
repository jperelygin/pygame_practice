from debugger.dbg import *
from debugger.dbg import Debugger

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
cat = pygame.image.load("cat.png").convert_alpha()
font = pygame.font.Font(None, 30)
fps = 60


dbg = Debugger(font)
running = True
debug_mode = -1
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_F12]:
            debug_mode *= -1

    screen.fill('white')
    screen.blit(cat, (150, 20))

    if debug_mode == 1:
        draw_tiles(40)
        dbg.add_message("mouse_position", pygame.mouse.get_pos())
        dbg.add_message("space_key_pressed", pygame.key.get_pressed()[pygame.K_SPACE])
        dbg.print()

    pygame.display.update()

pygame.quit()
