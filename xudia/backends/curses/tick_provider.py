from xudia.system import System
import time

class CursesTickProvider(System):
	def __init(self):
		self.fps = 0
		self.update = update_placeholder

	def begin(self):
		self.frame_begin = time.time()
		self.elapsed = 0

	def setFPS(self, fps):
		self.fps = fps
		if fps > 0:
			self.update = self.update_fixed_fps
		else:
			self.update = self.update_placeholder

	def update_fixed_fps(self):
		self.elapsed = time.time() - self.frame_begin
		while self.elapsed <= 1/self.fps:
			self.elapsed = time.time() - self.frame_begin
		self.frame_begin = time.time()

	def update_placeholder(self):
		self.elapsed = time.time() - self.frame_begin
		self.frame_begin = time.time()