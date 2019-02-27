#Error Handling or Exception Handling by Şammas Çölkesen

#this is just a basic structure of try-except statements

import sys # this is a module that provides us python basic functions.
#we can find what kind of functions avaible for us this method 
#dir(sys)

a = 3
b = 0

#In larger codes we cannot go back and analyse the problem so we could use error handling that where we think may cause a problem.
 
try:
	a/b
except Exception as e:


	print(sys.exc_info()[2].tb_lineno) 
	#exc_info method gives us a info about error.
	#tb_lineno give us a line that with error.

	# raise e 
	# e is a exception type
	#or print(str(exception type))

	# [0] is an error name
	# [1] is an error definition
	# [2] is an error line

	#or we can format our unique message
	print('Error: {}. {}, line: {}'.format(
		sys.exc_info()[0],
	 	sys.exc_info()[1],
	 	sys.exc_info()[2].tb_lineno
	 	))


#but this error handling may be as long as 100 lines.
#so we must define a function that must includes all things that we made before.



	"""

import sys
import logging

def error_handling():
	return '{}. {}, line: {}'.format(
		sys.exc_info()[0],
	 	sys.exc_info()[1],
	 	sys.exc_info()[2].tb_lineno
	 	)


try:
	a/b
except Exception as e:
	logging.error(error_handling())

	"""
