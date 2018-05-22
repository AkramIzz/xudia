class Xudia:
	def init(engine, scene, default_systems=True, fps=120):
		Xudia.engine = engine
		Xudia.scene = scene
		
		if default_systems:
			from .backends.curses.tick_provider import TickProvider
			from .backends.curses.renderer import Renderer
			from .backends.curses.input_handler import InputHandler

			Xudia.tickProvider = TickProvider()
			Xudia.input = InputHandler()
			Xudia.renderer = Renderer()

		Xudia.engine.init_systems()
		Xudia.tickProvider.setFPS(fps)