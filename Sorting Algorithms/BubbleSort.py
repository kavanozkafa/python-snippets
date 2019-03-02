
def bubbleSort(mylist):
	for passnum in range(len(mylist)-1,0,-1):
		for i in range(passnum):
			if mylist[i] > mylist[i + 1]:
				temp = mylist[i]
				mylist[i] = mylist[i + 1]
				mylist[i + 1] = temp

mlist = [2,78,45,990,45,68,34,3,345,42]
bubbleSort(mlist)
print(mlist)
