from ..utils import Vec2D

class Hitbox:
	def __init__(self, entity, width, height):
		self.entity = entity
		self.width = width
		self.height = height

	def x(self):
		return self.entity.position.x

	def y(self):
		return self.entity.position.y