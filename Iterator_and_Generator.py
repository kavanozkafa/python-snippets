
###################   ITERATOR   ################################

#An iterator is an object that contains a countable number of values.
#piece of data is repeating a similar calculation over and over.
"""
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

for example for loop is an iterator.
range is an iterator.

"""
for value in range(1,10):
	print(value)

#Python’s itertools library contains a count function that acts as an infinite range:
from itertools import count

for i in count():
	if i >= 10:
		break
		print(i, end=', ')


#Useful Iterators

#enumerate
#Often you need to iterate not only the values in an array, but also keep track of the index. You might be tempted to do things this way:
L = [2, 4, 6, 8, 10]
for i in range(len(L)):
	print(i, L[i])
#Although this does work, Python provides a cleaner syntax using the enumerate iterator:
for i, val in enumerate(L):
	print(i, val)

#zip
#Other times, you may have multiple lists that you want to iterate over simultaneously. You could certainly iterate over the index as in the non-Pythonic example we looked at previously, but it is better to use the zip iterator, which zips together iterables:
#Any number of iterables can be zipped together, and if they are dif‐ ferent lengths, the shortest will determine the length of the zip.
L = [2, 4, 6, 8, 10]
R = [3, 6, 9, 12, 15]
for lval, rval in zip(L, R):
	print(lval, rval)


#map and filter
#The map iterator takes a function and applies it to the values in an iterator:
# find the first 10 square numbers
square = lambda x: x ** 2
for val in map(square, range(10)):
	print(val, end=' ') 
#The filter iterator looks similar, except it only passes through values for which the filter function evaluates to True:
 # find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
	print(val, end=' ')





#Iterators as function arguments
#We saw that *args     	and  **kwargs can be used to pass sequences and dictionaries to functions. It turns out that the *args  	syntax works not just with sequences, but with any iterator:
 print(*range(10))
#So, for example, we can get tricky and compress the map example from before into the following:
print(*map(lambda x: x ** 2, range(10)))

#Specialized Iterators: itertools
#The itertools module contains a whole host of useful iterators; it’s well worth your while to explore the module to see what’s available. 
 from itertools import permutations 
 	p = permutations(range(3)) 
 	print(*p)
#(0, 1, 2) (0, 2, 1) (1, 0, 2) (1, 2, 0) (2, 0, 1) (2, 1, 0)

 from itertools import combinations 
	 c = combinations(range(4), 2) 
	 print(*c)
#(0, 1) (0, 2) (0, 3) (1, 2) (1, 3) (2, 3)
from itertools import product 
	p = product('ab', range(3)) 
	print(*p)
#('a', 0) ('a', 1) ('a', 2) ('b', 0) ('b', 1) ('b', 2)




[val for val in range(20) if val % 3 > 0]
#[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]
 L = []
for val in range(20):
if val % 3:
L.append(val)
L
#[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]

#For example, with curly braces you can create a set with a set comprehension:
 {n**2 for n in range(12)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121}
#The set comprehension respects this rule, and eliminates any duplicate entries:
 {a % 3 for a in range(1000)} Out [10]: {0, 1, 2}
#With a slight tweak, you can add a colon (:) to create a dict compre‐ hension:
 {n:n**2 for n in range(6)}
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#Finally, if you use parentheses rather than square brackets, you get what’s called a generator expression:
(n**2 for n in range(12))







#######################		GENERATOR ########################


#Generators
#A generator expression is essentially a list comprehension in which elements are generated as needed rather than all at once.

#List comprehensions use square brackets, while generator expressions use parentheses
#This is a representative list comprehension:
[n ** 2 for n in range(12)]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#While this is a representative generator expression:
(n ** 2 for n in range(12))
#<generator object <genexpr> at 0x104a60518>

#A list is a collection of values, while a generator is a recipe for producing values
#When you create a list, you are actually building a collection of val‐ ues, and there is some memory cost associated with that. 
#When you create a generator, you are not building a collection of values, but a recipe for producing those values. 
#Both expose the same iterator interface, as we can see here:
L = [n ** 2 for n in range(12)]
for val in L:
	print(val, end=' ')
#0 1 4 9 16 25 36 49 64 81 100 121
G = (n ** 2 for n in range(12))
for val in G:
	print(val, end=' ')
#0 1 4 9 16 25 36 49 64 81 100 121
#The difference is that a generator expression does not actually compute the values until they are needed. 
#This not only leads to memory efficiency, but to computational efficiency as well! 
#This also means that while the size of a list is limited by available memory, the size of a generator expression is unlimited!


#A list can be iterated multiple times; a generator expression is single use


L = [n ** 2 for n in range(12)]
for val in L:
print(val, end=' ')
print()

for val in L:
print(val, end=' ')
#0 1 4 9 16 25 36 49 64 81 100 121
#0 1 4 9 16 25 36 49 64 81 100 121
#A generator expression, on the other hand, is used up after one iteration:
G = (n ** 2 for n in range(12)) list(G)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
list(G)
#[]





#Example: Prime Number Generator
def gen_primes(N):
"""Generate primes up to N"""
	primes = set()
	for n in range(2, N):
		if all(n % p > 0 for p in primes):
			primes.add(n)
			yield n

print(*gen_primes(70))
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67






################# 			yield		####################

#we can make more complicated generators using generator functions, which make use of the yield  statement.
#Here we have two ways of constructing the same list:
  L1 = [n ** 2 for n in range(12)]

L2 = []
for n in range(12): L2.append(n ** 2)

print(L1) print(L2)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
#Similarly, here we have two ways of constructing equivalent generators:
G1 = (n ** 2 for n in range(12))

def gen():
	for n in range(12):
		yield n ** 2

G2 = gen() 
print(*G1) 
print(*G2)
#0 1 4 9 16 25 36 49 64 81 100 121
#0 1 4 9 16 25 36 49 64 81 100 121

#A generator function is a function that, rather than using return to return a value once, uses yield to yield a (potentially infinite) sequence of values. Just as in generator expressions, the state of the generator is preserved between partial iterations, but if we want a fresh copy of the generator we can simply call the function again.

Artık yield deyimini anlamak için, yeterli altyapıya sahibiz. yield deyimi, return deyimi gibi fonksiyonlarda kullanılır, ancak, fonksiyon bir generator döndürür. Şu örneğe bakalım;

def creategeneratorSquare(l):
    for x in l:
     yield x * x

generator = creategeneratorSquare([1,2,3,4,5])
for k in generator:
   print k

"""
Ekrana şunu basar:    
1
4
9
16
25
"""

#Yukarıdaki kod parçacığında, creategeneratorSquare isimli bir fonksiyon oluşturduk. Bu fonksiyonun, normal fonksiyonlardan farkı, bir generator döndürmesi. Bu fonksiyonu çağrıdığımızda, normal fonksiyonlardan beklediğimiz gibi, fonksiyonun gövdesi çalışmıyor, bunun yerine fonksiyon bir generator döndürüyor. Bu generator for döngüsü içinde kullanıldığında, fonksiyon içinde yazdığımız kod, yield görene kadar çalışıyor. Burada, yield deyimi "x * x" döndürüyor ve beklemeye başlıyor. Daha sonra, 6. satırdaki döngü, bir sonraki elemanı istedikçe, beklemedeki kod bloğu tekrar yield görene kadar çalışıp, yield gördüğünde sıradaki elemanı döndürüyor. Böylece, bu kod bloğu tamamlanıncaya kadar, 6. satırdaki for döngüsü k'ya farklı değerler atayıp, bunları ekrana bastırıyor.



def fibogenerator():
  a,b = 1,1
   while True:
     yield b
     a,b = b, a + b


for k in fibogenerator():
   if k > 10000000:
     print k
     break

"""
Ekrana şunu basar:  
14930352
"""

#Bu örnekte, biz istedikçe bir sonraki fibonacci sayısını veren bir generator kullanmak istedik. Bunun için, fibogenerator isimli bir fonksiyon yazdık. Bir önceki örnekten farklı olarak, bu sefer generator'u bir ara değişkende tutmaktansa, doğrudan for döngüsü içinde kullandık. Generator zaten tek kullanımlık olduğu için, bunları bir değişkene atamak çoğu zaman gereksiz. For döngüsünde ise, k 10 milyon'dan büyük olduğunda, k'yı ekrana bas ve döngüden çık dedik. Eğer döngüden çıkmak için herhangi birşey kullanmazsak, bu for döngüsü sonsuza kadar çalışırdı, çünkü, yazdığımız generator doğal yollardan sonlanmıyor.
