import pathlib
import pygame
import entities.basic_tiles as basic_tiles

class Enemy(basic_tiles.Tile):
    
    
    def __init__(
        self,
        coordinates,
        width,
        height,
        _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png"),
        
        
        health_points = 100,
        speed = 3,
        
    ) -> None:
        self.health_points = health_points
        self.speed = speed
        self._image_path = _image_path

        super().__init__(coordinates, width, height)
        