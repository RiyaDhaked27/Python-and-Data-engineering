#que2......
# Name = input("enter student name:")
# Class = input("enter student branch:")
# s1 = float(input("Enter marks for Subject 1: "))
# s2 = float(input("Enter marks for Subject 2: "))
# s3 = float(input("Enter marks for Subject 3: "))
# s4 = float(input("Enter marks for Subject 4: "))
# s5 = float(input("Enter marks for Subject 5: "))
#
# total = s1 + s2 + s3 + s4 + s5
# per = total/5
# # display the output
# print(f"The name of student is: {Name}")
# print(f"The branch of student is: {Class}")
# print(f"The total marks of student in five subjects are: {total}")
# print(f"The percentage of student is: {per:.2f}%")
# if per>=60:
#     print("Grade A")
# elif per>=50 and per<60:
#     print("Grade B")
# elif per>=40 and per<50 :
#     print("Grade C")
# elif per >= 33 and per < 40:
#     print("Grade D")
# else:
#     print("fail")
#

#que3.......
n = int(input("enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("factorial of", n, "is=", fact)

#que5......
x = [2,3,4,1,5]
small = x[0]
for j in range(len(x)):
    if small>x[j]:
        small = x[j]
        print("the smallest number is", small)
# second smallest number....
second_small = None
for j in range(len(x)):
    if x[j] != small:
        if second_small is None or x[j] < second_small :          # because '<' is not working in between str and int so we will use None keyword
            second_small = x[j]


if second_small is not None:
    print("second smallest number is:", second_small)
else:
    print("no second smallest is present in list.")

#find largest number....
y = [10, 80, 100, 40, 60]
largest = y[0]
for i in range(len(y)):
    if largest < y[i]:
        largest = y[i]
        print("maximum number is: ", largest)
# now find second_largest number
second_largest = None
for i in range(len(y)):
    if y[i] != largest:
        if second_largest is None or second_largest < y[i]:
            second_largest = y[i]

if second_largest is not None:
            print("the second maximum number is: ", second_largest)
else:
    print("no second maximum is present in list.")

# #que4........
# items = []
# prices = []
# total_bill = 0
# while True:
#     print('''1. Create Bill (Add Item)
#     2. Display Items with Prices and Total Bill
#     3. Display Total Amount Only
#     4. Exit''')
#
#     choice = int(input("Enter your choice (1-4): "))
#
#     if choice == 1:
#         # item = input("Enter item name: ")
#         # price = float(input("Enter item price: "))
#         # items.append(item)
#         # prices.append(price)
#         # print(f"'{item}' added to the bill price is '{price}'")
#         print("bill created: ")
#         prices.clear()
#         total_bill = 0
#     elif choice == 2:
#         item = input("Enter item name: ")
#         price = float(input("Enter item price: "))
#      # items.append(item)
#         prices.append(price)
#         if not items:
#             print("No items added yet.")
#         else:
#             print("\n--- Bill Details ---")
#             total_bill = 0
#             for i in range(len(items)):
#
#                 total_bill += prices[i]
#             print("Total Amount: ₹", total_bill)
#     elif choice == 3:
#         total_bill = sum(prices)
#         print("Total Bill Amount: ₹", total_bill)
#
#     elif choice == 4:
#         print("Exiting the billing program. Thank you!")
#         break
#     else:
#          print("Invalid choice! Please choose from 1 to 4.")
#
#
#que 4 using dictionary...
bill_items = {}
while True:
    print('''
1. Create Bill 
2. Display Items with Prices and Total Bill
3. Display Total Amount Only
4. Exit''')

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        bill_items[item] = price
        print(f"'{item}' added to the bill with price ₹{price:.2f}")

    elif choice == 2:
        if not bill_items:
            print("No items added yet.")
        else:
            print("\n--- Bill Details ---")
            total = 0
            for item, price in bill_items.items():
                print(f"{item}: ₹{price:.2f}")
                total += price
            print("Total Amount: ₹", total)

    elif choice == 3:
        if not bill_items:
            print("No items added yet.")
        else:
            total = sum(bill_items.values())
            print("Total Bill Amount: ₹", total)

    elif choice == 4:
        print("Exiting the billing program. Thank you!")
        break

    else:
        print("Invalid choice! Please choose from 1 to 4.")
