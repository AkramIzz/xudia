from xudia.scene import Scene
from xudia.entity import Entity
from xudia.systems.hitbox import Hitbox
from xudia.utils import Vec2D
from ship import Ship
from fps import FPS

from xudia import Xudia

class GameScene(Scene):
	def begin(self):
		self.enemy = Entity(
			Vec2D(Xudia.renderer.width-10, Xudia.renderer.height/2),
			Xudia.Graphic('<<==\n|===\n<<=='),
			None

		)
		hitbox = Hitbox(self.enemy, 4, 3)
		self.enemy.hitbox = hitbox
		
		self.add_entity(self.enemy)

		self.add_entity(Ship(Xudia.renderer.width/2, Xudia.renderer.height/2))
		
		self.add_entity(FPS())

		Xudia.input.add_listener('q', Xudia.engine.stop)