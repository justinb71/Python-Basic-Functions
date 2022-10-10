def calcPerimeter(width, length):
    perimeter = (width*2) + (length*2)
    return perimeter

width = int(input("What is the width: "))
length = int(input("What is the length: "))

print("The perimeter is",calcPerimeter(width,length))
