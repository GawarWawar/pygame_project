import pygame
  
class Tile():
    fill_colour = (170, 170, 170)
    border_size = 1
    corner_radius = (-1, -1, -1, -1) #top_left, top_right, bottom_left, bottom_right
    
    def __init__(
        self, 
        screen: pygame.Surface,
        coordinates: tuple,
        width: int,
        height: int,
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
            self.border_size,
            self.corner_radius[0],
            self.corner_radius[1],
            self.corner_radius[2],
            self.corner_radius[3],
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
    
class Entrance(Road):
    fill_colour = (255, 255, 255)



class TowerFundament (Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100
    
class Tower (TowerFundament):
    ...

class BasicTower (Tower):
    fill_colour = (0, 150, 0)
    border_size = 100
    draw_function = pygame.draw.circle