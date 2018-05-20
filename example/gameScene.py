from xudia.scene import Scene

from ship import Ship
from fps import FPS

from xudia import Xudia

class GameScene(Scene):
	def begin(self):
		self.addEntity(Ship(Xudia.renderer.width/2, Xudia.renderer.height/2))
		self.addEntity(FPS())
		Xudia.input.addListener('q', Xudia.engine.stop)

	def render(self):
		return self.entities