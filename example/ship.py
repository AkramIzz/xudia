from xudia import Xudia
from xudia.entity import Entity
from xudia.utils import Vec2D

import curses

from bullet import Bullet

class Ship(Entity):
	def __init__(self, x, y):
		shape = '+'
		super().__init__(Vec2D(x, y), shape)
		self.init_input(Xudia.input)
		self.velocity = Vec2D(0, 0)
		self.direction = Vec2D(0, 0)
		self.speed = 1

	def init_input(self, inputHandler):
		inputHandler.addListener('KEY_UP', self.onkeyup)
		inputHandler.addListener('KEY_RIGHT', self.onkeyright)
		inputHandler.addListener('KEY_DOWN', self.onkeydown)
		inputHandler.addListener('KEY_LEFT', self.onkeyleft)
		inputHandler.addListener(' ', self.onfire)
	
	def update(self):
		self.moveBy(self.velocity)
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
			b = Bullet(self.pos.x+4, self.pos.y+1, Vec2D(self.direction, 0))
		elif self.direction == -1:
			b = Bullet(self.pos.x-1, self.pos.y+1, Vec2D(self.direction, 0))
		else:
			return
		Xudia.scene.addEntity(b)

	def steer(self, direction):
		if direction == 1:
			self.setShape('==>>\n===|\n==>>')
			self.direction = 1
		elif direction == -1:
			self.setShape('<<==\n|===\n<<==')
			self.direction = -1
