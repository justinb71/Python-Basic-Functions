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
    if i == 0:
       highestScore = results[0][2]
       name = results[0][0]
    else:
        if results[i][2]> highestScore:
            highestScore = results[i][2]
            name = results[i][0]
        else:
            highestScore = highestScore
            name = name
print(name,"had the highest score with",highestScore)
               

