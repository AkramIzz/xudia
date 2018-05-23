import curses

from xudia.system import System
from xudia import Xudia

class InputHandler(System):
	def __init__(self):
		self.events = dict()
		self.add_on_next_update = []

	def addListener(self, key, callback):
		# DANGER:
		# adding a listener on the same frame may cause an infinite loop
		self.add_on_next_update.append((key, callback))

	def addWaitingListeners(self):
		for key, callback in self.add_on_next_update:
			if self.events.get(key):
				self.events[key].append(callback)
			else:
				self.events[key] = [callback]
		self.add_on_next_update = []

	def addListeners(self, keys, callbacks):
		for key, callback in zip(keys, callbacks):
			self.addListener(key, callback)

	def on_screen_created(self):
		curses.noecho()
		curses.cbreak()
		self.screen = Xudia.renderer.screen
		self.screen.keypad(1)
		self.screen.nodelay(True)

	def on_screen_ending(self):
		self.screen.keypad(0)
		curses.nocbreak()
		curses.echo()
		self.screen = None

	def update(self):
		self.addWaitingListeners()
		try:
			k = self.screen.getkey()
		except:
			return
		if k in self.events.keys():
			for callback in self.events[k]:
				callback()
