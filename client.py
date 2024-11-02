import pygame
import random

from player import Player

screen_width = 1080
screen_height = 720
FPS = 30

player = Player([screen_width/2, screen_height/2])

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS


## Game loop
running = True
dt = 0
while running:

    #1 Process input/events
    dt = clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.update(dt, keys)

    player.draw(screen)



    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()