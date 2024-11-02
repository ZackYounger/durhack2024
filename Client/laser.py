import pygame
from pygame.locals import *

from helpers import add_vecs, multiply_vec_float


def circle_surface(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


class Laser:
	def __init__(self, pos, vel_dir):
		self.pos = pos 
		self.vel = multiply_vec_float(vel_dir, .001)

		self.radius = 5

	def update(self):
		self.pos = add_vecs(self.pos, self.vel)


	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), self.pos, self.radius)

		screen.blit(circle_surface(self.radius, (255,255,255)), self.pos, special_flags=BLEND_RGB_ADD)