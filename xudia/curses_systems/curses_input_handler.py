from ..system import System

from xudia import Xudia

class CursesInputHandler(System):
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

	def begin(self):
		self.screen = Xudia.screen
		self.screen.nodelay(True)

	def update(self):
		self.addWaitingListeners()
		try:
			k = self.screen.getkey()
		except:
			return
		if k in self.events.keys():
			for callback in self.events[k]:
				callback()
