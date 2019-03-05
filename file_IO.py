# r-read , dosya yoksa hata verir
#w-write, dosya yoksa olusturur.
#a-append, dosya yoksa olusturur. varsa ekleme yapar
# The os module provides methods for file processing
import os

file = open('myFile.txt','w')
file.write('write this down')
file.writelines(['\nline 1','\nline 2','\nline 3'])
file.close()



file = open('myFile.txt','r')
file.read()
file.readline()
file.readlines()

file.seek(3) #imleci 3.karakterin basina getirir.
file.seek(0) #dosya basi
file.seek(5,1) #imleci bulundugu konumdan 5 birim kaydir.
file.seek(5,0) # imleci dosya basindandan 5 birim kaydir.
file.seek(-5,2) # imleci bulundugu konumdan basa dogru 5 birim kaydir

file.tell() #imlecin konumunu verir.


# "with"  guarantees the file will be closed if the program crashes
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
	myFile.write("Some random text\nMore random text\nAnd some more")

# Find out if the file is closed
print(myFile.closed)
 
# Get the file name
print(myFile.name)
 
# Get the access mode of the file
print(myFile.mode)

# Rename our file
os.rename("mydata.txt", "mydata2.txt")


# Delete a file
os.remove("mydata.dat")

# Display current directory
print("Current Directory :", os.getcwd())
 