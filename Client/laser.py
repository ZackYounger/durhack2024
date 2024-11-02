from helpers import add_vecs

class Laser:
	def __init__():
		self.pos = pos 
		self.vel = vel

		self.radius = 5

	def update(self):
		self.pos = add_vecs(self.pos, self.vel)


	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), radius)

		pygame.draw.circle(screen, (255,255,255), radius*2, special_flags=BLEND_RGB_ADD)
