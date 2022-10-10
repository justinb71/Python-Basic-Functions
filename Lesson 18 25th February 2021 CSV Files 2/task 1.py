import csv
allFriends = []

file = open("CSVFiles\\Address Book.csv", "rt")

reader = csv.reader(file, delimiter = ",")

for data in reader:
    allFriends.append(data)
file.close()


for friend in allFriends:
    print(friend)
