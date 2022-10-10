finished = False
total = 0
myFile = open("Text//Task5_Price.txt","wt")

while finished == False:

    
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    total = total + price
    
    myFile.write(name)
    myFile.write(" = £")
    myFile.write(str(price))
    myFile.write("\n")
    
    addItem = input("\ny for continue n for stop: ").lower()

    if addItem == "n":
        finished = True
        myFile.write("---------------\n")
        myFile.write("The total is: £")
        myFile.write(str(total))


myFile.close()
    
    

