from .utils import Vec2D

class Entity:
	def __init__(self, pos_vector, graphic):
		self.position = pos_vector
		self.graphic = graphic
		# temporary solution, should reflect the hitbox of the entity
		self.size = self.graphic.size

	def move_to(self, pos_vector):
		self.position = pos_vector

	def move_by(self, delta_vector):
		self.position += delta_vector

	def size(self):
		return self.size

	def update(self):
		pass