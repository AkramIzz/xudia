class Xudia:
	def init(engine, scene, default_systems=True, fps=120):
		Xudia.engine = engine
		Xudia.scene = scene
		
		if default_systems:
			from .curses_systems.curses_tick_provider import CursesTickProvider
			from .curses_systems.curses_renderer import CursesRenderer
			from .curses_systems.curses_input_handler import CursesInputHandler

			Xudia.tickProvider = CursesTickProvider()
			Xudia.input = CursesInputHandler()
			Xudia.renderer = CursesRenderer()

		Xudia.engine.init_systems()
		Xudia.tickProvider.setFPS(fps)