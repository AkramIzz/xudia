import sys
sys.path.append('../')

from xudia import Xudia
from xudia.engine import Engine
from xudia.systems.collision import Collision
from xudia.logger import Logger

from gameScene import GameScene

try:
	Logger.init()
	engine = Engine()

	Xudia.init(engine, GameScene())
	
	Xudia.collision = Collision()
	engine.add_system(Xudia.collision)
	
	engine.start()
except Exception as e:
	Logger.print_log()
	raise
