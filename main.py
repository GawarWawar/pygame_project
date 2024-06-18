import pygame
import entities.basic_tiles as basic_tiles

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

field = basic_tiles.Field(300, 220, 20)
field.draw_field(screen)

#draw a map
for i in range(len(field.field_of_tiles)):
    if i == 0:
        tile_type = basic_tiles.Entrance
    elif i != len(field.field_of_tiles)-1:
        tile_type = basic_tiles.Road
    else:
        tile_type = basic_tiles.Base
        
    tile_coordinates = field.field_of_tiles[i][5].body.topleft
    field.field_of_tiles[i][5] = tile_type(
                        screen,
                        tile_coordinates,
                        field.SQUARE_DIMENSIONS,
                        field.SQUARE_DIMENSIONS,
                    )

# for i in range(len(field)):
#     print(field[i][0].topleft)


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #player actions
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.dict["pos"]
            
            if (
                field.is_in_field(mouse_position)
            ):  
                
                tile_arr_pos = field.get_square_array_position(mouse_position)
                tile_coordinates = field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]].body.topleft
                
                    
                print(isinstance(
                    field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]],
                    basic_tiles.TowerFundament
                ))
                
                if not isinstance(
                    field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]],
                    basic_tiles.Road
                ):
                    if isinstance(
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]],
                        basic_tiles.TowerFundament
                    ):
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]] \
                            = basic_tiles.BasicTower(
                                screen,
                                tile_coordinates,
                                field.SQUARE_DIMENSIONS,
                                field.SQUARE_DIMENSIONS,
                            )
                    else:
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]] \
                            = basic_tiles.TowerFundament(
                                screen,
                                tile_coordinates,
                                field.SQUARE_DIMENSIONS,
                                field.SQUARE_DIMENSIONS,
                            )
                    
        
            
            
            
    if pygame.mouse.get_pressed()[0]:
        ...
        
        

    
    pygame.display.flip()

pygame.quit()