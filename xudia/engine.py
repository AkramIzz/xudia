import time
import curses

from xudia import Xudia

class Engine:
	def __init__(self):
		self.running = False

	def init_systems(self):
		self.systems = [Xudia.scene]
		self.scene = Xudia.scene
		self.input = Xudia.input
		self.renderer = Xudia.renderer
		self.tickProvider = Xudia.tickProvider

	def add_system(self, system):
		if self.running:
			system.begin()
		self.systems.appendleft(system)

	def remove_system(self, system):
		self.systems.remove(system)

	def start(self):
		curses.wrapper(self.game_loop)
		
	def game_loop(self, screen):
		self.running = True
		Xudia.screen = screen

		self.input.begin()
		self.renderer.begin()
		self.tickProvider.begin()
		for sys in self.systems:
			sys.begin()

		while self.running:
			self.input.update()
			for sys in self.systems:
				sys.update()
			self.renderer.update()
			self.tickProvider.update()

	def stop(self):
		self.running = False
