
#	importing data	#

#reading a text file
filename = 'novel.txt'
file = open(filename,'r') #open(filename,mode = 'r')
text = file.read()
file.close()
print(text)

#with is a context manager
#using "with" statement is very smart.we never think that do we close the file
with open('novel.txt','r') as file:
	print(file.read())


