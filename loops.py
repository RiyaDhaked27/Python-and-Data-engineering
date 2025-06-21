for x in range(1,10,2):        #(intial, condition, increment)
    print(x)
for y in range(9, 0, -1):
    print(y)
for a in range(9, 0, -1):
    pass
print("python")

#genrate a table
# n1 = int(input("enter a number: "))
# print("table is: ")
# for b in range(1,11,1):
#     print( n1, "*", b, "=", n1 * b)

# only print odd numbers in table of a number
# n2 = int(input("enter a number: "))
# print("table is: ")
# for p in range(1,11,1):
#     if n2%2==0:
#         continue
#     print( n2, "*", p, "=", n2 * p)

#nested for loop
for c in range(2,5):
    for s in range(1,11):
        print(c, "*", s, "=", c*s)

#pattern
for i in range(0,10):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# while loop....
num = 1
while num <= 3:
    print (num)
    num+=1

#i=1
while True:   #condition is always true khud se hi le li
     n = int(input("enter a number and 0 for exit"))
     if n == 0:
        break
     print(n)