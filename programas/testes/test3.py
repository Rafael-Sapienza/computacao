import os
if os.path.exists('myfile.txt'):
	print('yes')
	os.remove("myfile.txt")
else:
	print('no')



#Cria uma file
f = open("myfile.txt", "x")

#Deletes files and overwrites it
f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")

#Appends file
f = open("myfile.txt", "a")


A = 5*'\n'
f.write(f'{A}Ill have appended this file')

#prints file on command pallete
f = open("myfile.txt", "r")
A = f.read()
print(A)