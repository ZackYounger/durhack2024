import pygame

from helpers import multiply_vec_float, add_vecs

class Player:

	def __init__(self, pos):
		
		self.pos = pos
		self.vel = [0, 0]
		self.acc = [0, 0]

		self.width = 25
		self.height = 25

		player1_controls = {"up": pygame.K_w,
                    "down": pygame.K_s,
                    "right": pygame.K_d,
                    "left": pygame.K_a,
                    "jump": pygame.K_j,
                    "dash": pygame.K_k,
                    "hold": pygame.K_l,
                    "esc": pygame.K_ESCAPE}


        acc_scaling = 1

	def update(self, dt, keys):
		
		acc_inp = [keys[self.commands["right"]] - keys[self.commands["left"]],
						keys[self.commands["up"]] - keys[self.commands["down"]]]

		self.acc = multiply_vec_float(acc_inp, acc_scaling)

		s



	def draw(self, screen):
		self.draw_pos = [self.pos[0] - self.width/2, self.pos[1] - self.height/2]
		pygame.draw.rect(screen, (255,255,0), [*self.draw_pos, self.width, self.height])