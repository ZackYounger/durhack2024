import pygame

from helpers import multiply_vec_float, add_vecs

class Player:

	def __init__(self, pos):
		
		self.pos = pos
		self.vel = [0, 0]
		self.acc = [0, 0]

		self.width = 25
		self.height = 25
		self.acc_scaling = 1
		self.vel_drag = .8

		self.controls = {"up": pygame.K_UP,
                    "down": pygame.K_DOWN,
                    "right": pygame.K_RIGHT,
                    "left": pygame.K_LEFT,
                    "jump": pygame.K_j,
                    "dash": pygame.K_k,
                    "hold": pygame.K_l,
                    "esc": pygame.K_ESCAPE}

	def update(self, dt, keys):
		
		acc_inp = [keys[self.controls["right"]] - keys[self.controls["left"]],
						keys[self.controls["down"]] - keys[self.controls["up"]]]
		self.acc = multiply_vec_float(acc_inp, self.acc_scaling)

		self.vel = add_vecs(self.acc, self.vel)
		self.vel = multiply_vec_float(self.vel, self.vel_drag)

		self.pos = add_vecs(self.vel, self.pos)



	def draw(self, screen):
		self.draw_pos = [self.pos[0] - self.width/2, self.pos[1] - self.height/2]
		pygame.draw.rect(screen, (255,255,0), [*self.draw_pos, self.width, self.height])