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

for item in all_friends:
    print(item[0], item[1], "age: ",item[2])

        
