import pygame
import random


import Network.connect as connect
import Network.network as network

from Client.player import Player
from Client.levelManager import Level
from Client.animations import AnimationHandler


screen_width = 1080
screen_height = 720
FPS = 60


## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound



def ping(data):
  return network.ping(data)






def game_loop(screen):

  #n = network.Network(connect.collective_data['addr'], connect.collective_data)

  #seed = connect.collective_data.seed
  seed = 69.420

  playerID = 0

  opps = [0,1,2,3]
  opps.remove(playerID)
  opp_animationHandlers = {opp : AnimationHandler(opp) for opp in opps}


  level = Level()
  level.create_new_level(41, seed)
  border_walls = level.get_border_walls()

  block_width = level.block_width

  player = Player([screen_width, screen_height], border_walls, block_width, len(opps))

  clock = pygame.time.Clock()     ## For syncing the FPS

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

    screen.fill((51,204,255))

    player.update(dt, tick, keys)

    level.draw(screen, player.camera_scroll, player.screen_shake)

    player.draw(screen)

    #time to assemble the COLLECTIVE DATA
    data = {}
    data['pos'] = player.pos
    data['state'] = player.state
    #data['health'] = player.health #FUKCING KILL DNAIAL
    data['new_lasers'] = player.lasers_to_send



    #connect.collective_data = n.ping(connect.collective_data["player" + str(Player.playerID)])
    print(connect.collective_data)
    ## Done after drawing everything to the screen


    #draw other players
    for oppI in range(4):
        if oppI != player.playerID:
            sprite = opp_animationHandlers[oppI].get_sprite(connect.collective_data[oppI]['state'], player.sprite_scaling)
            screen.blit(sprite, sub_vecs(connect.collective_data[oppI]['pos'], player.camera_scroll + player.screen_shake))

            player.create_laser(*connect.collective_data[oppI]['new_lasers'], oppI)



    player.lasers_to_send = []

    pygame.display.flip()       

  pygame.quit()

if __name__ == "__main__":
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Hello There")
  
  game_loop(screen)
