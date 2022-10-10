import csv
allFriends = []

moreFriends = True
while moreFriends:
    name = input("Enter name    (Blank to stop): ")
    if name == "":
        moreFriends = False
    else:
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        friend = [name, email, phone]
        allFriends.append(friend)

file = open("CSVFiles\\Address Book.csv", "wt", newline="")

writer = csv.writer(file, delimiter = ",")

for friend in allFriends:
    writer.writerow(friend)
file.close()
