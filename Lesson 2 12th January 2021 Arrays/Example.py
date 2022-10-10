#creats an empty list
userNames = []

#Add the names to the list
userNames.append("Billy")
userNames.append("Jamie")
userNames.append("Evelyn")
userNames.append("Cathy")
userNames.append("Amy")

#Find the length of the list and print it to the screen
listLength = len(userNames)
print("The list length is:",listLength)

#Print the third element in the list
print("The third name in the list is:", userNames[2])

#Find the maximum value in the list and print it to the screen
maxValue = max(userNames)
print("The maximum value is:",maxValue)

#Find the minimum value in the list and print it to the screen
minValue = min(userNames)
print("The minimum value is:",minValue)

#Sort the list, then print it to the screen
userNames.sort()
print("The list after the names hae been sorted:")
for x in userNames:
    print(x)
