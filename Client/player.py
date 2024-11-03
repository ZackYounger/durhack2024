import pygame
import random

from Client.laser import Laser
from Client.animations import AnimationHandler

from Client.helpers import multiply_vec_float, add_vecs, sub_vecs

player_colours = [
	(0, 51, 204),
	(255, 51, 51),
	(255, 235, 20),
	(0, 153, 51)

]

dulled_player_colours = [[j/2 for j in colour] for colour in player_colours]

class Player:

	def __init__(self, screen_size, border_walls, block_width, playerID=0):
		
		self.playerID = playerID

		self.pos = [0,0]
		self.vel = [0, 0]
		self.acc = [0, 0]

		self.sprite_scaling = 2
		self.width = 24 * self.sprite_scaling
		self.height = 24 * self.sprite_scaling
		self.sprite_width = 20 * self.sprite_scaling
		self.sprite_height = 20 * self.sprite_scaling
		self.vel_drag = .8
		self.acc_scaling = 1

		self.animationHandler = AnimationHandler('loki')

		self.camera_scroll_speed = 20
		self.camera_scroll = [0, 0]

		self.block_width = block_width
		self.border_walls = border_walls

		self.screen_width = screen_size[0]
		self.screen_height = screen_size[1]

		self.controls = {"up": pygame.K_w,
                    "down": pygame.K_s,
                    "right": pygame.K_d,
                    "left": pygame.K_a,
                    "shoot":pygame.K_x,
                    "roll": pygame.K_SPACE,
                    "esc": pygame.K_ESCAPE}
		
		self.roll_speed = 50
		self.roll_cooldown = 120
		self.last_roll = 0
    
		self.laser_speed = 1
		self.shoot_cooldown = 60
		self.last_shoot = 0
		self.lasers = []

		#other_players = [0,1,2,3].remove(playerID)
		#self.kill_order = random.shuffle(other_players)





	def update(self, dt, tick, keys):

		#dt_const = dt * 60
		#nah fuck that if your game is laggy you're on your own

		self.acc = [0, 0]


		#mouse shenanigans
		mx, my = pygame.mouse.get_pos()
		mouse_dir = [mx - self.screen_width/2, my - self.screen_height/2]
		normal_mouse_dir = multiply_vec_float(mouse_dir, 1/(mouse_dir[0]**2 + mouse_dir[1]**2)**.5)



		#dash
		if keys[self.controls["roll"]]:
			if tick - self.last_roll > self.roll_cooldown:

				self.acc = add_vecs(self.acc, multiply_vec_float(normal_mouse_dir, self.roll_speed))
				self.vel = add_vecs(self.vel, multiply_vec_float(normal_mouse_dir, self.roll_speed/300))

				self.last_roll = tick



		#shoot
		if keys[self.controls["shoot"]]:
			if tick - self.last_shoot > self.shoot_cooldown:

				self.lasers.append( Laser(self.pos, normal_mouse_dir, self.playerID) )

				self.last_shoot = tick



		#movement
		acc_inp = [keys[self.controls["right"]] - keys[self.controls["left"]],
						keys[self.controls["down"]] - keys[self.controls["up"]]]
		
		self.acc = add_vecs(self.acc, multiply_vec_float(acc_inp, self.acc_scaling))

		self.vel = add_vecs(self.acc, self.vel)
		self.vel = multiply_vec_float(self.vel, self.vel_drag)

		self.pos = add_vecs(self.vel, self.pos)



		#collisions
		self.hitbox = pygame.Rect(self.pos[0] - self.width/2, self.pos[1] - self.height/2, self.width, self.height)

		#need to fix wall collisions
		wall_collisions = self.hitbox.collidelistall(self.border_walls)

		for wallIndex in wall_collisions:
			wall = self.border_walls[wallIndex]
			wall_center = [wall[0] + self.block_width/2, wall[1] + self.block_width/2]
			distance = add_vecs(self.pos, [-wall_center[0], -wall_center[1]])
			#decide which direction to fix
			dr = 0 if abs(distance[0]) > abs(distance[1]) else 1
			if distance[(dr+1)%2] < self.block_width / 2 + self.width / 2:
				self.pos[dr] =  wall_center[dr] + abs(distance[dr]) / distance[dr] * (self.block_width + (self.width if dr==0 else self.height))/2 



		#camera
		self.camera_scroll[0] += (self.pos[0] - self.camera_scroll[0] - self.screen_width/2) / self.camera_scroll_speed
		self.camera_scroll[1] += (self.pos[1] - self.camera_scroll[1] - self.screen_height/2) / self.camera_scroll_speed


		#I shouldnt be doing this here but I am loosing my will to live
		for laser in self.lasers:
			#move the lasers
			death_time = laser.update()

			#check if ouch
			if self.hitbox.colliderect(laser.hitbox) and laser.alive_time > 15:
				self.take_damage(laser.damage)
				laser.hit_player(self.playerID)

			#check if laser hits walls
			if len(laser.hitbox.collidelistall(self.border_walls)) > 0:
				self.lasers.remove(laser)



		#state time
		if self.vel[0] < 0:
			self.flipped = True
		else:
			self.flipped = False


		if tick - self.roll_cooldown < 15 and tick > 15:
			self.state = "dash"
		elif abs(self.vel[0]) > 1 or abs(self.vel[1]) > 1:
			self.state = "move"
		else:
			self.state = 'idle'


	def take_damage(self, amount):
		print('OUCH! FUCK SHIT OOWWW THA TFUCKING HURTS')



	def draw(self, screen):	

		sprite = self.animationHandler.get_sprite(self.state, self.sprite_scaling)
		sprite = pygame.transform.flip(sprite, self.flipped, False)

		self.draw_pos = [self.pos[0] - self.width/2 - self.camera_scroll[0],
						 self.pos[1] - self.height/2 - self.camera_scroll[1]]

		screen.blit(sprite, self.draw_pos)

		gun = pygame.image.load('Assets/sprites/gun.png').convert_alpha()
		screen.blit(gun, sub_vecs(self.pos, self.camera_scroll))


		#I shouldnt be doing this here but I am loosing my will to live
		for laser in self.lasers:
			laser.draw(screen, self.camera_scroll, dulled_player_colours)




