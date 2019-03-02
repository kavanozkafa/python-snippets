import math


def binarySearch(myList, element):
	bottom = 0
	top = len(myList) - 1
	index = -1
	while top >= bottom and index == -1:
		mid = int(math.floor((top + bottom) / 2.0))
		if myList[mid] == element:
			index = mid

		elif myList[mid] > element:
			top = mid-1

		else:
			bottom = mid + 1
	return index

myList = [2, 4, 5, 6, 8, 3]
print(binarySearch(myList, 8))