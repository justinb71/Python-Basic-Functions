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
        print(row[0],"is",row[2])

        
