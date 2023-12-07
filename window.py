import pygame as pg
from sys import exit

pg.init()

class MainWindow:
    def __init__(self, width, height, fps, caption, icon_path, Editor):
        self.window = pg.display.set_mode((width, height), vsync=True)

        try:
            self.icon_img = pg.image.load(icon_path)
            pg.display.set_icon(self.icon_img)
        except Exception:
            print("No icon path specified")

        

        pg.display.set_caption(str(caption))

        self.clock = pg.Clock()
        self.fps = fps
        self.editor = Editor()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
            self.window.fill('black')
            self.editor.run()
            
            pg.display.update()

            self.clock.tick(self.fps)