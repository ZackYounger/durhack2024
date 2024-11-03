import pygame

from Client.spritesheet import SpriteSheet

class AnimationHandler:
	def __init__(self, sprite_name):

		self.sheets = {}

		dir_name = f'Assets/sprites/male/{sprite_name}/'

		sprite_sheet_image = pygame.image.load(dir_name + 'base/idle.png').convert_alpha()
		idle_sheet = SpriteSheet(sprite_sheet_image)
		self.sheets['idle'] = idle_sheet

		self.frame_index = 0
		self.current_state_frame = 0
		self.frame_time = 5
		self.last_state = None


	# if i keeled over tomrrow you fucks would have no idea what this whitchcraft meant
	def get_sprite(state):
		self.current_state_frame += 1
		if self.last_state != state:
			self.current_state_frame = 0
			self.frame_index = 0

		else:
			if self.current_state_frame == self.frame_time:
				self.frame_index += 1
				self.current_state_frame = 0
			else:
				self.current_state_frame += 1

		self.last_state = state

		return self.sheets[state].get_image(self.frame_index)