#basic stack implementation

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == [] #check if Stack is empty

	def push(self, item):
		self.items.append(item) #insert element into stack

	def pop(self):
		return self.items.pop() #removes last element from stack

	
	def size(self):
		return len(self.items) #returns size of stack