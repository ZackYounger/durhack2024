import pygame
import random

import Network.connect as connect

from Client.player import Player
from Client.levelManager import Level


screen_width = 1080
screen_height = 720
FPS = 60


## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello There")
clock = pygame.time.Clock()     ## For syncing the FPS


level = Level()
level.create_new_level(41)
border_walls = level.get_border_walls()

block_width = level.block_width

connect.init_server()


player = Player([screen_width, screen_height], border_walls, block_width, "169.254.131.250")



## Game loop
running = True
dt = 0
tick = 0
while running:

    #1 Process input/events
    dt = clock.tick(FPS)     ## will make the loop run at the same speed all the time
    tick += 1
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player.update(dt, tick, keys)

    level.draw(screen, player.camera_scroll)

    player.draw(screen)

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()


def ping(self, data):
    return self.network.ping(data)