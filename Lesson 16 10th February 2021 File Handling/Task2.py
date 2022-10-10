films = []

myFile = open("Text//Task4_films.txt", "rt")

films = myFile.readlines()

myFile.close()


for x in films:
    print(x, end="")
