from xudia.entity import Entity

from xudia import Xudia
from xudia.systems.hitbox import Hitbox
from xudia.utils import Vec2D

class Bullet(Entity):
	def __init__(self, x, y, velocity):
		hitbox = Hitbox(self, 1, 1)
		super().__init__(Vec2D(x, y), Xudia.Graphic('+'), hitbox)
		self.velocity = velocity
		self.life = 60

	def get_speed(self):
		return self.velocity

	def update(self):
		self.life -= 1
		if self.life < 1:
			Xudia.scene.remove_entity(self)
		self.move_by(self.velocity)
