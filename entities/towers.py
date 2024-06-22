import pathlib
import pygame

import entities.basic_tiles as basic_tiles

class Projectile (basic_tiles.Tile):
    target = None
    
    
    # _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
    
    def __init__(
        self, 
        coordinates: tuple, 
        width: int, 
        height: int, 
        image_path: str,
    )-> None:
        self._image_path = image_path 
        
        super().__init__(coordinates, width, height)    
    

class TowerFundament (basic_tiles.Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
class Tower (TowerFundament):
    damage = 0
    attack_speed = 0
    
    projectiles = []
    
    projectile_width = 0
    projectile_height = 0
    _projectile_image_path = "" 
    
    def __init__(self, coordinates: tuple, width: int, height: int) -> None:

        
        super().__init__(coordinates, width, height)
    
    def fire_projectile(self, target):
        proj = Projectile(
            self.rect.center, 
            self.projectile_width, 
            self.projectile_height, 
            self._projectile_image_path
        )
        proj.target = target
        self.projectiles.append(proj)
        
    
    def attack(self, target):

        ...

class BasicTower (Tower):

    projectile_width = 2
    projectile_height = 2
    _projectile_image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")
    
    
    
    fill_colour = (0, 150, 0)
    border_size = 100
    draw_function = pygame.draw.circle
    corner_radius = (20, 20, 20, 20)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")