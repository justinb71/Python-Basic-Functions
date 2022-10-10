myFile = open("Text//Video Games Collection.txt", "wt")

myFile.write("Game Name          Format          PEGI Rating\n")
myFile.write("----------------------------------------------------------\n")

def addGame(name,form,rating):
    myFile.write(name)
    myFile.write("          ")
    myFile.write(form)
    myFile.write("          ")
    myFile.write(rating)
    myFile.write("+\n")

    
adding = True

while adding == True:
    name = input("\nEnter the name of the game: ")
    form = input("Enter the format of the game: ")
    rating = input("Enter the PEGI rating number: ")
    
    addGame(name, form, rating)
    
    cont = input("Enter y to continue and n to stop: ")

    if cont == "n":
        adding = False
        print("Text file has been created")


myFile.close()
