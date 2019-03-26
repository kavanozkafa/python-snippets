#Only one instance may exist at any given time


#First Way

class MySingleton(object):
	"""docstring for MySingleton"""
	_instance = None
	def __new__(self):
		if not self._instance: # check point if there is a instance or not.
			#main subject of singleton design pattern		
			self._instance = super(MySingleton,self).__new__(self)
			self.y = 10
		return self._instance

x = MySingleton() #create instance
print(x.y)
x.y = 20
z = MySingleton() # access same intance
print(z.y) # y will be 20




#Second way and easy decorator one

def singleton(myClass):
	instances = {}
	def getInstance(*args,**kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args,**kwargs)
		return instances[myClass]
	return getInstance

@singleton
class TestClass(object):
	pass

x = TestClass()
