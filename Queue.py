#basic queue implementation

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == [] #check if queue is empty

	def enqueue(self, item):
		self.items.insert(0, item) #insert element into queue

	def dequeue(self):
		return self.items.pop() #removes and returns the value of last element from queue

	
	def size(self):
		return len(self.items) #returns size of stack