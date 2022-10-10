import random

#Creates an array of Names
Names = ["John","Phillip","Sam","Poppy","Oliver","Leo","Thea","Freddie""Ava","Ivy"]

#Creates a random number from 0 to the length of the Names array
randNum = random.randint(0, len(Names))

#Finds the name corresponding to the random number
randName = Names[randNum]

#Prints out the random number and name
print("The random number is",randNum,"and the random name is",randName)

