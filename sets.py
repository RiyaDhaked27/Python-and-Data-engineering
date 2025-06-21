#......sets are unordered, unchangeable(items are unchangeable But you can remove and add items.), unindexed, written in curly brackets
s1 = {5,2,8,4,5,6,7}
s2 = {"a", "b", "c", "d", 5, 6, 2}
print(type(s1))
print(s1)
s1.add("Apple")           #add a element in set
print(s1)
s3 = s1.union(s2)
print(s3)
# s4 = s1|s2
# print(s4)
#s4 = s1&s2
#print(s4)
# s5 = set()
# s6 = set()
# for i in range(5):
#     s5.add(i)
#     for i in range(3, 9):
#         s6.add(i)
#         s7 = s5.intersection(s6)
#         print(s7)

#difference
# for i in range(3, 9)

