from xudia.scene import Scene

from ship import Ship
from fps import FPS

from xudia import Xudia

class GameScene(Scene):
	def begin(self):
		self.add_entity(Ship(Xudia.renderer.width/2, Xudia.renderer.height/2))
		self.add_entity(FPS())
		Xudia.input.add_listener('q', Xudia.engine.stop)