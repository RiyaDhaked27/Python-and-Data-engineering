# #assignment 3....que 2
# def calculator():
#     x = int(input("Enter the first number: "))
#     y = int(input("Enter the second number: "))
#
#     print('''
# Choose an operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# ''')
#
#     choice = input("Enter your choice (1-4): ")
#
#     if choice == '1':
#         print("Sum:", x + y)
#     elif choice == '2':
#         print("Subtraction:", x - y)
#     elif choice == '3':
#         print("Multiplication:", x * y)
#     elif choice == '4':
#         if y == 0:
#             print("Error: Division by zero is not allowed.")
#         else:
#             print(f"Division:, {x / y:.2f}")
#     else:
#         print("Invalid choice. Please select from 1 to 4.")
#
# calculator()

#que 3.....
# def palindrome():
#     n = int(input("enter a number with any no.of digits: "))
#     original = n
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n//10
#
#     if rev == original:
#        print(f"{original} number is palindrome.")
#     else:
#        print(f"{original} number is not palindrome.")
#
#
# palindrome()

# *********************** ROck Paper scissor Game ****************************
import random
def rock_paper_scissor():
    print("welcome to rock paper scissors game!...")
    choices = ["rock", "paper", "scissors"]
    print('''options are:
    1.Rock
    2. Paper
    3. Scissors''')
    user = input("enter your choice: ")
    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("game tie up.")
    elif user == 'rock':
        if computer == 'paper':
            print("computer wins.")
        else:
            print("user wins.")
    elif user == 'scissors':
        if computer == 'rock':
            print("computer wins.")
        else:
            print("user wins.")
    elif user == 'paper':
        if computer == 'scissors':
            print("computer wins.")
        else:
            print("user wins.")
    else:
        print("wrong choice!,choose among only rock, paper, scissors.")



rock_paper_scissor()
