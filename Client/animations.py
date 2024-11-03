import pygame

from Client.spritesheet import SpriteSheet

class AnimationHandler:
	def __init__(self, sprite_name):

		self.sheets = {}

		states = ['idle', 'move', 'dash']
		frames = [10,10,5]

		dir_name = f'Assets/sprites/male/{sprite_name}/'

		for i, state in enumerate(states):
			sprite_sheet_image = pygame.image.load(dir_name + f'base/{state}.png')#, pygame.SRCALPHA)
			sheet = SpriteSheet(sprite_sheet_image)
			self.sheets[state] = {'sheet' : sheet, 'frames' : frames[i]}

		self.frame_index = 0
		self.current_state_frame = 0
		self.frame_time = 5
		self.last_state = None


	# if i keeled over tomrrow you fucks would have no idea what this whitchcraft meant
	def get_sprite(self, state, scale=1):
		self.current_state_frame += 1
		if self.last_state != state:
			self.current_state_frame = 0
			self.frame_index = 0

		else:
			if self.current_state_frame == self.sheets[state]['frames']:
				self.current_state_frame = 0
				self.frame_index += 1


		self.last_state = state

		return self.sheets[state]['sheet'].get_image(self.frame_index, scale)