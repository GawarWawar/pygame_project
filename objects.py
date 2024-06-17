import pygame

class Tile(pygame.Rect):
    
    @classmethod    
    def get_subclusses(self):
            return [cls.__name__ for cls in self.__subclasses__()]
    
    @classmethod
    def transform (self, new_cls):
        self = globals()[new_cls]
        return self
        
class Road(Tile):
    ...    
class Tower(Tile):
    ...

if __name__ == "__main__":
    new_tile = Tile(0, 0, 10, 10)
    new_tile = new_tile.transform(Tile.get_subclusses()[0])
    print(new_tile.__name__)