# menu card oops 

class MenuCard:
    def __init__(self):
        
        self.menu_card = ['Dosa', 'Idli', 'Biriyani']

    def display_menu(self):
        
        print("Menu Card:", self.menu_card)

    def add_item(self):
        
        new_item = input("Enter item to add: ")
        self.menu_card.append(new_item)
        print("Added:", new_item)

    def update_item(self):
        
        if 'Dosa' in self.menu_card:
            self.menu_card[self.menu_card.index('Dosa')] = 'Masala Dosa'
            print("'Dosa' updated to 'Masala Dosa'.")
        else:
            print("'Dosa' is not in the menu.")

    def delete_item(self):
        
        delete_item = input("Enter item to delete: ")
        if delete_item in self.menu_card:
            self.menu_card.remove(delete_item)
            print("Deleted:", delete_item)
        else:
            print(delete_item, "is not in the menu.")

    def run(self):
        
        while True:
            print("\nMenu Options:")
            print("1. Display Menu")
            print("2. Add Item")
            print("3. Update 'Dosa' to 'Masala Dosa'")
            print("4. Delete Item")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.display_menu()
            elif choice == 2:
                self.add_item()
            elif choice == 3:
                self.update_item()
            elif choice == 4:
                self.delete_item()
            elif choice == 5:
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

menu = MenuCard()
menu.run()

# to add withdraw,check balance and deposit

class BankAccount:
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def create_account(self):
        self.Name = input("Enter the Account Holder Name: ")
        self.Amount = int(input("Enter the Initial Amount: "))
        self.Address = input("Enter the Address: ")
        self.AccountNo = int(input("Enter the Account Number: "))

    def display_information(self):
        print("------Your Account Information------")
        print(f"Name of the Account Holder: {self.Name}")
        print(f"Address: {self.Address}")
        print(f"Account Number: {self.AccountNo}")
        print(f"Current Balance: {self.Amount}")

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount > 0:
            self.Amount += amount
            print(f"Successfully deposited {amount}. New Balance: {self.Amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if 0 < amount <= self.Amount:
            self.Amount -= amount
            print(f"Successfully withdrew {amount}. New Balance: {self.Amount}")
        elif amount > self.Amount:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current Balance: {self.Amount}")


def main():
    user_1 = BankAccount()
    print("Creating First Account:")
    user_1.create_account()

    while True:
        print("\n------Menu------")
        print("1. Display Information")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_1.display_information()
        elif choice == 2:
            user_1.deposit()
        elif choice == 3:
            user_1.withdraw()
        elif choice == 4:
            user_1.check_balance()
        elif choice == 5:
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# Create a calculator using dictionary

operations = {
    "1": ("Add", lambda a, b: a + b),
    "2": ("Subtract", lambda a, b: a - b),
    "3": ("Multiply", lambda a, b: a * b),
    "4": ("Divide", lambda a, b: a / b if b != 0 else "Error! Division by zero"),
}

while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in operations:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        
        operation = operations[choice][1]  
        result = operation(a, b)         
        print(f"Result: {result}")
    else:
        print("Invalid choice, try again!")

