# IMPORTS
import pygame, sys
from constants import *
from logicope import *
from pprint  import pprint

# Path Instance
x = sys.path.insert(0, 'Ydra/assets/fonts/Inter/static/Inter-Light.ttf')

if(GAMESTATE):
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Ydra')
    clock = pygame.time.Clock()

# CREATE INSTANCES

# Font & Text
testFont = pygame.font.Font(None, 50)
textSurface = testFont.render("Hello World", False, (100, 200, 100))

if(GAMESTATE):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Bind the instances to the Display Surface
        screen.blit(textSurface, (20, 20))

        pygame.display.update()
        clock.tick(FPS) # implement better FPS system. Watch Clear Code's video on FPS