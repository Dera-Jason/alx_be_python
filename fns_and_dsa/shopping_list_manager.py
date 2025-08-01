shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is currently empty.")

    elif choice == "4":
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-4).")
