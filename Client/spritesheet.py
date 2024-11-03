import pygame

class SpriteSheet:
	def __init__(self, image):
		self.sheet = image
		self.width, self.height = 24, 24 #fuck shit fuck you stupid
		self.no_sprites = image.get_width() / self.width

	def get_image(self, frame, scale=1, colour=(255,255,255)):
		frame = frame % self.no_sprites
		image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
		image.blit(self.sheet, (0, 0), ((frame * self.width), 0, self.width, self.height))
		image = pygame.transform.scale(image, (self.width * scale, self.height * scale))
		#image.set_colorkey(colour)

		return image