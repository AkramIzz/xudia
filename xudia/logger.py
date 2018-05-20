class Logger:
	log_file = 'xudia_log'
	def init(log_file='xudia_log'):
		Logger.log_file = log_file
		with open(log_file, 'w') as f:
			pass
	
	def log(*text, sep=' ', end='\n'):
		with open(Logger.log_file, 'a') as log:
			for t in text[:-1]:
				log.write(str(t))
				log.write(sep)
			log.write(str(text[-1]))
			log.write(end)

	def print_log():
		with open(Logger.log_file, 'r') as log:
			print(log.read())