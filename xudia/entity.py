from .utils import Vec2D

class Entity:
	def __init__(self, pos_vector, graphic, hitbox):
		self.position = pos_vector
		self.graphic = graphic
		self.hitbox = hitbox

	def move_to(self, pos_vector):
		self.position = pos_vector

	def move_by(self, delta_vector):
		self.position += delta_vector

	def size(self):
		return self.size

	def update(self):
		pass