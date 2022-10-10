import csv

TITLE = ["Player Name","Game Name","Score"]

file = open("CSVFiles\\High Scores.csv", "wt", newline="")
writer = csv.writer(file, delimiter = ",")
writer.writerow(TITLE)

allScores = []
moreScores = True

while moreScores:
    playerName = input("Enter player name    (Blank to stop): ")
    if playerName == "":
        moreScores = False
    else:
        gameName = input("Enter game name: ")
        score = input("Enter score : ")

        score = [playerName, gameName, score]
        allScores.append(score)



for score in allScores:
    writer.writerow(score)
file.close()
