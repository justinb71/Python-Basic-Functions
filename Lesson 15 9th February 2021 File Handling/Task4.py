myFile = open("Text//Task4_films.txt","wt")

movie1 = input("Enter the first movie: ")+"\n"
movie2 = input("Enter the second movie: ")+"\n"
movie3 = input("Enter the third movie: ")+"\n"
movie4 = input("Enter the fourth movie: ")+"\n"
movie5 = input("Enter the fifth movie: ")+"\n"

myFile.write("Users Films\n")
myFile.write("-----------\n")
myFile.write(movie1)
myFile.write(movie2)
myFile.write(movie3)
myFile.write(movie4)
myFile.write(movie5)

myFile.close()
