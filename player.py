import pygame

from helpers import multiply_vec_float, add_vecs


class Player:

	def __init__(self, screen_size, border_walls, block_width):
		
		self.pos = [0,0]
		self.vel = [0, 0]
		self.acc = [0, 0]

		self.width = 25
		self.height = 25
		self.acc_scaling = 1
		self.vel_drag = .8

		self.camera_scroll_speed = 20
		self.camera_scroll = [0, 0]

		self.block_width = block_width
		self.border_walls = border_walls

		self.screen_width = screen_size[0]
		self.screen_height = screen_size[1]

		self.controls = {"up": pygame.K_UP,
                    "down": pygame.K_DOWN,
                    "right": pygame.K_RIGHT,
                    "left": pygame.K_LEFT,
                    "dash": pygame.K_k,
                    "esc": pygame.K_ESCAPE}
		

	def update(self, dt, keys):

		#movement
		acc_inp = [keys[self.controls["right"]] - keys[self.controls["left"]],
						keys[self.controls["down"]] - keys[self.controls["up"]]]
		self.acc = multiply_vec_float(acc_inp, self.acc_scaling)

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
			print(distance)
			dr = 0 if abs(distance[0]) > abs(distance[1]) else 1
			if distance[(dr+1)%2] < self.block_width / 2 + self.width / 2:
				self.pos[dr] =  wall_center[dr] + abs(distance[dr]) / distance[dr] * (self.block_width + (self.width if dr==0 else self.height))/2 


		#camera
		self.camera_scroll[0] += (self.pos[0] - self.camera_scroll[0] - self.screen_width/2) / self.camera_scroll_speed
		self.camera_scroll[1] += (self.pos[1] - self.camera_scroll[1] - self.screen_height/2) / self.camera_scroll_speed



	def draw(self, screen):
		self.draw_pos = [self.pos[0] - self.width/2 - self.camera_scroll[0],
						 self.pos[1] - self.height/2 - self.camera_scroll[1]]
		pygame.draw.rect(screen, (255,255,0), [*self.draw_pos, self.width, self.height])

		for wall in self.border_walls:
			
			draw_pos = [wall[0] + 1 - self.camera_scroll[0] , wall[1] + 1 - self.camera_scroll[1]]
			pygame.draw.rect(screen, (55,100,155), [*draw_pos, self.block_width - 2, self.block_width - 2])
