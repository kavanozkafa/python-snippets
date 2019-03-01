#This file includes some tips and tricks about pyhton .
#these codes can be very useful.

#for more visit : https://www.python.org/dev/peps/pep-0008/


######################
#swap the values of variables
x,y = y,x

#also works on any kind of arrays
list[i], list[i + 1] = list[i + 1] + list[i]

#####################
#converting a list to a string
mylist = ["apple", "milk","car","home"]
print(", ".join(mylist))

#####################
#short if code
print("hello" if 3 > 2 else "shit")
#>>hello

#####################
# the counter module is very useful
from collections import Counter
print(Counter("sammas"))
# Counter({'s': 2, 'a': 2, 'm': 2})

####################
# very cool combination library
from itertools import combinations
teams = ["BJK", "MUFC", "FBC","ASR"]
for game in combinations(teams,2):
	print(game)

"""

('BJK', 'MUFC')
('BJK', 'FBC')
('BJK', 'ASR')
('MUFC', 'FBC')
('MUFC', 'ASR')
('FBC', 'ASR')

"""

#################
#reverse of a string
word = "python"

reverseWord = word[::-1] #1

"python"[::-1] #2

#reverse of list
testList = [3, 5, 7]
testList.reverse()

testList[::-1]


#####################
#all the result we test in python console dispatches to temp name the _ (underscore)
>>2 + 1
#>>3
>>_
#>>3

########################
#very useful if usage
if m in [2,4,7,9]:
	print(m)

#instead of this
if m == 2 or m == 4 or m == 7 or m == 9


#####################3
#python3 doesn't contain switch-case statement
#here it is an alternative

def swithcCase(x):
	return swithcCase._system_dict.get(x, None)

swithcCase._system_dict = {'case1':1, 'case2':2, 'case3':3}

print(swithcCase('case2'))
#>>2


#####################
#we can use functions like sum to make greater generators for reducing the number of lines of code

#instead of this
sum = 0
for i in range(1300):
	if i % 3 == 0 or i % 5 == 0:
		sum += i
print(sum)

#we can try this
sum(i for i in range(1300) if i % 3 == 0 or i % 5 == 0)

#####################
#check the memory usage of an object
import sys
x = 1
print(sys.getssizeof(x))




#####################
#we can declare multiğle variables to call same function in a line

def callMe():
	return 1, 2, 3

a, b, c = callMe()
print(a, b, c)
#>> 1 2 3

#####################
#we can inspect an object and see all the operations avaible to perform on that objcet by using the dir() method.
test = [1, 2, 3]
print(dir(test)) # this shows the list operations

#####################
#use numpy module for trigonometri
import numpy as np
print(np.sin(90))
print(np.pi * 3)
