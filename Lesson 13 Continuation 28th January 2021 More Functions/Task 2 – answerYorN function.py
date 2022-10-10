def answerYorN(answer):
    result = ""
    if answer.lower() == "y":
        result = "Wrong"
    elif answer.lower() == "n":
        result = "Correct"
    else:
        result = "Try Again"
        
    return result


answer = answerYorN(input("Is The Earth Flat? Y or N: "))
print(answer)

