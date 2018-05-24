from xudia import Xudia
from xudia.entity import Entity
from xudia.systems.hitbox import Hitbox
from xudia.utils import Vec2D

from bullet import Bullet

class Ship(Entity):
	def __init__(self, x, y):
		shape = Xudia.Graphic('+')
		hitbox = Hitbox(self, 4, 3)
		super().__init__(Vec2D(x, y), shape, hitbox)
		self.init_input(Xudia.input)
		self.velocity = Vec2D(0, 0)
		self.direction = Vec2D(0, 0)
		self.speed = 1

	def init_input(self, input_handler):
		input_handler.add_listener('KEY_UP', self.onkeyup)
		input_handler.add_listener('KEY_RIGHT', self.onkeyright)
		input_handler.add_listener('KEY_DOWN', self.onkeydown)
		input_handler.add_listener('KEY_LEFT', self.onkeyleft)
		input_handler.add_listener(' ', self.onfire)
	
	def update(self):
		self.move_by(self.velocity)
		self.velocity = Vec2D(0, 0)

	def onkeyup(self):
		self.velocity = Vec2D(0, -self.speed)

	def onkeyright(self):
		self.velocity = Vec2D(self.speed, 0)
		if self.direction != 1:
			self.steer(1)

	def onkeydown(self):
		self.velocity = Vec2D(0, self.speed)

	def onkeyleft(self):
		self.velocity = Vec2D(-self.speed, 0)
		if self.direction != -1:
			self.steer(-1)

	def onfire(self):
		b = None
		if self.direction == 1:
			b = Bullet(self.position.x+4, self.position.y+1, Vec2D(self.direction, 0))
		elif self.direction == -1:
			b = Bullet(self.position.x-1, self.position.y+1, Vec2D(self.direction, 0))
		else:
			return
		Xudia.scene.add_entity(b)
		Xudia.collision.add_collidable(b, Xudia.scene.enemy, lambda : Xudia.scene.remove_entity(Xudia.scene.enemy))

	def steer(self, direction):
		if direction == 1:
			self.graphic.set_shape('==>>\n===|\n==>>')
			self.direction = 1
		elif direction == -1:
			self.graphic.set_shape('<<==\n|===\n<<==')
			self.direction = -1
