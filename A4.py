# ******************************* Assignment 4...que 1 ***********************************
#question 1
import csv
address_book = [['Name', 'Address', 'Mobile', 'email'],
                ['Abhay', 'Jaipur', 2345666, 'abc@123'],
                ['Riya', 'Agra', 7851077, 'riya@234'],
                ['Bhumi', 'USA', 6573894, 'bhumi@345']
                ]

with open("address_book.csv", "w", newline="") as file:
    write = csv.writer(file)
    for x in address_book:
        write.writerow(x)

with open("address_book.csv", "r", newline="") as file:
    read = csv.reader(file)
    for y in read:
        print(y)

# Question 3.....





