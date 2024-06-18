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
                field[int(x / self.SQUARE_DIMENSIONS)].append(
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
            

class Tile():
    fill_colour = (170, 170, 170)
    border_size = 1
    
    def __init__(
        self, 
        screen: pygame.Surface,
        coordinates: tuple,
        width: int,
        height: int
    ):
        self.screen = screen
        self.body = pygame.draw.rect(
            screen, 
            self.fill_colour, 
            pygame.Rect(
                coordinates[0],
                coordinates[1],
                width, 
                height
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
    
    def set_screen_colour(self):
        self.fill_colour = self.screen.get_colorkey()
        self.__init__(
            self.screen,
            self.body.topleft,
            self.body.width,
            self.body.height
        )
        
class Road(Tile):
    border_size = 100
    ... 
    
       
class Base(Road):
    fill_colour = (0, 139, 139)
    border_size = 100
    
class Entrance(Road):
    fill_colour = (255, 255, 255)
    border_size = 100

class TowerFundament (Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100

if __name__ == "__main__":
    new_tile = Tile(0, 0, 10, 10)
    new_tile = new_tile.transform(Tile.get_subclusses()[0])
    print(new_tile.__name__)