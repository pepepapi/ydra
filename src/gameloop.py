import pygame as pg
import sarg
from   camera   import Camera
from   settings import BGCOLOR, TICKS_PER_SECOND
from   settings import SCREEN_WIDTH, SCREEN_HEIGHT, Debug

change_occured = False

def gameloop(circuit) :
    global change_occured
    pg.init()
    running = True
    screenWidth  = sarg.Int("width",  SCREEN_WIDTH)
    screenHeight = sarg.Int("height", SCREEN_HEIGHT)
    delay   = sarg.Int("delay", 50)
    screen  = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pg.time.Clock()
    camera = Camera(pg)

    while running:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN :
            if Debug : print( "Mouse clicked at (%d, %d)" % event.pos)
            circuit.checkClicked(event.pos)

        change_occured = False
        clock.tick(TICKS_PER_SECOND)   # times per second
        circuit.computeOutput()
        if change_occured :
            screen.fill(BGCOLOR)
            circuit.draw(screen)
            pg.display.flip()
            camera.armed = True
            camera.takePicture(screen)
            if Debug : print( "Hit return to continue:")
    camera.makeGif(delay=delay, loop=0)
    pg.quit()
