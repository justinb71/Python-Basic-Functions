def addIntegers(minimum, maximum):
    total = 0
    for i in range(minimum, maximum+1):
        total += i
       
    return total

print(addIntegers(5,10))
