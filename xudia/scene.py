from .system import System

class Scene(System):
	def __init__(self):
		self.entities = []

	def addEntity(self, e):
		self.entities.append(e)

	def removeEntity(self, e):
		self.entities.remove(e)

	def removeAllEntities(self, e):
		self.entities = []

	def update(self):
		for e in self.entities:
			e.update()