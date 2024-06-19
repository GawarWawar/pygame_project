import pygame
import entities.basic_tiles as basic_tiles
import entities.map_building as map_building
import entities.enemies as enemies 

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

field = map_building.Field(600, 440, 40)
field.draw_field(screen)

# Draw a map example
entrances :list[tuple[int, int]] = []
bases :list[tuple[int, int]] = []
for i in range(len(field.field_of_tiles)):
    if i == 0:
        tile_type = basic_tiles.Entrance
    elif i != len(field.field_of_tiles)-1:
        tile_type = basic_tiles.Road
    else:
        tile_type = basic_tiles.Base
        
    tile_coordinates = field.field_of_tiles[i][5].rect.topleft
    field.field_of_tiles[i][5] = tile_type(
        tile_coordinates,
        field.SQUARE_DIMENSIONS,
        field.SQUARE_DIMENSIONS,
    )
    field.field_of_tiles[i][5].draw(screen)
    
    if tile_type == basic_tiles.Entrance:
        entrances.append((i, 5))
    if tile_type == basic_tiles.Base:
        bases.append((i, 5))

# for i in range(len(field)):
#     print(field[i][0].topleft)

# Stating conditionals
ENEMY_WAVE = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_WAVE, 2000)

foes : list[enemies.Enemy] = []

# Main game loop
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == ENEMY_WAVE:
            for i in range(1):
                foe_coordinates = field.field_of_tiles[entrances[0][0]][entrances[0][1]].rect.center
                print(foe_coordinates)
                foe_to_append = (
                    enemies.Enemy(
                        foe_coordinates,
                        field.SQUARE_DIMENSIONS/5,
                        field.SQUARE_DIMENSIONS/5
                    )
                )
                foe_to_append.draw(screen)
                print(foe_to_append.rect.topleft)
                foes.append(foe_to_append)
        
        #player actions
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.dict["pos"]
            
            if (
                field.is_in_field(mouse_position)
            ):  
                
                tile_arr_pos = field.get_square_array_position(mouse_position)
                tile_coordinates = field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]].rect.topleft
                    
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
                                tile_coordinates,
                                field.SQUARE_DIMENSIONS,
                                field.SQUARE_DIMENSIONS,
                            )
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]].draw(screen) 
                    else:
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]] \
                            = basic_tiles.TowerFundament(
                                tile_coordinates,
                                field.SQUARE_DIMENSIONS,
                                field.SQUARE_DIMENSIONS,
                            )
                        field.field_of_tiles[tile_arr_pos[0]][tile_arr_pos[1]].draw(screen)
        
    for row in field.field_of_tiles:
        for tile in row: 
            tile.draw(screen)    
        
    for foe_arr_pos, foe in enumerate(foes):
        foes[foe_arr_pos].rect = foe.rect.move(foe.speed, 0)      
        pygame.draw.rect(screen, foes[foe_arr_pos].fill_colour, foes[foe_arr_pos].rect)
        if foe.rect.colliderect(
            field.field_of_tiles[bases[0][0]][bases[0][1]].rect
        ):
            foes.pop(foe_arr_pos)
            
            
    if pygame.mouse.get_pressed()[0]:
        ...
        
        

    
    pygame.display.flip()

pygame.quit()