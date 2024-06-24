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
                self.foes_in_range.append(foe)
            else:
                if foe in self.foes_in_range:
                    self.foes_in_range.pop(self.foes_in_range.index(foe))

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
        target_coordinates = self.target.rect.center
        
        # TODO: move unit vector creation to separate function
        direction_vector = (target_coordinates[0] - self.rect.x, target_coordinates[1] - self.rect.y)
        magnitude_of_direction_vector = (
            direction_vector[0]**2 + 
            direction_vector[1]**2
        )**0.5
        if magnitude_of_direction_vector != 0:
            unit_vector = (
                direction_vector[0]/magnitude_of_direction_vector,
                direction_vector[1]/magnitude_of_direction_vector
            )
            movement = (
                self.speed * unit_vector[0],
                self.speed * unit_vector[1]
            )

            self.coordinates = (self.coordinates[0] + movement[0], self.coordinates[1] + movement[1])
            self.rect = self.rect.move_to(x = self.coordinates[0], y = self.coordinates[1])
        


class TowerFundament (basic_tiles.Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
class Tower (TowerFundament):
    damage = 0
    attack_range = 0
    
    projectile_speed = 0
    
    attack_speed = 0
    _attack_cd = 0
    
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
            self._projectile_image_path,
            self.projectile_speed
        )
        proj.target = target
        self.projectiles.append(proj)

    def cool_down(self) -> bool:
        # TODO: CHANGE FPS FROM 60 TO CONSTANT
        if pygame.time.get_ticks() - self._attack_cd > self.attack_speed * 1000: # -> HERE SHOULD BE FPS
            return True
        return False
        
    def attack(self):
        enemy_position = 0
        if len(self.range.foes_in_range) > 0 and self.cool_down():
            #BUG: Fires always in the first seen enemy, even when enemy is out of range
            self.fire_projectile(
                self.range.foes_in_range[enemy_position]
            )
            ticks = pygame.time.get_ticks()
            self._attack_cd = ticks
            
        ...

class BasicTower (Tower):
    attack_speed = 1

    projectile_width = 10
    projectile_height = 10
    projectile_speed = 2
    _projectile_image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")
    
    attack_range = 500    
    
    fill_colour = (0, 150, 0)
    border_size = 100
    draw_function = pygame.draw.circle
    corner_radius = (20, 20, 20, 20)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")