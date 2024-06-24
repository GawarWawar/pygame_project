import pathlib
import pygame

  
class Tile():
    fill_colour = (170, 170, 170)
    border_size = 1
    corner_radius = (-1, -1, -1, -1) #top_left, top_right, bottom_left, bottom_right
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tile.png")
    
    def __init__(
        self,
        coordinates: tuple,
        width: int,
        height: int,
    ) -> None:
        # TODO: It is needed for better precision and I need to make all movement work through this stuff coordinates
        self.coordinates = coordinates
        
        # TODO: Look at this and decide if this properties are needed
        self.width = width
        self.height = height
        
        # Upload image
        self.image = pygame.image.load(self._image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        
        # Assign rect to property
        self.rect = self.image.get_rect()
        
        # Change the start coordinates
        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
        
    def draw(
        self, 
        screen: pygame.Surface,
    ):
        screen.blit(
            self.image,
            self.rect,
        )
    
    # TODO: REWORK OR DELETE
    def set_screen_colour(self, screen):
        self.fill_colour = screen.get_colorkey()
        self.__init__(
            screen,
            self.rect.topleft,
            self.rect.width,
            self.rect.height
        )
    
    @classmethod    
    def get_subclusses(self):
        return [cls.__name__ for cls in self.__subclasses__()]
    
    @classmethod
    def transform (self, new_cls):
        self = globals()[new_cls]
        return self
    
  
        
class Road(Tile):
    border_size = 100
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/True_road.png")
    
class Base(Road):
    fill_colour = (0, 139, 139)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Base.png")
    
    
class Entrance(Road):
    fill_colour = (255, 255, 255)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Entance.png")


