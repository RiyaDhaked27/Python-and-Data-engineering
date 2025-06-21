d = {1:"python", 2:"java", 3:"name:", 4:"programming language", 5:{1:"one", 2:"two", 3:"three"}}
print(type(d))
print(d[3])
print(d[5])
print(d[5][2])

# #insertion in dictionary
Dict = {}
print(Dict)
Dict[1] = "My"
Dict[2] = "Name"
Dict[3] = "is"
Dict[4] = "Riya"
print(Dict)
#
#deletion in dictionary
del(d[3])                      #delete name element
print(d)

#print keys and items
print(Dict.keys())
print(Dict.items())
print(Dict.values())
# print(d.update(Dict))

#merge(update) two dictionaries
Dict.update(d)
print(Dict)

#copy dictionary
Dict = d.copy()
print(Dict)
d.clear()
print(d)                      #now first dictionary is clear(empty)


