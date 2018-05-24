from .system import System

class Scene(System):
	def __init__(self):
		self.entities = []

	def add_entity(self, e):
		self.entities.append(e)

	def remove_entity(self, e):
		try:
			self.entities.remove(e)
			return True
		except:
			return False

	def remove_all_entities(self, e):
		self.entities = []

	def update(self):
		for e in self.entities:
			e.update()