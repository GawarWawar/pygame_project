import pygame
import entities.basic_tiles as basic_tiles

class Enemy(basic_tiles.Tile):
    
    def __init__(
        self,
        coordinates,
        width,
        height,
        
        fill_colour = (0, 0, 120),
        border_size = 100,
        corner_radius = (-1, -1, -1, -1), # top_left, top_right, bottom_left, bottom_right
        
        health_points = 100,
        speed = 3,
        
    ) -> None:
        self.health_points = health_points
        self.speed = speed
        
        self.fill_colour = fill_colour
        self.border_size = border_size
        self.corner_radius = corner_radius 
        super().__init__(coordinates, width, height)
        