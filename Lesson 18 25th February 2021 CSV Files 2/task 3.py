import csv
allScores = []
changeValue = ""
file = open("CSVFiles\\High Scores.csv", "rt")

reader = csv.reader(file, delimiter = ",")

for data in reader:
    allScores.append(data)
file.close()


score=allScores[0]
print(score[0],"scored",score[2],"in",score[1])

changeVaule = input("Do you want to change the score (Enter y or n):\n")
print(changeVaule)
if changeValue.lower() == "y":
    changedScore = input("Enter new score: ")
    score[2] = changedScore
else:
    print("\n")
