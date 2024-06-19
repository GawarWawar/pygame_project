import pygame
import entities.basic_tiles as basic_tiles

class Field():
    def __init__(
        self, 
        FIELD_WIDTH = 1000, 
        FIELD_HIGHT = 700, 
        SQUARE_DIMENSIONS = 20
    ) -> None:
        self.FIELD_WIDTH = FIELD_WIDTH
        self.FIELD_HIGHT = FIELD_HIGHT
        self.SQUARE_DIMENSIONS = SQUARE_DIMENSIONS
        
        self.field_of_tiles = []

    def draw_field(self, screen):
        field : list[list[basic_tiles.Tile]] = []

        for x in range(
            0,
            self.FIELD_WIDTH, 
            self.SQUARE_DIMENSIONS
        ):    
            field.append([])
            for y in range(
                0,
                self.FIELD_HIGHT,
                self.SQUARE_DIMENSIONS
            ):
                tile_to_add = basic_tiles.Tile(
                        (
                            int((screen.get_width() - self.FIELD_WIDTH) / 2 + x), 
                            int((screen.get_height() - self.FIELD_HIGHT) / 2 + y) 
                        ),
                        self.SQUARE_DIMENSIONS,
                        self.SQUARE_DIMENSIONS
                    )  
                tile_to_add.update(screen)
                field[int(x / self.SQUARE_DIMENSIONS)].append(
                    tile_to_add
                )
            
            self.top_left = (
                int((screen.get_width() - self.FIELD_WIDTH) / 2), # x
                int((screen.get_height() - self.FIELD_HIGHT) / 2) # y
            )
            
            
            self.field_of_tiles = field
            
    def get_square_array_position(self, mouse_position):
        if len(self.field_of_tiles) == 0:
            raise AttributeError("Need to add tiles to the field first")
        return (
            int((mouse_position[0] - self.top_left[0]) / self.SQUARE_DIMENSIONS),
            int((mouse_position[1] - self.top_left[1]) / self.SQUARE_DIMENSIONS)
        )
        
    def is_in_field(self, mouse_position):   
        if(
            (
                mouse_position[0] >= self.top_left[0]
                and mouse_position[1] >= self.top_left[1]
            )
            and
            (
                mouse_position[0] < self.top_left[0] + self.FIELD_WIDTH 
                and mouse_position[1] < self.top_left[1] + self.FIELD_HIGHT
            )
        ):
            return True
        else:
            return False
        ...
            