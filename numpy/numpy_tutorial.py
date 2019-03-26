import numpy as np

x = np.array([1, 2, 3])
print(x)

#we can do math with numpy array objects
#we can pass list or tuple to array() and return as a array object
x = x*2
print(x) #[2 4 6]


#we would have had to use a list comprehension
print([2*xl for xl in x]) #[4, 8, 12]

#We can work with more arrays and make them interact
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
a+b #[4 4 4]

#We can also create multidimensional arrays
M = np.array([[1, 2, 3], [4, 5, 6]])
M[1,2] #6

#Another important function the one that we already met, is arange()
np.arange(6) #[0 1 2 3 4 5]
