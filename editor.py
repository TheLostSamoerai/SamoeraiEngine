import pygame as pg

class Editor:
    def __init__(self, Particle):
        self.particle = Particle()
    def run(self):
        mouse_pos = pg.mouse.get_pos()
        self.particle.run(mouse_pos)