from .utils import Vec2D

def getSize(shape):
	size = Vec2D(0, 0)
	size.y = len(shape.split('\n'))
	size.x = len(shape.split('\n')[0])
	return size

class Entity:
	def __init__(self, pos_vector, shape):
		self.pos = pos_vector
		self.shape = shape
		self.size = getSize(shape)

	def moveTo(self, pos_vector):
		self.pos = pos_vector

	def moveBy(self, delta_vector):
		self.pos += delta_vector

	def position(self):
		return self.pos

	def size(self):
		return self.size

	def render(self):
		return self.shape

	def setShape(self, shape):
		self.shape = shape
		self.size = getSize(shape)