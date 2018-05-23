from .backends import curses_backend

class Xudia:
	def init(engine, scene, backend=curses_backend, fps=120):
		Xudia.backend = backend
		Xudia.engine = engine
		Xudia.scene = scene
		
		Xudia.tickProvider = backend.get_tick_provider()
		Xudia.input = backend.get_input_handler()
		Xudia.renderer = backend.get_renderer()

		Xudia.engine.init_systems()
		Xudia.tickProvider.set_fps(fps)