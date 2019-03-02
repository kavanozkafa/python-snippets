def LinearSearch(list, item):
	pos = 0
	found = False
	while pos < len(list) and not found:
		if list[pos] == item:
			found = True
		else:
			pos = pos + 1
	return found, pos

print(LinearSearch([2,78,45,990,45,68,34,3,345,42],2))