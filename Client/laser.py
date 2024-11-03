import pygame
from pygame.locals import *

from Client.helpers import add_vecs, multiply_vec_float, sub_vecs


def circle_surface(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


class Laser:
	def __init__(self, pos, vel_dir, playerID):
		self.pos = pos 
		self.laser_speed = 5
		self.vel = multiply_vec_float(vel_dir, self.laser_speed)

		self.radius = 5

		self.damage = 20

		self.playerID = playerID

		self.alive_time = 0



	def update(self):

		self.hitbox = pygame.Rect(self.pos[0] - self.radius/2, self.pos[1] - self.radius/2, self.radius, self.radius)

		self.pos = add_vecs(self.pos, self.vel)

		self.alive_time += 1

	def hit_player(self, playerID):
		pass



	def draw(self, screen, camera_scroll, player_colours):

		#i know i know, i dont know why but it lags behind without this :((((
		self.hitbox = pygame.Rect(self.pos[0] - self.radius/2, self.pos[1] - self.radius/2, self.radius, self.radius)


		draw_pos = add_vecs(self.pos, multiply_vec_float(camera_scroll, -1))
		pygame.draw.circle(screen, (255,255,255), draw_pos, self.radius)
		screen.blit(circle_surface(self.radius*2, (100,100,100)), sub_vecs(draw_pos, [self.radius*2, self.radius*2]), special_flags=BLEND_RGB_ADD)

		#draw the hitbox because i am mentally ill
		#pygame.draw.rect(screen, player_colours[self.playerID], [self.hitbox[0] - camera_scroll[0], self.hitbox[1] - camera_scroll[1], self.hitbox[2], self.hitbox[3]])





