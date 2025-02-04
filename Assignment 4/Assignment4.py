# Initialize empty personal info dictionary and friends list
personal_info = {}
friends = []

def add_friend():
    print("\nAdd A New Friend:")
    name = input("Enter friend's name: ")
    age = int(input("Enter friend's age: "))
    favColours = input("Enter friend's favorite colors (comma-separated): ").split(",")
    Job = input("Enter friend's Job: ")
    city = input("Enter friend's city: ")
    quote = input("Enter friend's quote: ")
    
    # Store friend's information in personal_info dictionary
    personal_info[name] = {
        "age": age,
        "favColours": favColours,
        "Job": Job,
        "city": city,
        "quote": quote
    }
    
    # Add friend's name to the friends list
    friends.append(name)
    print(f"{name} has been added to your friends list.")

def edit_friend():
    if not friends:
        print("You have no friends to edit. Add some friends first!")
        return
    
    print("\nCurrent friends:")
    for i, friend in enumerate(friends):
        print(f"{i+1}. {friend}")
    
    index = int(input("Enter the number of the friend to edit: ")) - 1
    if 0 <= index < len(friends):
        name = friends[index]
        print(f"\nEditing {name}:")
        personal_info[name]["age"] = int(input(f"Enter new age (current: {personal_info[name]['age']}): "))
        personal_info[name]["favColours"] = input(f"Enter new favorite colors (comma-separated, current: {', '.join(personal_info[name]['favColours'])}): ").split(",")
        personal_info[name]["Job"] = input(f"Enter new Job (current: {personal_info[name]['Job']}): ")
        personal_info[name]["city"] = input(f"Enter new city (current: {personal_info[name]['city']}): ")
        personal_info[name]["quote"] = input(f"Enter new quote (current: {personal_info[name]['quote']}): ")
        print(f"{name}'s information has been updated.")
    else:
        print("Invalid friend number.")

def RmvFriend():
    if not friends:
        print("You have no friends to remove. Go make some friends first!")
        return
    print("\nCurrent friends:")
    for i, friend in enumerate(friends):
        print(f"{i+1}. {friend}")
    index = int(input("Enter the number of the friend to remove: ")) - 1
    if 0 <= index < len(friends):
        removed_friend = friends.pop(index)
        del personal_info[removed_friend]
        print(f"{removed_friend} has been removed from your friends list.")
    else:
        print("Invalid friend number.")

def display_info():
    if not personal_info:
        print("\nNo information available. Please add some friends first.")
    else:
        print("\nFriends Information:")
        for name, info in personal_info.items():
            print(f"\n{name}:")
            for key, value in info.items():
                if isinstance(value, list):
                    print(f"  {key.capitalize()}: {', '.join(value)}")
                else:
                    print(f"  {key.capitalize()}: {value}")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add a friend")
    print("2. Edit a friend")
    print("3. Remove a friend")
    print("4. Display information")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_friend()
    elif choice == '2':
        edit_friend()
    elif choice == '3':
        RmvFriend()
    elif choice == '4':
        display_info()
    elif choice == '5':
        print("Goodbye! May your fufu always be smooth!")
        break
    else:
        print("Invalid choice. Please try again, or are you waiting for Ghana-maybe time?")
