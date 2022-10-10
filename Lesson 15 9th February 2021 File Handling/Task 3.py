myFile = open('Text//Task3_UserGames.txt','wt')


game1 = input("Enter the first game: ")+"\n"
game2 = input("Enter the second game: ")+"\n"
game3 = input("Enter the third game: ")+"\n"
game4 = input("Enter the fourth game: ")+"\n"
game5 = input("Enter the fifth game: ")+"\n"

myFile.write("Users Favourite Games\n")
myFile.write("---------------------\n")
myFile.write(game1)
myFile.write(game2)
myFile.write(game3)
myFile.write(game4)
myFile.write(game5)

myFile.close()
