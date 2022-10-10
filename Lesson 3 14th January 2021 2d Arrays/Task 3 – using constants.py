#Define the index constants
NAME = 0
EMAIL = 1
AGE = 2


all_friends = []
getMore = True

while getMore:
    name = input("Enter name (blank to stop): ")

    if name == "":
        getMore = False
    else:
        email_address = input("Enter email: ")
        age = int(input("Enter age: "))
        
        friend = [name, email_address, age]
        all_friends.append(friend)



upper_age = int(input("\nEnter upper age limit: "))
print("\nThese friends are under",upper_age)
for row in all_friends:
    if row[AGE] < upper_age:
        print(row[NAME],"is",row[AGE])

        
