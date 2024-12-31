# Initial menu
menu_card = ['Dosa', 'Idli', 'Biriyani']

while True:
    print("\nMenu Options:")
    print("1. Display Menu")
    print("2. Add Item")
    print("3. Update 'Dosa' to 'Masala Dosa'")
    print("4. Delete Item")
    print("5. Exit")

    
    choice = int(input("Enter your choice: "))

    if choice == 1:
    
        print("Menu Card:", menu_card)

    elif choice == 2:
        
        new_item = input("Ener item to add: ")
        menu_card.append(new_item)
        print("Added:", new_item)

    elif choice == 3:
        
        if 'Dosa' in menu_card:
            menu_card[menu_card.index('Dosa')] = 'Masala Dosa'
            print("'Dosa' updated to 'Masala Dosa'.")
        else:
            print("'Dosa' is not in the menu.")

    elif choice == 4:
        
        delete_item = input("Enter item to delete: ")
        if delete_item in menu_card:
            menu_card.remove(delete_item)
            print("Deleted:", delete_item)
        else:
            print(delete_item, "is not in the menu.")

    elif choice == 5:
        
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")

print("\n Calculator")

def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Floor Division (//)")
    print("6. Exponentiation (**)")

    
    choice = int(input("Enter the number of the operation (1-6): "))

    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    if choice == 1:
        print("Result:", num1 + num2)
    elif choice == 2:
        print("Result:", num1 - num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        if num2 != 0:
            print("Result:", num1 // num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 6:
        print("Result:", num1 ** num2)
    else:
        print("Invalid choice, please try again.")


calculator()
