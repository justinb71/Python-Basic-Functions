games = []

myFile = open("Text//Task1_Games.txt", "rt")

games = myFile.readlines()

myFile.close()

for x in games:
    print(x, end="")
