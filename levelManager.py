import pygame

from random import choice

from helpers import add_vecs

class Level:

	def __init__(self):
		self.block_width = 75

	def create_new_level(self, size):


		#make size odd
		size = size if size % 2 == 1 else size + 1
		self.size = size
		middle = size / 2

		dirs = [[1,0], [0,1], [-1,0], [0,-1]]
		last_dir = None

		self.level = [[1 for i in range(size)] for j in range(size)]

		pos = [round(size/2+.5), round(size/2+.5)]
		iterations = 25

		self.level[pos[1]][pos[0]] = 0
		for i in range(iterations):
			direction = choice(dirs)
			pos = add_vecs(pos, direction)
			self.level[pos[1]][pos[0]] = 0

			#expand
			for direction in dirs:
				temp_loc = add_vecs(pos, direction)
				self.level[temp_loc[1]][temp_loc[0]] = 0


	def draw(self, screen, camera_scroll):

		for y in range(len(self.level)):
			for x in range(len(self.level[y])):

				if self.level[y][x] == 1:

					screen_pos = [(x - self.size / 2) * self.block_width + screen.get_width() / 2,
									(y - self.size / 2) * self.block_width + screen.get_height() / 2]
					draw_pos = [screen_pos[0] + 1 - camera_scroll[0] , screen_pos[1] + 1 - camera_scroll[1]]
					pygame.draw.rect(screen, (255,0,255), [*draw_pos, self.block_width - 2, self.block_width - 2])