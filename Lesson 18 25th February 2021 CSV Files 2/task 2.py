import csv
allScores = []

file = open("CSVFiles\\High Scores.csv", "rt")

reader = csv.reader(file, delimiter = ",")

for data in reader:
    allScores.append(data)
file.close()


for score in allScores:
    print(score[0],"scored",score[2],"in",score[1])
