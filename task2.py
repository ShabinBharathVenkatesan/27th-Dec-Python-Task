# Access values from the 'fruits' list
fruits = ['mango', ['fruitpulp', 'mixedpulp'], 'banana', ('apple', 'grapes')]

# Accessing elements
print(fruits[0])  # mango
print(fruits[1])  # ['fruitpulp', 'mixedpulp']
print(fruits[1][0])  # fruitpulp
print(fruits[1][1])  # mixedpulp
print(fruits[3][0])  # apple
print(fruits[3][1])  # grapes

# Iterate over a list using a for loop and range function
Menu = ['Dal', 'Paneer', 'Kofta', 'Tawa Paneer', 'Rice', 'Roti']
for i in range(len(Menu)):
    print(Menu[i])

# Iterate over a tuple using a for loop
author_name = ('j k rowling', 'rachel aaron', 'hans aanrud', 'verna aardema')
for i in range(len(author_name)):
    print(author_name[i])

# Print timing
Timing = 'It\'s 7.30am'
print(Timing)

# Input from user and display employee details
employee_name = input("Enter Employee Name: ")
salary = input("Enter Salary: ")
company = "ChangPond Technology"
print("\nPrinting Employee Details")
print("Name", "Salary", "Company")
print(employee_name, salary, company)

# Based on strings
print('Hello World')  # Output 1
print(r'E:\ChangpondNewBatch\Python')  # Output 2 (raw string for escape characters)

# Create dynamic lists
float_list = [float(input(f"Enter float element {i+1}: ")) for i in range(5)]
print("Dynamic Float List:", float_list)

string_list = [input(f"Enter string element {i+1}: ") for i in range(5)]
print("Dynamic String List:", string_list)

# Iterate over a while loop
i = 0
while i < len(Menu):
    print(Menu[i])
    i += 1

# Iterate over author_name using a while loop
i = 0
while i < len(author_name):
    print(author_name[i])
    i += 1

# Display results using range function
# For loop: 3, 6, 9, 12, 15
for i in range(3, 16, 3):
    print(i, end=" ")
print()

# While loop: 12, 9, 6, 3
i = 12
while i >= 3:
    print(i, end=" ")
    i -= 3
print()

# List Methods
Menu = ['Dal', 'Paneer', 'Kofta', 'Tawa Paneer', 'Rice', 'Roti']
# Replace 'Tawa Paneer' with 'Malai Paneer'
Menu[Menu.index('Tawa Paneer')] = 'Malai Paneer'

# Replace 'Rice' and 'Roti' with 'Tandoori Roti' and 'Naan'
Menu[Menu.index('Rice')], Menu[Menu.index('Roti')] = 'Tandoori Roti', 'Naan'
print("Updated Menu:", Menu)

# Iterate over fruits list using a for loop
for item in fruits:
    if type(item) == list or type(item) == tuple:
        for i in item:  
            print(i)
    else:
        print(item)

