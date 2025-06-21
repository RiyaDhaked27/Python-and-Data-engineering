a = 10
b = 20
if a is not b:          #if a is not equal to b so print a
    print(a)
st = "Python"
if "P" in st:
    print(st)

#print binary value of a number
print(bin(a))
print(bin(b))
print(a&b)

#if else conditions and nested if else conditions
n1 = int(input("enter a num: "))
if n1 % 2 == 0:
    print("number is even.")
    print()
    if n1 % 10 == 0:
        print("true")
        pass
else:
    print("number is odd.")

per = int(input("percentage?: "))
if per>80:
    print("Grade A")
elif per>60:
    print("Grade B")
else:
    print("Grade C")

#calculator
x = int(input("enter a number: "))
y = int(input("enter second number: "))
op = input("enter a operator for perform operation: ")
if op == '+' :
    print("addition is: ", x + y)
elif op == '-':
    print("subtraction is: ", x - y)
elif op == '*':
    print("multiplication is: ", x * y)
elif op == '/':
    print("division is:" ,x / y)
else:
    print("wrong choice")

#print statement with if condition
i = 20
if i < 50 : print("right")
print("riya") if i==10 else print("sweet")
