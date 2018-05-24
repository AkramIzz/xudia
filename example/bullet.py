from xudia.entity import Entity

from xudia import Xudia
from xudia.utils import Vec2D

class Bullet(Entity):
	def __init__(self, x, y, velocity):
		super().__init__(Vec2D(x, y), Xudia.Graphic('+'))
		self.velocity = velocity
		self.life = 60

	def get_speed(self):
		return self.velocity

	def update(self):
		self.life -= 1
		if self.life < 1:
			Xudia.scene.remove_entity(self)
		self.move_by(self.velocity)
