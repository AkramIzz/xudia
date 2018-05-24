def get_tick_provider():
	from .curses.tick_provider import TickProvider
	return TickProvider()

def get_renderer():
	from .curses.renderer import Renderer
	return Renderer()

def get_input_handler():
	from .curses.input_handler import InputHandler
	return InputHandler()

def get_graphic_class():
	from .curses.graphic import Graphic
	return Graphic