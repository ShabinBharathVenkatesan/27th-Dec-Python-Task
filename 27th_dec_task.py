
# 1. frequency count program

numbers = [1, 2, 3, 2, 4, 1, 5, 2, 4, 1]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)



# 2. expected output 
questions = []

while True:
    print("\n1. Add a question")
    print("2. Show the latest 5 questions")
    choice = input("Enter your choice: ")

    if choice == '1':
        question = input("Enter your question: ")
        questions.append(question)
        print("Question added!")

    elif choice == '2':  
        print("Latest 5 Questions:")
        for q in questions[-5:]:  
            print(q)


    else:
        print("Invalid choice. Please try again.")


# 3. write a program which will give u max,min and addition of values
numb = input("Enter the list of numbers: ").split()  

numb = [int(i) for i in numb]

smallest = numb[0]
largest = numb[0]
total_sum = 0


for num in numb:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    total_sum += num  

print("The smallest number is:", smallest)
print("The largest number is:", largest)
print("The sum of the numbers is:", total_sum)

            


