#Creates a list
myList = []

#Adds 5 integers to the list
myList.append(1)
myList.append(132)
myList.append(43)
myList.append(65)
myList.append(12)

#Prints out the max and min values
print("The maximum value is:",max(myList))
print("The minimum value is:",min(myList))

#Sorts the list and prints it to the screen
myList.sort()

for x in myList:
    print(x)
