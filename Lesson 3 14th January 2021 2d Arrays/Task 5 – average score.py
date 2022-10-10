results = []

total = 0
playing = True
while playing == True:
    name = input("What is your name (blank to stop): ")
    if name == "":
        playing = False
    else:
        gameName = input("What is the name of the game: ")
        score = int(input("What is your highest score: "))

        player = [name,gameName,score]
        results.append(player)

    
        

for i in range(0,len(results)):
    total = total + results[i-1][2]

print("The average is",total/len(results))
               

