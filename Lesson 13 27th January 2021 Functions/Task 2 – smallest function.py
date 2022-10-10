def minimum(a, b, c):
    numbers = []
    numbers.append(a)
    numbers.append(b)
    numbers.append(c)

    minNum = min(numbers)
    return minNum

print(minimum(int(input("First number: ")),int(input("Seconds number: ")),int(input("Last number: "))))
        
