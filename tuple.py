# we cannot modify tuple(we can not delete and insert a particular element in a tuple). Tuple is ordered
t = (10,20,30,20,40,10,50)        #boolean values always give in without quotes and in capital letters
t2 = ('a', 'b')
t3 = (t, t2)
print(t3)
print(type(t))
print(t)
print(t[3])           #print a particular value
l = (len(t))
print(l)
# for x in range(l):
#     print(x)          #print only index number
# for x in range(l):
#     print(t[x])       #print only tuple values
# for x in range(l):
#     print(x, t[x])    #print both index number nad values

# t4 = (1,2,3)           # we cannot modify tuple(we can not delete and insert a particular element in a tuple)
# del t4                 #give error
#print(t4)

t = ('30',)*3
print(t)

#tuple operations.....
tp = (15,40,50,20,15,50,100,40)
print(min(tp))
print(max(tp))
c = tp.count(15)
print(c)
print(sum(tp))
print(tp.index(100))




