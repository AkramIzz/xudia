import curses
from ..system import System
from ..utils import Vec2D

from xudia import Xudia

class CursesRenderer(System):
	def begin(self):
		self.screen = Xudia.screen
		self.scene = Xudia.scene
		self.init_curses()
		self.update_dims()

	def init_curses(self):
		curses.noecho()
		curses.curs_set(False)
		curses.cbreak()
	
	def update(self):
		graphics = self.scene.render()
		self.screen.clear()
		curses.update_lines_cols()
		self.update_dims()
		for g in graphics:
			self.draw(g.render().split('\n'), g.position(), g.size)
		self.screen.refresh()

	def update_dims(self):
		self.width = curses.COLS
		self.height = curses.LINES

	def draw(self, graphic, pos, size):
		pos = Vec2D(int(pos.x), int(pos.y))
		size = Vec2D(int(size.x), int(size.y))
		graphic, pos, size = self.getVisible(graphic, pos, size)
		try:
			for i, l in enumerate(graphic):
				self.screen.addstr(pos.y + i, pos.x, l)
		except curses.error:
			pass
				
	def getVisible(self, graphic, pos, size):
		# the whole graphic isn't visible
		if pos.y >= curses.LINES or pos.x >= curses.COLS:
			return [], pos, Vec2D(0, 0)
		if pos.y + size.y <= 0 or pos.x + size.x <= 0:
			return [], pos, Vec2D(0, 0)

		# partially hidden up or down
		if len(graphic) > curses.LINES - pos.y:
			graphic = graphic[:curses.LINES - pos.y]
		if pos.y < 0:
			graphic = graphic[-pos.y:]
			pos.y = 0

		# partially hidden left or right
		if len(graphic[0]) > curses.COLS - pos.x:
			for i in range(len(graphic)):
				graphic[i] = graphic[i][:curses.COLS - pos.x]
		if pos.x < 0:
			for i in range(len(graphic)):
				graphic[i] = graphic[i][-pos.x:]
			pos.x = 0
		
		return graphic, pos, Vec2D(len(graphic[0]), len(graphic))