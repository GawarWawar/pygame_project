import pathlib
import pygame

import entities.basic_tiles as basic_tiles
import entities.enemies as enemies

class TurretRange (basic_tiles.Tile):
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/TowerRange.png")
    foes_in_range : list [enemies.Enemy]= []
    
    
    def detect (
        self, 
        foes: list[enemies.Enemy]
    ):
        for foe in foes:
            if self.rect.colliderect(foe.rect):
                self.foes_in_range.add(foe)
            else:
                foe.remove(self.foes_in_range)

class Projectile (basic_tiles.Tile):
    target: enemies.Enemy|None  = None
    
    
    # _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
    
    def __init__(
        self, 
        coordinates: tuple, 
        width: int, 
        height: int, 
        image_path: str,
        projectile_speed: int,
    )-> None:
        self._image_path = image_path 
        self.speed = projectile_speed
        
        super().__init__(coordinates, width, height)    
        
    def attack(self):
        coordinates = self.target.rect.center
        coordinates = (
            (coordinates[0] - self.rect.x) * self.speed, 
            (coordinates[1] - self.rect.y) * self.speed
        )
        self.rect.move(**coordinates)
        


class TowerFundament (basic_tiles.Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
class Tower (TowerFundament):
    damage = 0
    attack_speed = 0
    attack_range = 0
    
    projectile_speed = 0
    
    projectiles = []
    
    projectile_width = 0
    projectile_height = 0
    _projectile_image_path = "" 
    
    def __init__(self, coordinates: tuple, width: int, height: int) -> None:
        self.range = TurretRange(
            coordinates, 
            self.attack_range/2,
            self.attack_range/2
        )
        self.range.rect = self.range.rect.move(
            coordinates[0] - self.range.rect.center[0] + width/2, 
            coordinates[1] - self.range.rect.center[1] + height/2, 
        )
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
    attack_range = 500
    
    _projectile_image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")
    
    
    
    fill_colour = (0, 150, 0)
    border_size = 100
    draw_function = pygame.draw.circle
    corner_radius = (20, 20, 20, 20)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")