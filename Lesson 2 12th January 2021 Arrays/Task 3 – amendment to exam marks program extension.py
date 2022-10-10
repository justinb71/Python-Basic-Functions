#Creates a list
ExamMarks = []
amountOfMarks = int(input("How many marks are you going to type: "))

#Asks the user to enter 5 marks
for i in range(0,amountOfMarks):
    mark = int(input("Please enter a mark: "))
    ExamMarks.append(mark)

#Finds the lowest and highest marks and prints it to the screen
print("\nThe highest mark is:",max(ExamMarks))
print("The lowest mark is:",min(ExamMarks))

#Sorts the list and prints it
ExamMarks.sort()
print("\nThe exam marks in order are:\n")

for x in ExamMarks:
    print(x)
