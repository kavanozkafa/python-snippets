import json


print "This is a JSON example. JSON means JavaScript Object Notation.It is more faster and much lighter than XML."
print "REST API works with JSON"
print "It looks like python dictionary  \n \n \n"

movie = {}

movie['godfather'] = {
	'name' : 'godfather',
	'year' : 1972,
	'Genre' : "Drama"
}

movie['Gladiator'] = {
	'name' : 'gladiator',
	'year' : 2000,
	'Genre' : "Drama"
}

#assign this to a string
Film = json.dumps(movie)
print(Film)
print "\n\n"
#write this to a file
with open("/home/sammas/Desktop/films.txt", "w") as f:
	f.write(Film)

#read from that file
readFilm = open("/home/sammas/Desktop/films.txt", "r")
fileFilm = readFilm.read()
print("\nJSON file from file \n" + fileFilm)

print "\n\n"

#we can also access spesific data
print(movie['godfather'])
print(movie['godfather']['year'])