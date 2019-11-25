class pylogger:

	def __init__(self, log_file=False, toStd=True):
		
		self.log_file = log_file
		self.toStd = toStd



	def config(self, log_file=False, toStd=True):
		
		self.log_file = log_file
		self.toStd = toStd


	def log(self, string, status=0):

		import datetime, sys, traceback

		global error_count
		global warning_count

		if "warning_count" not in globals():
			warning_count = 0
		if "error_count" not in globals():
			error_count = 0
		
		if status == 0:
			status_msg = "INFO"
		if status == 1:
			status_msg = "WARNING"
			warning_count += 1
		elif status == 2:
			status_msg = "ERROR"
			error_count += 1
		
		
		time = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S ")
		log_string = str(time) + str(status_msg) + ": " + str(string)
		
		
		if self.log_file:
			if self.log_file == True:
				print("Error: logfile can't be true!")
			else:
				try:
					with open(self.log_file, 'a') as f:
						f.writelines(log_string + "\n")

				except IOError:
					print("Error: The logfile is not accessible. Please make sure that the path exists and the permissions are correct.")
					traceback.print_exc()

		if self.toStd:
			if status == 0:
				print(log_string, file=sys.stdout)
			elif status == 1 or status == 2:
				print(log_string, file=sys.stderr)

	def counted_errors():
		if error_count == 0:
			return "No Errors!"
		else:
			return error_count

	def counted_warnings():
		if warning_count == 0:
			return "No Warnings!"
		else:
			return warning_count
