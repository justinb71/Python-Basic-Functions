import random

rolling = True
score = 0

while rolling == True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    if dice1 == dice2:
        if dice1 == 6:
            score += 0
        else:
            score = score * 2
    else:
        score += dice1 + dice2
    print("\nDice1 =",dice1,"    Dice2 =",dice2)

    rollAgain = input("\nEnter Yes To Roll Again Or Press No To Stop\n\n").lower()

    if rollAgain == "no":
        rolling = False
        break

print("Dice1 =",dice1,"    Dice2 =",dice2,"The Final Score Is",score)
        
    
    

