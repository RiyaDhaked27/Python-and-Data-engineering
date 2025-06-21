f = open("new1.txt", "w")
f.write("this is first line")
f.write("this is second line")
f.close()

#file read by for loop(file open in read mode)
f = open("new1.txt", "r")
for x in f:
    print(x)
#file read direct read command
f = open("new1.txt", "r")
print(f.read())
#...read file using with
with open("new1.txt")as file:
    data=file.read()
    print(data)

#...file open in append
f = open("new1.txt", "a")
f.write("this is first line")
f.close()
