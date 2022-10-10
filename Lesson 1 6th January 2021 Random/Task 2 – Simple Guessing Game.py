import random

randNum = random.randint(1, 50)

attempts = 0


while True:
    guess = int(input("Please Enter Your Guess "))

    if guess < randNum:
        print("Too Low")
        attempts  += 1
    elif guess > randNum:
        print("Too High")
        attempts += 1
    else:
        print("Correct, It Is",str(randNum)+". It Took You",attempts,"Tries")
        break
