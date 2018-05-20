from xudia.entity import Entity

from xudia import Xudia
from xudia.utils import Vec2D

class FPS(Entity):
	def __init__(self, x=0, y=0):
		super().__init__(Vec2D(x, y), shape='')
		self.lastCall = 0

	def update(self):
		if self.lastCall >= 0.1:
			self.lastCall = 0
			self.update_display()
		self.lastCall += Xudia.tickProvider.elapsed 

	def update_display(self):
		engine = Xudia.engine
		self.setShape('FPS: ' 
			+ str(int(1/Xudia.tickProvider.elapsed)).ljust(3) 
			+ '  Entities:' + str(len(Xudia.scene.entities))
			+ '  ' + str(Xudia.renderer.width) + 'x' + str(Xudia.renderer.height))
