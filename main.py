import pygame
import objects

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

field = objects.Field(1000, 700, 20)
field.draw_field(screen)

# for i in range(len(field)):
#     print(field[i][0].topleft)


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.dict["pos"]
            
            if (
                (
                    mouse_position[0] >= field.top_left_x 
                    and mouse_position[1] >= field.top_left_y
                )
                and
                (
                    mouse_position[0] < field.top_left_x + field.FIELD_WIDTH 
                    and mouse_position[1] < field.top_left_y + field.FIELD_HIGHT
                )
            ):  
                
                square_position = field.get_square_array_position(mouse_position)
                
                field.field_of_tiles[square_position[0]][square_position[1]] \
                    = objects.Road(
                        screen,
                        (
                            int(
                                square_position[0] * field.SQUARE_DIMENSIONS + field.top_left_x
                            ),
                            int(
                                square_position[1] * field.SQUARE_DIMENSIONS + field.top_left_y
                            )
                        ),
                        field.SQUARE_DIMENSIONS,
                        field.SQUARE_DIMENSIONS,
                    )

            
            
            
    if pygame.mouse.get_pressed()[0]:
        ...
        
        

    
    pygame.display.flip()

pygame.quit()