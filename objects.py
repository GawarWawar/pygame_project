import pygame

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
        field : list[list[Tile]] = []
        for y in range(
            0,
            self.FIELD_HIGHT, 
            self.SQUARE_DIMENSIONS
        ):    
            field.append([])

        for x in range(
            0,
            self.FIELD_WIDTH, 
            self.SQUARE_DIMENSIONS
        ):    
            for y in range(
                0,
                self.FIELD_HIGHT,
                self.SQUARE_DIMENSIONS
            ):
                field[int(y / self.SQUARE_DIMENSIONS)].append(
                    Tile(
                        screen,
                        (
                            int((screen.get_width() - self.FIELD_WIDTH) / 2 + x), 
                            int((screen.get_height() - self.FIELD_HIGHT) / 2 + y) 
                        ),
                        self.SQUARE_DIMENSIONS,
                        self.SQUARE_DIMENSIONS
                    )
                )
            
            self.top_left_x = int((screen.get_width() - self.FIELD_WIDTH) / 2)
            self.top_left_y = int((screen.get_height() - self.FIELD_HIGHT) / 2)
            
            
            self.field_of_tiles = field
            
            

class Tile(pygame.Rect):
    fill_colour = (170, 170, 170)
    border_size = 1
    
    def __init__(
        self, 
        screen: pygame.Surface,
        coordinates: tuple,
        width: int,
        hight: int
    ):
        self.screen = screen
        self.body = pygame.draw.rect(
            screen, 
            self.fill_colour, 
            pygame.Rect(
                coordinates[0],
                coordinates[1],
                width, 
                hight
            ), 
            self.border_size
        )
    
    
    @classmethod    
    def get_subclusses(self):
            return [cls.__name__ for cls in self.__subclasses__()]
    
    @classmethod
    def transform (self, new_cls):
        self = globals()[new_cls]
        return self
        
class Road(Tile):
    fill_colour = (200, 0, 0)
    border_size = 100
    ... 
    
       
class Tower(Tile):
    ...

if __name__ == "__main__":
    new_tile = Tile(0, 0, 10, 10)
    new_tile = new_tile.transform(Tile.get_subclusses()[0])
    print(new_tile.__name__)