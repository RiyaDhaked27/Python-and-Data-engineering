str = "my name is sweetie"
print(str[4])                       # 4 for print a letter
print(str[0:5])                     # print letters 0 to less than 5
print(str[1:])                      # start with 2nd letter and print upto the last
print(str[0::2])                    #start with 0 letter with one one letters skip
l = len(str)
print(l)                            # length counts starts with 1
# for x in l:                       #print single single letter of a string
#     print(str(x))

#string reverse

print(ord("A"))                     #give ascii value of character

#lists.......
s = [10,20,30,40,"python",[1,2,3]]
print(s)
print(type(s))
print(s[4])
print(s[5][1])                      #5 element ka 1 index letter
s.reverse()                         #reverse of a list
print(s)
print(len(s))                       #lenght count starts with 1

#find max and min number
# x = [2,3,4,1,5]
# max = x[0]
# for

#split function
# t = input("enter element(separate by space)")

#append the list
k = [1,2]
k.append(10)
k.append(20)
print(k)
k.insert(0,5)
print(k)
k.extend(["x", "y"])
print(k)
k.remove(10)
print(k)