from .utils import Vec2D

def get_size(shape):
	size = Vec2D(0, 0)
	size.y = len(shape.split('\n'))
	size.x = len(shape.split('\n')[0])
	return size

class Entity:
	def __init__(self, pos_vector, shape):
		self.pos = pos_vector
		self.shape = shape
		self.size = get_size(shape)

	def move_to(self, pos_vector):
		self.pos = pos_vector

	def move_by(self, delta_vector):
		self.pos += delta_vector

	def position(self):
		return self.pos

	def size(self):
		return self.size

	def render(self):
		return self.shape

	def set_shape(self, shape):
		self.shape = shape
		self.size = get_size(shape)