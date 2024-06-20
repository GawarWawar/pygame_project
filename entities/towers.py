import pathlib
import pygame

import entities.basic_tiles as basic_tiles

class TowerFundament (basic_tiles.Tile):
    fill_colour = (180, 160, 160) 
    border_size = 100
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Tower_fundament.png")
    
class Tower (TowerFundament):
    ...

class BasicTower (Tower):
    fill_colour = (0, 150, 0)
    border_size = 100
    draw_function = pygame.draw.circle
    corner_radius = (20, 20, 20, 20)
    _image_path = pathlib.Path(__file__).parent.joinpath("pictures/Basic_tower.png")