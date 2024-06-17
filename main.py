import pygame

pygame.init()
WIDTH = 1280
HIGHT = 720

screen = pygame.display.set_mode((WIDTH, HIGHT))
clock = pygame.time.Clock()
running = True
dt = 0


# lines = [[], []]
# for i in range(0, int(screen.get_width()), 20):
#     lines[0].append(pygame.draw.line(screen, "white", pygame.Vector2(i, 0), pygame.Vector2(i, screen.get_height())))
# for j in range(0, int(screen.get_height()), 20):
#     lines[1].append(pygame.draw.line(screen, "white", pygame.Vector2(0, j), pygame.Vector2(screen.get_width(), j)))

FIELD_WIDTH = 100
FIELD_HIGHT = 70
SQUARE_DIMENSIONS = 20

field = []
for i in range(
    0,
    FIELD_WIDTH, 
    SQUARE_DIMENSIONS
):    
    field.append([])
    for j in range(
        0,
        FIELD_HIGHT,
        SQUARE_DIMENSIONS
    ):
        field[int(i / SQUARE_DIMENSIONS)].append(
            pygame.draw.rect(
                screen, 
                (170, 170, 170), 
                (
                    int((screen.get_width() - FIELD_WIDTH) / 2 + i), 
                    int((screen.get_height() - FIELD_HIGHT) / 2 + j), 
                    SQUARE_DIMENSIONS, 
                    SQUARE_DIMENSIONS), 
                1
            )
        )


    
  


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()

pygame.quit()