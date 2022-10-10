films = []

myFile = open("Text//Task4_films.txt", "rt")

films = myFile.readlines()

myFile.close()

films.sort()

for x in films:
    print(x, end="")
