import pygame
import entities.basic_tiles as basic_tiles

class Enemy(basic_tiles.Tile):
    
    def __init__(
        self,
        health_points = 100,
        fill_colour = (0, 0, 120),
        border_size = 0,
    ) -> None:
        self.health_points = 100
        self.fill_colour = (0, 0, 120)
        self.border_size = 0
        corner_radius = (-1, -1, -1, -1) #top_left, top_right, bottom_left, bottom_right
        