from xudia.utils import Vec2D

class Graphic:
	def __init__(self, shape):
		self.set_shape(shape)

	def get_size(shape):
		size = Vec2D(0, 0)
		size.y = len(shape.split('\n'))
		size.x = len(shape.split('\n')[0])
		return size

	def set_shape(self, shape):
		self.shape = shape
		self.size = Graphic.get_size(shape)

	def render(self):
		return self.shape.split('\n')