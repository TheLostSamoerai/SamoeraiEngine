import pygame as pg

class Particle:
    def __init__(self, size):
        self.particle = pg.Surface((20, 20))
        self.rect = self.particle.get_frect()
    
    def run(self, mouse_pos):
        if pg.KEYDOWN:
            if
        self.rect.center = (mouse_pos)
