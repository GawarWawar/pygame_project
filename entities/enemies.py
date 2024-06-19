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
        corner_radius = (-1, -1, -1, -1),
        
        health_points = 100,
        speed = 8,
        
    ) -> None:
        self.health_points = 100
        self.speed = 3
        
        self.fill_colour = (0, 0, 120)
        self.border_size = 0
        self.corner_radius = (-1, -1, -1, -1) #top_left, top_right, bottom_left, bottom_right
        super().__init__(coordinates, width, height)
        