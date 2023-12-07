import pygame as pg
from sys import exit

pg.init()

class MainWindow:
    def __init__(self, width, height, fps, caption, icon_path, Game):
        self.window = pg.display.set_mode((width, height), vsync=True)

        self.icon_img = pg.image.load(icon_path)
        pg.display.set_icon(self.icon_img)

        pg.display.set_caption(str(caption))

        self.clock = pg.Clock()
        self.fps = fps
        self.game = Game()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
            self.window.fill('black')
            self.game.run()
            
            pg.display.update()

            self.clock.tick(self.fps)