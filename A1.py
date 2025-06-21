Name = input("enter student name:")
Class = input("enter student branch:")
s1 = float(input("Enter marks for Subject 1: "))
s2 = float(input("Enter marks for Subject 2: "))
s3 = float(input("Enter marks for Subject 3: "))
s4 = float(input("Enter marks for Subject 4: "))
s5 = float(input("Enter marks for Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
per = total/5
print(f"The percentage of student is: {per:.2f}%")
if per>30:
    print("Grade A")
elif per>20:
    print("Grade B")
else:
    print("Grade C")
# print the output
print(f"The name of student is: {Name}")
print(f"The branch of student is: {Class}")
print(f"The total marks of student in five subjects are: {total}")

#que2. concatenation of two strings
str1 = input("enter first string: " )
str2 = input("enter second string: " )
str = str1 + str2
print(str)
print(str.lower())
print(str.upper())
print(str.title())         #first letter is capital
print(len(str))
print(str.count('i'))      #count the index of 'i'
print(str.isalpha())
print(str.isdigit())
print("reverse of string: ", str[::-1])