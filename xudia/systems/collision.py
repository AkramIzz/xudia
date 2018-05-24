from ..system import System

class Collision(System):
	def __init__(self):
		self.collidables = []

	def colliding(a, b):
		return (
			a.x() < b.x() + b.width and a.x() + a.width > b.x() 
			and a.y() < b.y() + b.height and a.y() + a.height > b.y()
		)

	def add_collidable(self, a, b, callback):
		self.collidables.append({'hitbox': (a.hitbox, b.hitbox), 'callback': callback})

	def update(self):
		colliding = filter(lambda c : Collision.colliding(*c['hitbox']), self.collidables)
		for c in colliding:
			c['callback']()