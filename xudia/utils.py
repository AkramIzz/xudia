class Vec2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self, vec):
		self.x += vec.x
		self.y += vec.y

	def mul(self, scalar):
		self.x *= scalar
		self.y *= scalar

	def __add__(self, vec):
		return Vec2D(self.x + vec.x, self.y + vec.y)

	def __mul__(self, scalar):
		return Vec2D(scalar * self.x, scalar * self.y)