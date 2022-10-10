def colour(favColour):
    result = ""
    if favColour.lower() == "black":
        result = "Night"
    elif favColour.lower() == "blue":
        result = "Sky"
    elif favColour.lower() == "red":
        result = "Danger"
    else:
        result = "Don't Know"
    return result
answer = colour(input("What is your favourite colour?: "))
print(answer)
